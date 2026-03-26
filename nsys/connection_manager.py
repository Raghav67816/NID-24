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
"""
class DataReader(QObject):
    data_ready = Signal(object, object, object) # send both ch1 and ch2 data

    def __init__(self):
        super(DataReader, self).__init__()

        self.isReading = False
        self.isOpen = False

        self.buffer_a = np.array([])
        self.buffer_b = np.array([])
        self.buffer_c = np.array([])

        self.data_unpacked = None
        
        self.serial_port = QSerialPort()
        self.serial_port.setBaudRate(QSerialPort.Baud115200)
        self.serial_port.setReadBufferSize(1024)
        self.serial_port.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        self.serial_port.setParity(QSerialPort.Parity.NoParity)
        self.serial_port.setReadBufferSize(12) # in bytes (3 floats, 4 bytes per float)
                
        self.serial_port.readyRead.connect(self.on_data_rcvd)
        self.serial_port.errorOccurred.connect(self.on_error)

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

    """
    receving: bytearray -> QByteArray
    we are using little eadian byte order
    we unpack data with <ff tag.

    float values might have more decimal places than the original float
    don't worry data is fine. it's just that computers can't represent it precisely.

    trim the float till 2nd decimal place.
    """
    def on_data_rcvd(self):
        data_b = self.serial_port.readAll()

        try:
            self.data_unpacked = unpack("<fff", bytes(data_b))

        except error:
            pass # it's just that the data size is not 8 bytes (corruption possible let's bribe the data)
        
        self.buffer_a = np.append(self.buffer_a, round(self.data_unpacked[0], 6))        
        self.buffer_b = np.append(self.buffer_b, round(self.data_unpacked[1], 6))
        self.buffer_c = np.append(self.buffer_c, round(self.data_unpacked[2], 6))

        if len(self.buffer_a) == 1000 and len(self.buffer_b) == 1000 and len(self.buffer_c) == 1000:
            self.data_ready.emit(self.buffer_a, self.buffer_b, self.buffer_c)
            self.buffer_a = np.array([])
            self.buffer_b = np.array([])
            self.buffer_c = np.array([])

    def cleanup(self):
        self.isOpen = False
        self.serial_port.close()
        


"""
the system communicates with ADS1293 via bluetooth (rfcomm)
simulators are also designed with bluetooth protocol in mind

this class internally handles:
1. binding baddr to virtual port
2. reading data from it
3. sending it to main application
4. look after QProcess
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
