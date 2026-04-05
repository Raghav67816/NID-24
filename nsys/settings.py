from os import getcwd

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSettings, QObject


class Settings(QObject):
    def __init__(self):
        super(Settings, self).__init__()

        self.cwd = getcwd()
        self.default_location = f"{self.cwd}/config/settings.ini"

        self.settings_obj = QSettings("NID-24", "Raghav67816")

class SettingsApp(QMainWindow):
    pass
