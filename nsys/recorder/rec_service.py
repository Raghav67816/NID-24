"""
record incoming data for later analysis
"""
import numpy as np
from os import getcwd
from PySide6.QtCore import Signal, QObject, QTimer

from datetime import datetime

class RecorderService(QObject):

    started = Signal()
    paused = Signal()
    update_time = Signal(str)

    def __init__(self):
        super(RecorderService, self).__init__()

        self.buff_limit = 64 # MB
        self.default_dump_location = f"{getcwd()}"

        self.file_index = 0

        self.isRunning = False

        self.time = "00:00" # MM:SS format

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start()

    def on_buff_full(self, ch1: np.ndarray, ch2: np.ndarray, ch3: np.ndarray):
        if self.isRunning:
            combined_buffer = np.array([ch1, ch2, ch3])
            np.savetxt(
                f"{self.default_dump_location}/recorder/{self.file_index}.csv",
                combined_buffer,
                delimiter=",",
                fmt='%.6f'
            )
            self.file_index += 1

    def on_timeout(self):
        if self.isRunning:
            time = datetime.strptime(self.time, "%M:%S")
            new_ss = time.second + 1
            new_mm = time.minute

            if new_ss >= 59:
                new_mm += 1
                new_ss = 0

            self.time = f"{new_mm}:{new_ss}"

            self.update_time.emit(self.time)

    def toggleRecording(self):
        if not self.isRunning:
            self.isRunning = True
            self.started.emit()

        else:
            self.isRunning = False
            self.paused.emit()

    def load_caset(self, caset_path: str):
        pass

