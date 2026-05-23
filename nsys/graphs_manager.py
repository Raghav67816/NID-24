"""
manages functions related to graphs
1. preparing graphs and objects
2. merging them
3. menu related functions
"""

import pyqtgraph as pg
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QLayout, QMenu, QSizePolicy, QColorDialog

def on_region_finished(lrt: pg.LinearRegionItem):
    return lrt.getRegion()


def attach_lrt(graph: pg.PlotWidget, lrt_refs: dict, channels: dict):
    lrt = pg.LinearRegionItem(
        orientation="vertical",
        pen=pg.mkPen("r"),
    )

    lrt.sigRegionChangeFinished.connect(on_region_finished)
    graph.addItem(lrt)

    channel_keys = list(channels.keys())

    for index, channel in enumerate(channels.values()):
        if channel == graph:
            channel_key = channel_keys[index]
            lrt_refs[channel_key] = lrt
            return


def confirm_regions(lrt_refs: dict, channels: dict):
    if list(lrt_refs.values()).count(None) == 3:
        return
    
    # get non None reference
    global lrt_ref_
    for lrt_ref in lrt_refs.values():
        if lrt_ref != None:
            lrt_ref_ = lrt_ref
    
    # attach 
    for channel in channels:
        if lrt_refs[channel] == None:
            attach_lrt(channels[channel], lrt_refs, channels)

    for lrt_ref in lrt_refs.values():
        lrt_ref.setRegion(lrt_ref_.getRegion())

def detach_lrt(graph: pg.PlotWidget, lrt: pg.LinearRegionItem, lrt_refs: dict):
    for index, lrt_ in enumerate(lrt_refs.values()):
        if lrt == lrt_:
            lrt_refs[lrt_refs.keys()[index]] = None
            break

    graph.removeItem(lrt)

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
