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
            val_label = QLabel("-")

            obj_name = f"channel_{i + 1}_{name.lower()}"
            if obj_name in refs:
                return

            val_label.setObjectName(f"channel_{i + 1}_{name}_val")
            layout.addRow(feature_label, val_label)

            # refs[name] = val_label
            refs[name] = val_label

    return refs

class FeaturesExtractor(QObject):

    computed = Signal(dict)

    def __init__(self, featuresBox: QTabWidget):
        super(FeaturesExtractor, self).__init__()
        
        # key: feature_name, compute function
        self.functions = {}
        self.data = {}

        with open(f"{getcwd()}/config/default_features.txt", "r") as features_file:
            features = features_file.readlines()
            features_file.close()

        for feature in features:
            self.functions[feature.lower()] = None

        self.add_feature("RMS", self.rms)

    def get_features(self):
        return self.functions.keys()

    def add_feature(self, name: str, compute_func: callable):
        name = name.lower()
        if name in self.functions.keys() and self.functions[name] != None:
            return # if feature exists but compute function is not specified
        
        self.functions[name] = compute_func
        if compute_func == None:
            print("Warning: Compute function is not defined. Feature will not be calculated")


    def compute_all(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        for feature in self.functions.keys():
            if self.functions[feature]:
                self.data[feature] = self.functions[feature](ch1, ch2, ch3)

        print(self.data)
        self.computed.emit(self.data)

    
    # default functions below
    def rms(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        rms_a = np.sqrt(np.mean(np.square(ch1)))
        rms_b = np.sqrt(np.mean(np.square(ch2)))
        rms_c = np.sqrt(np.mean(np.square(ch3)))

        return [rms_a, rms_b, rms_c]
