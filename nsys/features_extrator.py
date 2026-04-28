import numpy as np
from PySide6.QtCore import QThread, Signal


class FeaturesWorker(QThread):

    readyRead = Signal(dict)

    def __init__(self, features: list):
        super(FeaturesWorker, self).__init__()

        self.features = ["rms"]

    def calc_rms(self):
        pass

    def set_signal(self, signal: np.ndarray):
        pass
