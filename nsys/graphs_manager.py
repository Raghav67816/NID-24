"""
manages functions related to graphs
1. preparing graphs and objects
2. merging them
3. menu related functions
"""

import pyqtgraph as pg
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLayout, QMenu, QSizePolicy, QColorDialog

def prepare_graphs(layout: QLayout) -> tuple:
    ch1 = pg.PlotWidget()
    ch2 = pg.PlotWidget()
    ch3 = pg.PlotWidget()

    graphs = {
        "channel_1": ch1,
        "channel_2": ch2,
        "channel_3": ch3
    }

    curves = {
        "channel_1": ch1.plot(),
        "channel_2": ch2.plot(),
        "channel_3": ch3.plot()
    }

    for index, channel in enumerate(graphs.keys()):
        channel_name = f"Channel {index+1}"
        graph = graphs[channel]
        graph.setTitle(channel_name)
        graph.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        layout.addWidget(graphs[channel])

    return graphs, curves

def on_active_menu_triggered(action, channels: dict):
    channel_name = action.text().lower().replace(" ", "_")
    graph = channels[channel_name]
    if action.isChecked(): # hidden
        graph.show()
    else:
        graph.setMinimumSize(channels[channel_name].size())
        graph.hide()

def change_graph_color(color, graph):
    print(f"type of color: {type(color.toRgb())}")
    graph.getAxis("left").setPen(color.toRgb())
    graph.getAxis("bottom").setPen(color.toRgb())

    
def show_color_dialog(graph_name: str, channels:dict):
    graph_name = graph_name.lower().replace(" ", "_")
    color_dialog = QColorDialog()
    color_dialog.colorSelected.connect(lambda color: change_graph_color(color, channels[graph_name]))
    color_dialog.show()
    color_dialog.exec()


def on_set_color(action: QAction, channels: dict):
    show_color_dialog(action.text(), channels)
    print(action.text())


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
    active_gmenu.triggered.connect(lambda checked: on_active_menu_triggered(checked, channels))
    color_menu.triggered.connect(lambda checked: on_set_color(checked, channels))
    menu.addMenu(color_menu)
