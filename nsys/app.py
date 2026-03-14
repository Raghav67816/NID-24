# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtCore import QMargins, Qt
from PySide6.QtGui import QAction
from theme_engine import prepare_sheet 
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu

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

        self.ui.boardBtn.clicked.connect(self.board_manager.show_board_manager)
        self.channels = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        self.ui.graphLayout.setSpacing(12)
        self.ui.graphLayout.setContentsMargins(QMargins(12, 12, 12, 12))


    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())

app = QApplication()
app_win = AppWindow()
app_win.show()
app.exec()
