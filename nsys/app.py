# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtGui import QAction
from theme_engine import prepare_sheet
from PySide6.QtCore import QMargins, Qt, QProcess, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox

import numpy as np
import pyqtgraph as pg

from board_manager import BoardManager
from recorder.rec_service import RecorderService
from graphs_manager import prepare_graphs, prepare_menu
from connection_manager import RFCommProcess, DataReader


"""
Rethinking the board connection flow.

Earlier a device address was required
but now it's not

but considering i will have a standalone board which does not know where to connect 
"""

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
        self.recorder = RecorderService()
        self.data_reader = DataReader(self.recorder)

        self.buffer = np.array([])
        
        self.channels, self.curves = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        """
        Connect to signals here
        """
        self.ui.boardBtn.clicked.connect(self.board_manager.show_board_manager)
        self.board_manager.device_selected.connect(self.on_device_selected)
        self.ui.toggleDataBtn.clicked.connect(self.on_start_clicked)
        self.ui.recordBtn.clicked.connect(self.recorder.toggleRecording)

        self.conn_manager.new_connection.connect(self.on_rfcomm_started)
        self.conn_manager.com_finished.connect(self.on_rfcomm_finished)

        self.data_reader.update.connect(self.update_graphs)
        
        self.conn_manager.start_process()

        self.recorder.update_time.connect(self.update_recorder_time)


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
        count = 0
        items = []

        for i in range(self.ui.deviceSelectionBox.count()):
            items.append(self.ui.deviceSelectionBox.itemText(i))

        if device_addr not in items:
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
    def update_graphs(self, cha: np.ndarray, chb: np.ndarray, chc: np.ndarray):
        self.curves["channel_1"].setData(cha)
        self.curves["channel_2"].setData(chb)
        self.curves["channel_3"].setData(chc)


    def update_recorder_time(self, time: str):
        self.ui.recordingTime.setText(time)

    def update_latency(self, latency: int):
        self.ui.latencyVal.setText(f"{str(latency)} sec")

    
    def closeEvent(self, event):
        print("Exiting")
        self.conn_manager.cleanup()
        event.accept()
        

app = QApplication()
app_win = AppWindow()
app_win.show()
app.exec()
