# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
    QFrame, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_DeviceConnDialog(object):
    def setupUi(self, DeviceConnDialog):
        if not DeviceConnDialog.objectName():
            DeviceConnDialog.setObjectName(u"DeviceConnDialog")
        DeviceConnDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DeviceConnDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(DeviceConnDialog)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.refreshBtn = QToolButton(self.header)
        self.refreshBtn.setObjectName(u"refreshBtn")

        self.horizontalLayout.addWidget(self.refreshBtn)


        self.verticalLayout.addWidget(self.header)

        self.devicesContainer = QListWidget(DeviceConnDialog)
        self.devicesContainer.setObjectName(u"devicesContainer")

        self.verticalLayout.addWidget(self.devicesContainer)

        self.buttonBox = QDialogButtonBox(DeviceConnDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DeviceConnDialog)
        self.buttonBox.accepted.connect(DeviceConnDialog.accept)
        self.buttonBox.rejected.connect(DeviceConnDialog.reject)

        QMetaObject.connectSlotsByName(DeviceConnDialog)
    # setupUi

    def retranslateUi(self, DeviceConnDialog):
        DeviceConnDialog.setWindowTitle(QCoreApplication.translate("DeviceConnDialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("DeviceConnDialog", u"Connected Devices:", None))
        self.refreshBtn.setText("")
    # retranslateUi

