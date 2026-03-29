import numpy as np
from signal import SIGINT
from os import kill, system
from struct import unpack, error
from scipy.signal import decimate

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QProcess, Signal, QObject, QTimer
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo


"""
Connect your android app before you start the reader

This class manages unpacking and sending data to other classes.
This is the entry gate for the data.

for now we only create vbuffers should hold 100 values
"""
class DataReader(QObject):

    update = Signal(object, object, object)

    PLOT_UPDATE_INTERVAL = 60 # ms
    BUFFER_SIZE = 1000
    VBUFFER_SIZE = 100
    DECI_CNT = 6

    def __init__(self):
        super(DataReader, self).__init__()

        self.isReading = False
        self.isOpen = False

        self.data_unpacked = None

        self.index = 0
        self.vindex = 0

        # buffers
        self.buffer_a = np.zeros(self.BUFFER_SIZE + 1)
        self.buffer_b = np.zeros(self.BUFFER_SIZE + 1)
        self.buffer_c = np.zeros(self.BUFFER_SIZE + 1)

        self.vbuffer_a = np.zeros(self.VBUFFER_SIZE + 1)
        self.vbuffer_b = np.zeros(self.VBUFFER_SIZE + 1)
        self.vbuffer_c = np.zeros(self.VBUFFER_SIZE + 1)

        self.x = np.zeros(self.VBUFFER_SIZE + 1)
        
        # graph update timer
        self.update_timer = QTimer()
        self.update_timer.setInterval(self.PLOT_UPDATE_INTERVAL)
        self.update_timer.timeout.connect(self.update_plots) # TODO: MAKE UPDATE GRAPH FUNCTION
        self.update_timer.start()
        
        self.serial_port = QSerialPort()
        self.init_serial()
                
        self.serial_port.readyRead.connect(self.on_data_rcvd)
        self.serial_port.errorOccurred.connect(self.on_error)

    def init_serial(self):
        self.serial_port.setBaudRate(QSerialPort.Baud115200)
        self.serial_port.setReadBufferSize(1024)
        self.serial_port.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        self.serial_port.setParity(QSerialPort.Parity.NoParity)
        self.serial_port.setReadBufferSize(12) # in bytes (3 floats, 4 bytes per float)

    def open_port(self):
        try:
            self.serial_port.setPortName("/dev/rfcomm0")
            self.isOpen = self.serial_port.open(QSerialPort.ReadOnly)
            print(f"is port opened: {self.isOpen}")
            

        except Exception as e:
            print("failed to open ports")
            self.isOpen = False
            print(str(e))

    def on_error(self):
        print(f"Error occurred: {self.serial_port.error()}")

    def on_data_rcvd(self):
        data_packed = self.serial_port.readAll()
        try:
            self.data_unpacked = unpack("<fff", bytes(data_packed))

        except error:
            pass

        # reset index, keeps rolling
        if self.index >= self.BUFFER_SIZE:
            self.index = 0

        # flip data
        
    def update_plots(self):
        self.vbuffer_a[:-1] = self.vbuffer_a[1:]
        self.vbuffer_b[:-1] = self.vbuffer_b[1:]
        self.vbuffer_c[:-1] = self.vbuffer_c[1:]

        self.vbuffer_a[-1] = round(self.data_unpacked[0], 6)
        self.vbuffer_b[-1] = round(self.data_unpacked[1], 6)
        self.vbuffer_c[-1] = round(self.data_unpacked[2], 6)
    
        self.update.emit(self.vbuffer_a, self.vbuffer_b, self.vbuffer_c)
    
    def cleanup(self):
        self.isOpen = False
        self.serial_port.close()
        


"""
the system communicates with ADS1293 via bluetooth (rfcomm)
simulators are also designed with bluetooth protocol in mind

this class internally handles:
1. binding baddr to virtual port
2. look after QProcess
"""
class RFCommProcess(QProcess):

    com_started = Signal()

    """
    int should be -1 for errors
    1 for graceful exit
    """
    com_finished = Signal(int, str)
    new_connection = Signal()
    
    def __init__(self, app):
        super(RFCommProcess, self).__init__(app)

        self.addr = None
        self.setProgram("/usr/bin/rfcomm")
        
        self.setProcessChannelMode(QProcess.MergedChannels)

        self.finished.connect(self.on_process_finish)
        self.errorOccurred.connect(self.on_error_occurred)
        self.readyReadStandardOutput.connect(self.on_read_output)

    def set_device_addr(self, addr: str):
        self.addr = addr

    def start_process(self):
        # first add sdp profile
        try:
            system("sdptool add SP")
            print("Profile added")

            self.setArguments(["listen", "hci0 1"])
            self.start()
            print(self.readAllStandardError())

        except Exception as error:
            print("Failed to add profile.")
            print(str(error))

    def on_process_finish(self, exit_code: int):
        msg = f"RFComm exited with {str(exit_code)}"
        if exit_code != 0:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Connection Error")
            msgBox.setText(msg)
            msgBox.setStandardButtons(QMessageBox.StandardButtons.Close)
            
        self.com_finished.emit(-1, msg)

    def on_read_output(self):
        data = self.readAllStandardOutput().data()
        if not data:
            return

        data_str = data.decode("utf-8")
        print(data_str)

    def on_error_occurred(self, error: QProcess.ProcessError):
        print("Error occurred")
        print(self.error())


    def cleanup(self):
        try:
            kill(self.processId(), SIGINT)
            print("Process finished")

        except Exception as error:
            print("error intterupting the process")
            print(str(error))

        hasEnded = self.waitForFinished(5000)
        if not hasEnded:
            self.terminate()
