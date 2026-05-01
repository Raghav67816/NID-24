# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtGui import QIcon
from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox, QListWidgetItem

from platform import platform
import numpy as np

from settings import SettingsApp, Settings
from features_extrator import prepare_features_box

from recorder.loader import DataLoader
from recorder.rec_service import RecorderService
from graphs_manager import prepare_graphs, prepare_menu
from connection_manager import RFCommProcess, DataReader

from utils.theme_engine import ThemeEngine
from utils.custom_widgets import Mod_LineEdit, swap_widgets, DataControlsWidget


"""
Rethinking the board connection flow.

Earlier a device address was required
but now it's not

but considering i will have a standalone board which does not know where to connect 
"""

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        
        self.theme_engine = ThemeEngine()
        self.platform = None

        """
        Setup Ui here
        """
        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(self.theme_engine.prepare_sheet())

        self.ui.graphLayout.setSpacing(12)
        self.ui.graphLayout.setContentsMargins(QMargins(12, 12, 12, 12))

        """
        Define all utilities here.
        """
        self.menu = QMenu(self)
        self.settings = Settings()
        self.recorder = RecorderService()
        self.data_loader = DataLoader()
        self.data_reader = DataReader(self.recorder)

        self.conn_manager = None
        if self.platform != "win":
            self.conn_manager = RFCommProcess(self)
            self.conn_manager.start_process()

        self.normal_mode = True
        
        self.channels, self.curves = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        # load config before access config
        self.settings.load_config()
        print("dumping config")
        print(self.settings.config)

        prepare_features_box(self.ui.featuresTabWidget)

        if platform().lower().startswith("win"):
            self.platform = "win"
            self.settings.settings_obj.setValue("platform", "win")

        else:
            self.platform = "linux"
            self.settings.settings_obj.setValue("platform", "linux")

        # check platform 
        # change the device selection combo box to custom line edit
        self.loadFromDir = Mod_LineEdit()
        self.loadFromDir.setPlaceholderText("Load from directory...")
        self.loadFromDir.clicked.connect(self.on_load_from_dir_clicked)
        
        swap_widgets(self.ui.loadFilePathEdit, self.loadFromDir)
        

        """
        Connect to signals here
        """
        self.ui.toggleDataBtn.clicked.connect(self.on_start_clicked)
        self.ui.recordBtn.clicked.connect(
            lambda state, btn=self.ui.recordBtn: self.recorder.toggleRecording(btn)
        )
        self.ui.modeToggleBtn.clicked.connect(self.change_application_mode)
        
        self.data_reader.update.connect(self.update_graphs)
        self.data_reader.connected.connect(self.update_status)

        self.ui.settingsBtn.clicked.connect(self.open_settings)

        self.recorder.update_time.connect(self.update_recorder_time)

    # override default context menu
    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())


    def on_load_from_dir_clicked(self):
        self.data_loader.request_loader(self)

    """
    start simulating data
    first checks if port is already bounded or not.
    """
    def on_start_clicked(self):
        btn_text = self.ui.toggleDataBtn.text().lower()
        
        if btn_text == "start":
            
            # if port is not opened when start is pressed 
            # open the port, if the port is opened connected will be emitted
            # and we can change the text
            if not self.data_reader.isOpen:
                self.data_reader.open_port()
            
            self.data_reader.isReading = True
            self.ui.toggleDataBtn.setText("Stop")
            self.ui.toggleDataBtn.setStyleSheet(
                """
                QPushButton{
                    color: white;
                    background-color: {0}
                }
                """.format(self.theme_engine.get_color("danger-color"))
            )
            
        if btn_text == "stop":
            self.data_reader.isReading = False
            self.ui.toggleDataBtn.setText("Start")
            self.ui.toggleDataBtn.setStyleSheet(
                """
                QPushButton{
                    color: white;
                    background-color: {0}
                }
                """.format(self.theme_engine.get_color("primary-color"))
            )

    def toggleRecorder(self):
        self.recorder.toggleRecording()
        self.ui.recordBtn.setIcon(QIcon(""))


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

    def update_status(self, isConnected: bool):
        def set_color(text: str, color: str):
            return f"<p style='color: {color}'>{text}</p>"
    
        if isConnected:
            self.ui.statusVal.setTextFormat(Qt.TextFormat.RichText)
            self.ui.statusVal.setText(
                set_color("Connected", "green")
            )
            

        else:
            self.ui.statusVal.setTextFormat(Qt.TextFormat.RichText)
            self.ui.statusVal.setText(
                set_color("Disconnected", "red")
            )

    def change_mode(self, mode: str):
        if mode.lower() == "obs":
            controls_widget = DataControlsWidget()
            swap_widgets(self.ui.toggleDataBtn, controls_widget)

    def change_application_mode(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Application Mode Change")
        msg_box.setText("Changing Application Mode Will Reset Your Current State")
        msg_box.setStandardButtons(
            QMessageBox.StandardButtons.Ok |
            QMessageBox.StandardButtons.Cancel
        )
        msg_box.show()
        ret = msg_box.exec()

        if ret == QMessageBox.StandardButtons.Ok:
            if self.normal_mode:
                self.ui.modeToggleBtn.setText("OBS")
                self.ui.modeToggleBtn.setStyleSheet("QToolButton{ color: orange; font-weight: bold  }")
                self.normal_mode = False

                self.change_mode(self.ui.modeToggleBtn.text())

            elif self.normal_mode != True:
                self.ui.modeToggleBtn.setText("NOR")
                self.ui.modeToggleBtn.setStyleSheet("QToolButton{ color: green; font-weight: bold  }")
                self.normal_mode = True

        else:
            pass

    
    def open_settings(self):
        settings_app = SettingsApp(
            self.settings,
            self.theme_engine
        )

        settings_app.show()
        settings_app.exec()
    
    def closeEvent(self, event):
        print("Exiting")

        if self.platform != "win":
            self.conn_manager.cleanup()

        event.accept()
        

app = QApplication()

app_win = AppWindow()
app_win.show()
app.exec()
