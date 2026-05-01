from ui.dataControlWidget_ui import Ui_dataControlWidget

from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QComboBox, QLineEdit, QWidget

def swap_widgets(old: QWidget, new: QWidget):
    layout = old.parentWidget().layout()
    layout.replaceWidget(old, new)
    
    old.deleteLater()

class Mod_ComboBox(QComboBox):
    clicked = Signal()

    def __init__(self, theme: str = None):
        super(Mod_ComboBox, self).__init__()
        
        if theme:
            self.setStyleSheet(theme)

    def showPopup(self):
        print("clicked")
        self.clicked.emit()
        super().showPopup()
        

class Mod_LineEdit(QLineEdit):
    clicked = Signal()
    
    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)
    

class DataControlsWidget(QWidget):

    toggled = Signal(bool)
    previous = Signal()
    forward = Signal()

    def __init__(self):
        super(DataControlsWidget, self).__init__()

        self.ui = Ui_dataControlWidget()
        self.ui.setupUi(self)


        # true for playing
        # false for paused
        self.state = True

        self.ui.toggleBtn.clicked.connect(self.on_toggled)
        self.ui.prevBtn.clicked.connect(self.previous.emit)
        self.ui.forwardBtn.clicked.connect(self.forward.emit)


    def on_toggled(self):
        if self.state:
            self.state = not self.state
            self.ui.toggleBtn.setIcon(QIcon(":/icons/icons8-pause-32.png"))
        else:

            self.state = not self.state
            self.ui.toggleBtn.setIcon(QIcon(":/icons/icons8-play-30.png"))
        self.toggled.emit(self.state)
