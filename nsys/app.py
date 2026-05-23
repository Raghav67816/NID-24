# import dependencies
from ui.app import Ui_AppWindow

from PySide6.QtCore import QMargins, Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox

import numpy as np

from pyqtgraph import PlotWidget

from settings import SettingsApp, Settings
from features_extractor import FeaturesExtractor

from recorder.loader import request_loader
from recorder.rec_service import RecorderService
from connection_manager import DataReader, RFCommProcess
from graphs_manager import prepare_graphs, prepare_menu, attach_lrt, confirm_regions

from utils.theme_engine import ThemeEngine
from utils.custom_widgets import Mod_LineEdit, swap_widgets, DataControlsWidget


class AppWindow(QMainWindow):

    app_exit = Signal()

    def __init__(self):
        super(AppWindow, self).__init__()
        
        self.theme_engine = ThemeEngine()

        """
        Setup Ui here
        """
        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(self.theme_engine.prepare_sheet())

        self.ui.graphLayout.setSpacing(12)
        self.ui.graphLayout.setContentsMargins(QMargins(12, 12, 12, 12))

        self.ui.actionTogglePoints.setCheckable(True)

        self.lrt_ref = {
            "channel_1": None,
            "channel_2": None,
            "channel_3": None
        }

        """
        Define all utilities here.
        """
        self.menu = QMenu(self)
        self.settings = Settings()
        self.recorder = RecorderService()
        self.features_extractor = FeaturesExtractor(self.ui.featuresTabWidget)
        self.data_reader = DataReader(
            self,
            self.recorder,
            self.settings,
            self.features_extractor
        )

        self.comm_process = RFCommProcess(self)
        self.normal_mode = True

        self.featureUiRefs = self.features_extractor.get_ui_refs()
        
        self.channels, self.curves = prepare_graphs(self.ui.graphLayout)
        prepare_menu(self, self.channels, self.menu)

        self.settings.load_config()

        self.loadFromDir = Mod_LineEdit()
        self.loadFromDir.setPlaceholderText("Load from directory...")
        
        swap_widgets(self.ui.loadFilePathEdit, self.loadFromDir)  

        """
        Connect to signals here
        """
        self.ui.toggleDataBtn.clicked.connect(self.on_start_clicked)
        self.ui.recordBtn.clicked.connect(self.recorder.toggleRecording)
        self.ui.modeToggleBtn.clicked.connect(self.change_application_mode)
        
        self.data_reader.update.connect(self.update_graphs)
        self.data_reader.connected.connect(self.update_status)
        self.data_reader.write_latency.connect(self.update_latency)

        self.ui.settingsBtn.clicked.connect(self.open_settings)

        self.recorder.update_time.connect(self.update_recorder_time)

        self.loadFromDir.clicked.connect(self.load_data_from_file)

        self.features_extractor.feature_added.connect(self.on_new_feature_added)
        self.features_extractor.computed.connect(self.update_feature_vals)

        for curve in self.curves.keys():
            self.curves[curve].sigPointsClicked.connect(
                lambda points, item, event, curve=curve: self.on_points_clicked(
                    points,
                    self.channels[curve]
                )
            )

        self.comm_process.start_process()


        """
        connect to actions here
        """
        self.ui.actionTogglePoints.setParent(self)
        self.addAction(self.ui.actionTogglePoints)
        self.ui.actionTogglePoints.toggled.connect(self.toggle_points)

        self.ui.actionConfirm_Regions.setParent(self)
        self.addAction(self.ui.actionConfirm_Regions)
        self.ui.actionConfirm_Regions.triggered.connect(self.on_confirm_regions)


    # override default context menu
    def contextMenuEvent(self, event):
        self.menu.exec(event.globalPos())

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
                    background-color: _color_
                }
                """.replace("_color_", self.theme_engine.get_color("danger-color"))
            )
            
        if btn_text == "stop":
            self.data_reader.isReading = False
            self.ui.toggleDataBtn.setText("Start")
            self.ui.toggleDataBtn.setStyleSheet(
                """
                QPushButton{
                    color: white;
                    background-color: _color_
                }
                """.replace("_color_", self.theme_engine.get_color("primary-color"))
            )


    """
    update the graph when data is received
    """
    def update_graphs(self, cha: np.ndarray, chb: np.ndarray, chc: np.ndarray):
        self.curves["channel_1"].setData(cha)
        self.curves["channel_2"].setData(chb)
        self.curves["channel_3"].setData(chc)


    def update_recorder_time(self, time: str):
        self.ui.recordingTime.setText(time)

    def update_latency(self, latency: float):
        self.ui.latencyVal.setText(f"{str(latency)} ms")

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

    def load_data_from_file(self):
        url = request_loader(self)
        if url != "":
            self.loadFromDir.setText(url)

            if self.normal_mode:
                self.change_application_mode()

            self.data_reader = DataReader(
                self,
                self.recorder,
                self.settings.settings_obj,
                self.features_extractor
            )

    def on_new_feature_added(self, refs: dict):
        self.featureUiRefs = refs

    def update_feature_vals(self, computed_vals: dict):
        for feature in computed_vals.keys():
            feature_out = computed_vals[feature]
            for i in range(len(feature_out)):
                round_ = round(feature_out[i], 3)
                self.featureUiRefs[f"channel_{i + 1}_{feature}"].setText(str(round_))

    
    def on_points_clicked(self, points: list, channel: PlotWidget):
        attach_lrt(channel, self.lrt_ref, self.channels)

    def toggle_points(self, checked: bool):
        if checked:
            for curve in self.curves.values():
                curve.setSymbol(None)

        else:
            for curve in self.curves.values():
                curve.setSymbol("o")

    def on_confirm_regions(self):
        confirm_regions(self.lrt_ref, self.channels)

    
    def open_settings(self):
        settings_app = SettingsApp(
            self.settings,
            self.theme_engine
        )

        settings_app.show()
        settings_app.exec()
    
    def closeEvent(self, event):
        self.app_exit.emit()
        event.accept()
        

app = QApplication()

app_win = AppWindow()
app_win.show()
app.exec()
