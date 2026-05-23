# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_labeling_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QLineEdit, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_SaveDataDialog(object):
    def setupUi(self, SaveDataDialog):
        if not SaveDataDialog.objectName():
            SaveDataDialog.setObjectName(u"SaveDataDialog")
        SaveDataDialog.resize(394, 296)
        self.verticalLayout = QVBoxLayout(SaveDataDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.featuresTable = QTableWidget(SaveDataDialog)
        if (self.featuresTable.columnCount() < 4):
            self.featuresTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.featuresTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.featuresTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.featuresTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.featuresTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.featuresTable.setObjectName(u"featuresTable")

        self.verticalLayout.addWidget(self.featuresTable)

        self.labelEdit = QLineEdit(SaveDataDialog)
        self.labelEdit.setObjectName(u"labelEdit")

        self.verticalLayout.addWidget(self.labelEdit)

        self.buttonBox = QDialogButtonBox(SaveDataDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SaveDataDialog)
        self.buttonBox.accepted.connect(SaveDataDialog.accept)
        self.buttonBox.rejected.connect(SaveDataDialog.reject)

        QMetaObject.connectSlotsByName(SaveDataDialog)
    # setupUi

    def retranslateUi(self, SaveDataDialog):
        SaveDataDialog.setWindowTitle(QCoreApplication.translate("SaveDataDialog", u"Label Data & Save", None))
        ___qtablewidgetitem = self.featuresTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SaveDataDialog", u"Feature", None))
        ___qtablewidgetitem1 = self.featuresTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SaveDataDialog", u"Channel 1", None))
        ___qtablewidgetitem2 = self.featuresTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SaveDataDialog", u"Channel 2", None))
        ___qtablewidgetitem3 = self.featuresTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SaveDataDialog", u"Channel 3", None))
    # retranslateUi

