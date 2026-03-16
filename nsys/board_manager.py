from theme_engine import prepare_sheet
from ui.connection_ui import Ui_DeviceConnDialog

from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QObject, Signal, QProcess
from PySide6.QtBluetooth import QBluetoothLocalDevice
from PySide6.QtWidgets import QDialog, QListWidgetItem


"""
this class will not manage pairing
the user is required to pair the board via native settings menu
"""

class BoardManager(QDialog):
    def __init__(self):
        super(BoardManager, self).__init__()

        self.ui = Ui_DeviceConnDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Connect Board")
        self.setModal(True)

        self.setStyleSheet(prepare_sheet())

        self.localDevice = QBluetoothLocalDevice()
        self.deviceItems = []
        self.rfcomm_process = None

        self.serial_port = QSerialPort()
        # configure serial port
        self.serial_port.setPortName("/dev/rfcomm0")
        self.serial_port.setReadBufferSize(1024)
        # self.serial_port.setBaudRate(QSerialPort.Baud11520) # check this

        self.on_device_selected = Signal(str)
        self.on_rfcomm_started = Signal(str)
        self.on_rfcomm_finished = Signal(int)

        self.refresh_view()

        # self.on_device_selected.connect(__on_device_selected__)
        self.ui.refreshBtn.clicked.connect(self.refresh_view)

    def refresh_view(self):
        for deviceItem in self.deviceItems:
            row = self.ui.devicesContainer.row(deviceItem)
            item = self.ui.devicesContainer.takeItem(row)
            del item

        self.deviceItems.clear()

        for device in self.localDevice.connectedDevices():
            item = QListWidgetItem()
            item.setText(device.toString())
            self.ui.devicesContainer.addItem(item)
            self.deviceItems.append(item)
            
        
    def show_board_manager(self):
        self.show()
        self.exec()


    def on_dialog_accepted(self):
        device = self.ui.devicesContainer.currentItem()
        self.on_device_selected.emit(device.text())

    def __on_device_selected__(self, device_addr: str):
        self.rfcomm_process = QProcess()
        self.rfcomm_process.setArguments(["bind", "/dev/rfcomm0", device_addr, 1])
        self.rfcomm_process.started.connect(self.__on_rfcomm_started__)
        self.rfcomm_process.finished.connect(self.__on_rfcomm_exit__)
        self.rfcomm_process.execute()

    def __on_rfcomm_exit__(self, code: int, exitStatus: QProcess.ExitStatus):
        self.on_rfcomm_exit.emit(code)

    def __on_rfcomm_started__(self):
        self.on_rfcomm_started.emit()
