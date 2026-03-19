# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtGui import QAction
from theme_engine import prepare_sheet 
from PySide6.QtCore import QMargins, Qt, QProcess, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox

import numpy as np
import pyqtgraph as pg
from collections import deque

from board_manager import BoardManager
from graphs_manager import prepare_graphs, prepare_menu
from connection_manager import RFCommProcess, DataReader

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        """
        Setup Ui here
        """
        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(prepare_sheet())

        self.ui.graphLayout.setSpacing(12)
        self.ui.graphLayout.setContentsMargins(QMargins(12, 12, 12, 12))

        """
        Define all utilities here.
        """
        self.menu = QMenu(self)
        self.conn_manager = RFCommProcess(self)
        self.board_manager = BoardManager()
        self.data_reader = DataReader()

        self.buffer = deque(maxlen=500)
        
        self.channels = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        """
        Connect to signals here
        """
        self.ui.boardBtn.clicked.connect(self.board_manager.show_board_manager)
        self.board_manager.device_selected.connect(self.on_device_selected)
        self.ui.toggleDataBtn.clicked.connect(self.on_start_clicked)

        self.conn_manager.new_connection.connect(self.on_rfcomm_started)
        self.conn_manager.com_finished.connect(self.on_rfcomm_finished)

        self.conn_manager.start_process()        

        self.data_reader.data_ready.connect(self.update_graphs)

    # override default context menu
    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())

    """
    RF COMM CALLBACKS
    """
    def on_rfcomm_started(self):
        self.ui.statusVal.setText("CONNECTED")

    def on_rfcomm_finished(self, code: int, desc: str):
        self.ui.statusVal.setText("DISCONNECTED")

    """
    once user selected target board from Board Manager dialog
    add it to data sources list
    """
    def on_device_selected(self, device_addr: str):
        self.ui.deviceSelectionBox.insertItem(0, device_addr)


    """
    start simulating data
    first checks if port is already bounded or not.
    """
    def on_start_clicked(self):
        btn_text = self.ui.toggleDataBtn.text().lower()

        if btn_text == "start":
            if not self.data_reader.isOpen:
                self.data_reader.open_port()
                
            self.data_reader.isReading = True
            self.ui.toggleDataBtn.setText("Stop")

        elif btn_text == "stop":
            self.data_reader.isReading = False
            self.ui.toggleDataBtn.setText("Start")


    """
    update the graph when data is received
    """
    def update_graphs(self, data: np.ndarray):
        for channel in self.channels.keys():
            self.channels[channel].clear()
            self.channels[channel].plot().setData(data)

    """
    the new problem:
    HIGH CPU USAGE
    and it was obvious 

    solution:
        the buffer fills up every second with 200 samples
        trim the buffer, take last 100 i.e latest 100 sample and plot them         
    """
    
    def closeEvent(self, event):
        print("Exiting")
        self.conn_manager.cleanup()
        event.accept()
        

app = QApplication()
app_win = AppWindow()
app_win.show()
app.exec()
