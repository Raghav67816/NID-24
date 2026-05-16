import numpy as np

from os import getcwd
from pathlib import Path

from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel


"""
the base software provides important and basic features.
users can add more feature by specifying name and compute function.
"""

def prepare_features_box(refs: dict, features_box: QTabWidget):

    # load default features
    with open(Path(f"{getcwd()}/config/default_features.txt"), "r") as f_file:
        features = f_file.readlines()
        f_file.close()

    for feature in features:
        feature = feature.replace("\n", "")
        add_feature(refs, features_box, feature, lambda x: print("hi"))

def add_feature(refs: dict, features_box: QTabWidget, name: str, comp_func: callable):
    if name != None and comp_func != None:

        count = features_box.count()

        for i in range(count):
            widget = features_box.widget(i)
            layout = widget.layout()

            if not layout:
                layout = QFormLayout(widget)

            feature_label = QLabel(f"{name}: ")
            val_label = QLabel("")

            obj_name = f"channel_{i + 1}_{name.lower()}"
            if obj_name in refs.keys():
                return

            val_label.setObjectName(f"channel_{i + 1}_{name}")
            layout.addRow(feature_label, val_label)


class FeaturesExtractor(QObject):
    def __init__(self):
        super(FeaturesExtractor, self).__init__()
        pass

