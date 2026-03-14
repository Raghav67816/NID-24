from theme_engine import prepare_sheet
from ui.connection_ui import Ui_DeviceConnDialog

from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import QObject, Signal
from PySide6.QtBluetooth import QBluetoothLocalDevice


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

        self.refresh_view()

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
