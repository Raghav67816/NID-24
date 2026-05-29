from os import getcwd
from random import randint

from time import time

from settings import Settings

import numpy as np
from PySide6.QtCore import Qt
from ui.SaveDataDialog import Ui_SaveDataDialog
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QDialogButtonBox

class SaveDataDialog(QDialog):
    def __init__(self,
                style: str, 
                computed_features: dict,
                settings_obj: Settings, 
                class_labels_ref: dict):
        super(SaveDataDialog, self).__init__()
        
        self.ui = Ui_SaveDataDialog()
        self.ui.setupUi(self)

        self.ui.labelEdit.setPlaceholderText("Enter class name e.g PINCH, FIST etc")
        self.setStyleSheet(style)

        self.computed_features = computed_features

        self.class_labels_ref = class_labels_ref
        self.settings_obj = settings_obj

        self.class_id = 0

        self.show_feature_vals()

        self.ui.saveBtn.clicked.connect(self.on_save_clicked)
        self.ui.cancelBtn.clicked.connect(self.on_cancel_clicked)

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
        class_label = self.ui.labelEdit.text()
        if class_label in list(self.class_labels_ref.keys()):
            print(f"{class_label} found in label ids")
            self.class_id = self.class_labels_ref[class_label]
        
        else:
            self.class_id = randint(0, 20)
            while self.class_id in list(self.class_labels_ref.values()):
                self.class_id = randint(0, 20)

            self.class_labels_ref[class_label] = self.class_id

        path = f"{getcwd()}/data/{time()}.npy"
        np.save(path, np.array([self.class_labels_ref[class_label], self.computed_features]))

        print(self.class_labels_ref)

    def on_save_clicked(self):
        self.save_data()
        self.accept()

    def on_cancel_clicked(self):
        self.reject()
