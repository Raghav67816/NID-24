from os import getcwd
from random import Random

import numpy as np
from PySide6.QtCore import Qt
from ui.SaveDataDialog import Ui_SaveDataDialog
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QDialogButtonBox

class SaveDataDialog(QDialog):
    def __init__(self, style: str, computed_features: dict):
        super(SaveDataDialog, self).__init__()
        
        self.ui = Ui_SaveDataDialog()
        self.ui.setupUi(self)

        self.ui.labelEdit.setPlaceholderText("Enter class name e.g PINCH, FIST etc")
        self.setStyleSheet(style)

        self.computed_features = computed_features

        self.label_ids = {}

        self.show_feature_vals()

        self.ui.buttonBox.clicked.connect(self.on_buttonBox_clicked)

    def show_feature_vals(self):
        self.ui.featuresTable.setRowCount(len(self.computed_features.keys()))
        for index, feature in enumerate(self.computed_features.keys()):
            # write feature names
            # column = 0
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            item.setText(feature)
            self.ui.featuresTable.setItem(index, 0, item)

            for v_index, val in enumerate(self.computed_features[feature]):
    
                # write feature vals
                val_item = QTableWidgetItem()
                val_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                val_item.setText(str(val))

                self.ui.featuresTable.setItem(index, v_index + 1, val_item)

    def save_data(self):
        self.r_id = Random.randint(0, 20)
        while self.r_id in self.label_ids.values():
            self.r_id = Random.randint(0, 20)

        class_label = self.ui.labelEdit.text()
        if class_label not in self.label_ids.keys():
            self.label_ids[class_label] = self.r_id

        array = np.array([self.r_id, self.computed_features])
        np.save(f"{getcwd()}/data/{self.r_id}.npy", array)

    
    def on_buttonBox_clicked(self, button):
        if button.text() == QDialogButtonBox.ButtonRole.AcceptRole:
            print("accepted")
