from os import getcwd
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel

def prepare_features_box(parent, features_box: QTabWidget):
    with open(f"{getcwd()}\\config\\features.txt", "r") as f_file:
        features = f_file.readlines()
        f_file.close()

        num_tabs = features_box.count()
        refs = {}

        for i in range(num_tabs):

            widget = features_box.widget(i)
            layout = QFormLayout(parent)

            for feature in features:
                label = QLabel(f"{feature}: ".replace("\n", ""))
                label_val = QLabel("-")
                label_val.setObjectName(f"channel_1_{feature}")
                
                layout.addRow(label, label_val)

                refs[label_val.objectName] = label_val

            widget.setLayout(layout)

