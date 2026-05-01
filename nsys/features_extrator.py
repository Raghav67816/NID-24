from os import getcwd
from PySide6.QtWidgets import QTabWidget, QFormLayout, QLabel

def prepare_features_box(features_box: QTabWidget):

    with open(f"{getcwd()}\\config\\features.txt", "r") as f_file:
        features = f_file.readlines()
        f_file.close()

        num_tabs = features_box.count()
        refs = {}

        for i in range(num_tabs):

            widget = features_box.widget(i)
            layout = QFormLayout(widget)

            for feature in features:
                feature = feature.replace("\n", "")
                label = QLabel(f"{feature}: ")
                label_val = QLabel("-")
                label_val.setObjectName(f"channel_{i+1}_{feature}")
                
                layout.addRow(label, label_val)

                refs[label_val.objectName] = label_val

