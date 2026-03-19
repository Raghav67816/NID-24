import numpy as np
from os import kill
from signal import SIGINT
from scipy.signal import decimate

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QProcess, Signal, QObject, QTimer
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo


"""
Connect your android app before you start the reader
"""
class DataReader(QObject):
    data_ready = Signal(object)

    def __init__(self):
        super(DataReader, self).__init__()

        self.isReading = False
        self.isOpen = False

        self.internal_buffer = np.array([])
        
        self.serial_port = QSerialPort()
        self.serial_port.setBaudRate(QSerialPort.Baud115200)
        self.serial_port.setReadBufferSize(1024)
        self.serial_port.setFlowControl(QSerialPort.FlowControl.HardwareControl)
        self.serial_port.setParity(QSerialPort.Parity.NoParity)
                
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

    def on_data_rcvd(self):
        """
        worked like a charm for 6 mins
        """
        data_b = self.serial_port.readLine().data().decode("utf-8")
        self.internal_buffer = np.append(self.internal_buffer, float(data_b))
        if len(self.internal_buffer) > 200:
            self.data_ready.emit(decimate(self.internal_buffer, 3))
            self.internal_buffer = np.array([])


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
        self.setArguments(["watch", "hci0"])
        self.start()
        print(self.readAllStandardError())

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
