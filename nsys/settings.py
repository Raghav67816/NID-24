from os import getcwd
from pathlib import Path

import serial

from PySide6.QtCore import QSettings, QObject, QSize, Signal
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QLineEdit, QComboBox

from ui.settings_ui import Ui_SettingsWindow
from utils.theme_engine import ThemeEngine

from utils.custom_widgets import swap_widgets, Mod_LineEdit, Mod_ComboBox


class Settings(QObject):
    def __init__(self):
        super(Settings, self).__init__()

        self.cwd = getcwd()
        self.default_location = Path(f"{self.cwd}/config/settings.ini")

        self.settings_obj = QSettings("NID-24", "Raghav67816")

        # default config
        # fallback to this if loading config fails or isn't set yet
        self.config = {
            "updateInterval": 60,
            "theme": "default",
            "saveDataFilePath": "~/home/nid-data",
            "maxPacketLen": 10^6
        }

        self.valid_keys = [
            "updateInterval",
            "theme",
            "saveDataFilePath",
            "maxPacketLen"
        ]
    
    def load_config(self):
        for valid_key in self.valid_keys:
            val = self.settings_obj.value(valid_key)
            if val is not None:
                self.config[valid_key] = val

class SettingsApp(QMainWindow):

    settings_updated = Signal()

    def __init__(self, settings_obj: QObject, theme_engine: ThemeEngine):
        super(SettingsApp, self).__init__()

        self.ui = Ui_SettingsWindow()
        self.settings_obj = settings_obj
        self.theme_engine = theme_engine

        self.ui.setupUi(self)

        self.ui.applyBtn.clicked.connect(self.on_apply_clicked)
        self.ui.discardBtn.clicked.connect(self.on_discard_clicked)

        self.setStyleSheet(self.theme_engine.prepare_sheet())
        self.setMaximumSize(QSize(400, 600))

        self.ui.saveDataPath.setText(
            str(self.settings_obj.config['saveDataFilePath'])
        )
        self.ui.updateInterval.setText(
            str(self.settings_obj.config['updateInterval'])
        )

        self.portBox = Mod_ComboBox()
        self.portBox.setPlaceholderText("--Select Serial Port--")
        self.portBox.setEditable(False)
        self.portBox.clicked.connect(self.on_portbox_clicked)
        
        swap_widgets(self.ui.serialPortBox, self.portBox)

        self.saveDataPath = Mod_LineEdit()
        self.saveDataPath.setText(str(self.settings_obj.config['saveDataFilePath']))

        swap_widgets(self.ui.saveDataPath, self.saveDataPath)

    
    def on_apply_clicked(self):
        input_widgets = [
            self.ui.theme,
            self.ui.updateInterval,
            self.saveDataPath
        ]

        for widget in input_widgets:
            if type(widget) == Mod_LineEdit or type(widget) == QLineEdit:
                self.settings_obj.settings_obj.setValue(widget.objectName(), str(widget.text()))

            elif type(widget) == QComboBox:
                self.settings_obj.settings_obj.setValue(widget.objectName(), str(widget.currentText()))

        self.close()


    def on_discard_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Your changes will be discarded.")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        msg.show()
        ret = msg.exec()

        if ret == QMessageBox.StandardButton.Cancel:
            msg.close()
        
        elif ret == QMessageBox.StandardButton.Ok:
            msg.close()
            self.close()

    def on_save_path_clicked(self):  
        url = QFileDialog.getExistingDirectoryUrl(
            self,
            "Select Data Directory",
            "~/",
            options=QFileDialog.Option.ShowDirsOnly
        )
                
        if url != "":
            self.saveDataPath.setText(url)

    
    def on_portbox_clicked(self):
        ports = serial.tools.list_ports.comports()
        self.portBox.clear()
        for port in ports:
            self.portBox.addItem(str(port))    
