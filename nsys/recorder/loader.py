from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QFileDialog, QMainWindow


# might get removed
class DataLoader(QObject):
    
    selected = Signal(str) # send file path to line edit
    
    def request_loader(self, parent: QMainWindow):
        url = QFileDialog.getOpenFileName(
            parent,
            "Select Data Directory",
            "~/",
            options=QFileDialog.Option.ShowDirsOnly
        )
        
        if url != "":
            self.selected.emit(url.toString())
        
