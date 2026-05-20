import numpy as np

from os import getcwd
from pathlib import Path

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel

"""
NOTE: Right now we are doing only feature extraction for 
channel 1
"""


class FeaturesExtractor(QObject):

    feature_added = Signal(dict)
    computed = Signal(dict)

    def __init__(self, featuresBox: QTabWidget):
        super(FeaturesExtractor, self).__init__()

        self.features_data = {}
        self.computed_values = {}
        self.featuresUiRefs = {}
        self.active_channel = 0

        featuresBox.currentChanged.connect(self.set_active_channel)

        for i in range(featuresBox.count()):
            layout = QFormLayout()
            widget = featuresBox.widget(i)
            widget.setLayout(layout)

        with open(f"{getcwd()}/config/default_features.txt", "r") as features_file:
            for feature in features_file.readlines():
                self.add_feature(featuresBox, feature, None)
            features_file.close()

        self.set_function_to_feature("rms", self.rms)
        self.set_function_to_feature("mea", self.mea)
        self.set_function_to_feature("variance", self.variance)
        self.set_function_to_feature("waveform_length", self.waveform_length)
        self.set_function_to_feature("difference_abs_mean_value", self.diff_abs_mean_value)

    # set function to feature
    def set_function_to_feature(self, feature: str, compute_func: callable):
        if feature not in self.features_data.keys():
            return
        
        self.features_data[feature] = compute_func

    def add_feature(self, featuresBox: QTabWidget, feature: str, compute_func: callable):
        feature = feature.replace("\n", "")
        
        if feature in self.features_data.keys():
            return
        
        self.features_data[feature.lower().replace(" ", "_")] = compute_func
        self.add_feature_to_ui(featuresBox, feature)

    def add_feature_to_ui(self, featuresBox: QTabWidget, name: str):
        tab_count = featuresBox.count()

        # each tab must have a QFormLayout
        for i in range(tab_count):
            tab = featuresBox.widget(i)
            layout: QFormLayout = tab.layout()

            feature_label = QLabel(f"{name}: ")
            val_label = QLabel("-")

            val_label.setStyleSheet("font-weight: bold")

            layout.addRow(feature_label, val_label)
            self.featuresUiRefs[f"channel_{i + 1}_{name.lower().replace(" ", "_")}"] = val_label

        self.feature_added.emit(self.featuresUiRefs)

    def compute_features(
        self,
        ch1: np.ndarray,
        ch2: np.ndarray,
        ch3: np.ndarray
    ):
        for feature in self.features_data.keys():
            out = self.features_data[feature](ch1, ch2, ch3)
            self.computed_values[feature] = out
            self.computed.emit(self.computed_values)
            return self.computed_values

    def get_ui_refs(self):
        return self.featuresUiRefs
    
    def set_active_channel(self, index: int):
        self.active_channel = index

    def rms(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        rms_a = np.sqrt(np.mean(np.square(ch1)))
        rms_b = np.sqrt(np.mean(np.square(ch2)))
        rms_c = np.sqrt(np.mean(np.square(ch3)))

        return (rms_a, rms_b, rms_c)
    
    def mea(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        mea_a = np.abs(np.mean(ch1))
        mea_b = np.abs(np.mean(ch2))
        mea_c = np.abs(np.mean(ch3))

        return (mea_a, mea_b, mea_c)
    
    def variance(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        var_a = np.var(ch1)
        var_b = np.var(ch2)
        var_c = np.var(ch3)

        return (var_a, var_b, var_c)
    

    def waveform_length(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        wl_a = np.sum(np.abs(np.diff(ch1)))
        wl_b = np.sum(np.abs(np.diff(ch2)))
        wl_c = np.sum(np.abs(np.diff(ch3)))

        out = (wl_a, wl_b, wl_c)
        return out
    

    # TODO: Change calculation of mv_b, and mv_c
    def diff_abs_mean_value(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        wlength = self.computed_values['waveform_length']
        mv_a = (1/(len(ch1) - 1))*wlength[0]
        mv_b = (1/(len(ch2) - 1))*wlength[1]
        mv_c = (1/(len(ch3) - 1))*wlength[2]

        return (mv_a, mv_b, mv_c)
    
    def sec_order_moment(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        wlength = self.compute_features['waveform_length']
        som_a = np.sum(np.square(wlength))
        # som_b = np.sum(np.square(wlength))
        # som_c = np.sum(np.square(wlength))

        # TODO: Second Order Moment depends on wlength, currently we only have wlength of 1st channel

        return (som_a, 0, 0)
    