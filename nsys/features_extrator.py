import numpy as np

from os import getcwd
from pathlib import Path

from functools import wraps

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel

def prepare_features_box(features_box: QTabWidget):

    with open(Path(f"{getcwd()}/config/features.txt"), "r") as f_file:
        features = f_file.readlines()
        f_file.close()

        num_tabs = features_box.count()
        refs = {}

        for i in range(num_tabs):

            widget = features_box.widget(i)
            layout = QFormLayout(widget)

            for feature in features:
                feature = feature.replace("\n", "")
                label = QLabel(f"{feature}: ")
                label_val = QLabel("-")
                label_val.setObjectName(f"channel_{i+1}_{feature}")
                
                layout.addRow(label, label_val)

                refs[label_val.objectName] = label_val


class FeatureExtractor(QObject):
    readyRead = Signal(dict) # new feature values are calculate

    def __init__(self):
        super(FeatureExtractor, self).__init__(self)

        self.refs = {}
        self.features = []

        with open(Path(f"{getcwd()}/config/features.txt"), "r") as f_file:
            self.features = f_file.readline()
            for feature in self.features:
                feature = feature.replace("\n", "")

            f_file.close()


    def write_data(
            self,
            ch1: np.ndarray,
            ch2: np.ndarray,
            ch3: np.ndarray
    ):
        data = {}
        for feature in self.refs.keys():
            data[str(feature)] = self.refs[feature]([
                ch1,
                ch2,
                ch3
            ])

        self.readyRead.emit(data)
