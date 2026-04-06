from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal

class ComboBox(QComboBox):
    clicked = Signal()

    def __init__(self):
        super(ComboBox, self).__init__()
        pass

    def showPopup(self):
        print("clicked")
        self.clicked.emit()
        super().showPopup()
