import numpy as np

from os import getcwd
from pathlib import Path

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel


class FeaturesExtractor(QObject):

    feature_added = Signal(dict)
    computed = Signal(dict)

    def __init__(self, featuresBox: QTabWidget):
        super(FeaturesExtractor, self).__init__()

        self.features_data = {}
        self.computed_values = {}
        self.featuresUiRefs = {}

        for i in range(featuresBox.count()):
            layout = QFormLayout()
            widget = featuresBox.widget(i)
            widget.setLayout(layout)

        with open(f"{getcwd()}/config/default_features.txt", "r") as features_file:
            for feature in features_file.readlines():
                self.add_feature(featuresBox, feature, None)
            features_file.close()

        self.set_function_to_feature("rms", self.rms)

    # set function to feature
    def set_function_to_feature(self, feature: str, compute_func: callable):
        if feature not in self.features_data.keys():
            return
        
        self.features_data[feature] = compute_func
        print(self.features_data[feature])

    def add_feature(self, featuresBox: QTabWidget, feature: str, compute_func: callable):
        if feature in self.features_data.keys():
            return
        
        self.features_data[feature.lower()] = compute_func
        self.add_feature_to_ui(featuresBox, feature)

    def add_feature_to_ui(self, featuresBox: QTabWidget, name: str):
        tab_count = featuresBox.count()

        # each tab must have a QFormLayout
        for i in range(tab_count):
            tab = featuresBox.widget(i)
            layout: QFormLayout = tab.layout()

            feature_label = QLabel(f"{name}: ")
            val_label = QLabel("-")

            layout.addRow(feature_label, val_label)
            self.featuresUiRefs[f"channel_{i + 1}_{name.lower()}"] = val_label

        self.feature_added.emit(self.featuresUiRefs)

    def compute_features(
        self,
        ch1: np.ndarray,
        ch2: np.ndarray,
        ch3: np.ndarray
    ):
        for feature in self.features_data.keys():
            out = self.features_data[feature](ch1, ch2, ch3)
            self.computed_values[feature] = round(out[0], 3)

        self.computed.emit(self.computed_values)

    def get_ui_refs(self):
        return self.featuresUiRefs

    def rms(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        rms_a = np.sqrt(np.mean(np.square(ch1)))
        # rms_b = np.sqrt(np.mean(np.square(ch2)))
        # rms_c = np.sqrt(np.mean(np.square(ch3)))

        return (rms_a, 0, 0)
