from PySide6.QtWidgets import QFileDialog, QMainWindow


def request_loader(parent: QMainWindow):
    url = QFileDialog.getOpenFileName(
        parent,
        "Select Data File",
        "~/"
    )
    return url[0]
