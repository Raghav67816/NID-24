"""
record incoming data for later analysis
"""
import numpy as np
from os import getcwd
from PySide6.QtCore import Signal, QObject, QTimer

from datetime import datetime

"""

DESIGN RULE

to maintaince consistency in system design both recorder and generator:
1. MUST store data in the following format

    PARENT ARRAY
    [
        [x1, x2, x3, x4 ...... xn] -> channel 1
        [y1, y2, y3, y4 ...... yn] -> channel 2
        [z1, z2, z3, z4 ...... zn] -> channel 3
    ]

2. Instead of generating data in chunk, write data in chunk.
"""

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
            # np.savetxt(
            #     f"{self.default_dump_location}/recorder/{self.file_index}.csv",
            #     combined_buffer,
            #     delimiter=",",
            #     fmt='%.6f'
            # )
            np.save(f"{self.default_dump_location}/recorder/{self.file_index}.npy", combined_buffer)
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

