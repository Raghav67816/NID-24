import sys
import random
from PySide6 import QtWidgets, QtCore # Use PySide6 imports
import pyqtgraph as pg
import numpy as np

class RealTimePlotWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 PyQtGraph Real-Time Plotting")

        # Create a PlotWidget and set it as the central widget
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)
        self.plot_widget.setBackground('w') # Set background to white
        self.plot_widget.setTitle("Real-Time Data Stream")
        self.plot_widget.setXRange(0, 100) # Set a fixed X range for rolling plot

        # Create a plot data item (curve)
        self.curve = self.plot_widget.plot(pen=pg.mkPen(color=(255, 0, 0), width=2))
        
        # Initialize data arrays
        self.data_x = np.arange(100)
        self.data_y = np.zeros(100, dtype=float) # Start with zeros

        # Set up a QTimer to update the plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50) # Update every 50ms (20 Hz)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Shift data to the left by one sample (rolling plot effect)
        self.data_y[:-1] = self.data_y[1:]
        # Add new random data point to the end
        self.data_y[-1] = random.uniform(0, 100) 
        
        # Update the plot with the new data
        self.curve.setData(self.data_x, self.data_y)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RealTimePlotWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
