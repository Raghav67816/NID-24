# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtGui import QAction
from theme_engine import prepare_sheet 
from PySide6.QtCore import QMargins, Qt, QProcess, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox

import pyqtgraph as pg

from board_manager import BoardManager
from graphs_manager import prepare_graphs, prepare_menu

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(prepare_sheet())
        
        self.menu = QMenu(self)

        # define utilities here
        self.board_manager = BoardManager()
        self.board_manager.on_rfcomm_started.connect(self.on_rfcomm_started)
        self.board_manager.on_rfcomm_finished.connect(self.on_rfcomm_finished)

        self.ui.boardBtn.clicked.connect(self.board_manager.show_board_manager)
        self.channels = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        self.ui.graphLayout.setSpacing(12)
        self.ui.graphLayout.setContentsMargins(QMargins(12, 12, 12, 12))


    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())

    """
    RF COMM CALLBACKS
    """
    def on_rfcomm_started(self):
        self.ui.statusVal.setText("CONNECTED")
        self.board_manager.serial_port.open(QIODeviceBase.OpenModeFlag.ReadOnly)

    def on_rfcomm_finished(self, code: int):
        self.ui.statusVal.setText("DISCONNECTED")
        if code != 0:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Connection Error")
            msgBox.setText("RFCOMM process exited with non 0 exit code.")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Close)
            msgBox.show()
            msgBox.exec()

    def read_serial_data(self):
        while self.board_manager.serial_port.canReadLine():
            self.process_data(self.board_manager.serial_port.readLine().data.decode('utf-8').strip())            

app = QApplication()
app_win = AppWindow()
app_win.show()
app.exec()
