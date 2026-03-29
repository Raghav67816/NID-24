import sys
import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

class RealTimePlotting(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtGraph Real-Time Plotting with PySide6")
        self.setGeometry(100, 100, 800, 600)

        # Create a PlotWidget and set it as the central widget
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Configure the plot
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("Real-Time Sine Wave", color="b", size="20pt")
        styles = {"color": "#f00", "font-size": "15px"}
        self.plot_widget.setLabel("left", "Amplitude", **styles)
        self.plot_widget.setLabel("bottom", "Time (s)", **styles)
        self.plot_widget.addLegend()
        self.plot_widget.setYRange(-1.1, 1.1) # Optional: set a fixed Y range for performance

        # Create a plot data item
        self.curve = self.plot_widget.plot(pen=pg.mkPen(color=(255, 0, 0), width=2), name="Sine Wave")

        # Data variables
        self.data_x = []
        self.data_y = []
        self.data_len = 100 # Display last 100 points
        self.i = 0

        # Set up a QTimer to update the plot
        self.timer = QTimer()
        self.timer.setInterval(50)  # Update every 50ms (20 fps)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        # Generate new data point
        new_y = np.sin(self.i * 0.1)
        self.i += 1

        # Append new data
        self.data_x.append(self.i)
        self.data_y.append(new_y)

        # Keep only the last 100 points for a "rolling" plot
        if len(self.data_x) > self.data_len:
            self.data_x = self.data_x[-self.data_len:]
            self.data_y = self.data_y[-self.data_len:]

        # Update the plot with new data
        self.curve.setData(self.data_x, self.data_y)

def main():
    app = QApplication(sys.argv)
    window = RealTimePlotting()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
