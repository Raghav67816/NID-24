"""
manages functions related to graphs
1. preparing graphs and objects
2. merging them
3. menu related functions
"""

import pyqtgraph as pg
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLayout, QMenu

def prepare_graphs(layout: QLayout) -> str:
    ch1 = pg.PlotWidget()
    ch2 = pg.PlotWidget()
    ch3 = pg.PlotWidget()

    graphs = {
        "channel_1": ch1,
        "channel_2": ch2,
        "channel_3": ch3
    }

    for index, channel in enumerate(graphs.keys()):
        channel_name = f"Channel {index+1}"
        graph = graphs[channel]
        graph.setTitle(channel_name)
        layout.addWidget(graphs[channel])

    return graphs


def prepare_menu(app, channels: dict, menu: QMenu):
    menu.addAction("Merge Graphs")
    active_gmenu = QMenu("Active Graphs", app)
    color_menu = QMenu("Set Color", app)

    for index, channel in enumerate(channels.keys()):
        channel_name = f"Channel {index+1}"
        
        active_action = QAction(channel_name, app)
        active_action.setCheckable(True)
        active_action.setChecked(True)
        active_gmenu.addAction(active_action)

        color_action = QAction(channel_name, app)
        color_menu.addAction(color_action)

    menu.addMenu(active_gmenu)
    menu.addMenu(color_menu)
