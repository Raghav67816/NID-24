from PySide6.QtCore import Signal
from PySide6.QtWidgets import QComboBox, QLineEdit, QWidget

def swap_widgets(old: QWidget, new: QWidget):
    layout = old.parentWidget().layout()
    layout.replaceWidget(old, new)
    
    old.deleteLater()

class Mod_ComboBox(QComboBox):
    clicked = Signal()

    def __init__(self):
        super(Mod_ComboBox, self).__init__()
        pass

    def showPopup(self):
        print("clicked")
        self.clicked.emit()
        super().showPopup()
        

class Mod_LineEdit(QLineEdit):
    clicked = Signal()
    
    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)
