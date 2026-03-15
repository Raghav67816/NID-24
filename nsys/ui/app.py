# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSplitter, QToolButton, QVBoxLayout, QWidget)
from ui import resources_rc

class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        if not AppWindow.objectName():
            AppWindow.setObjectName(u"AppWindow")
        AppWindow.setWindowModality(Qt.WindowModality.NonModal)
        AppWindow.resize(800, 600)
        self.centralwidget = QWidget(AppWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.splitterLayout = QVBoxLayout(self.container)
        self.splitterLayout.setSpacing(0)
        self.splitterLayout.setObjectName(u"splitterLayout")
        self.splitterLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.container)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.topBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 0, 12, 0)
        self.boardBtn = QToolButton(self.topBar)
        self.boardBtn.setObjectName(u"boardBtn")
        self.boardBtn.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/connection.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boardBtn.setIcon(icon)
        self.boardBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.boardBtn)


        self.splitterLayout.addWidget(self.topBar, 0, Qt.AlignmentFlag.AlignLeft)

        self.splitter = QSplitter(self.container)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.left_container = QFrame(self.splitter)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(200, 0))
        self.left_container.setStyleSheet(u"QFrame{\n"
"	border: none\n"
"}")
        self.left_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Shadow.Raised)
        self.graphLayout = QVBoxLayout(self.left_container)
        self.graphLayout.setSpacing(0)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.graphLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.left_container)
        self.right_container = QFrame(self.splitter)
        self.right_container.setObjectName(u"right_container")
        self.right_container.setMinimumSize(QSize(100, 0))
        self.right_container.setMaximumSize(QSize(16777215, 16777215))
        self.right_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ds_box = QGroupBox(self.right_container)
        self.ds_box.setObjectName(u"ds_box")
        self.verticalLayout_3 = QVBoxLayout(self.ds_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.deviceSelectionBox = QComboBox(self.ds_box)
        self.deviceSelectionBox.addItem("")
        self.deviceSelectionBox.setObjectName(u"deviceSelectionBox")

        self.verticalLayout_3.addWidget(self.deviceSelectionBox)

        self.dsParamLayout = QFormLayout()
        self.dsParamLayout.setObjectName(u"dsParamLayout")
        self.freqLabel = QLabel(self.ds_box)
        self.freqLabel.setObjectName(u"freqLabel")

        self.dsParamLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.freqLabel)

        self.freqInput = QLineEdit(self.ds_box)
        self.freqInput.setObjectName(u"freqInput")

        self.dsParamLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.freqInput)

        self.noiseLabel = QLabel(self.ds_box)
        self.noiseLabel.setObjectName(u"noiseLabel")

        self.dsParamLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.noiseLabel)

        self.noiseLevel = QSlider(self.ds_box)
        self.noiseLevel.setObjectName(u"noiseLevel")
        self.noiseLevel.setOrientation(Qt.Orientation.Horizontal)

        self.dsParamLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.noiseLevel)


        self.verticalLayout_3.addLayout(self.dsParamLayout)

        self.toggleDataBtn = QPushButton(self.ds_box)
        self.toggleDataBtn.setObjectName(u"toggleDataBtn")

        self.verticalLayout_3.addWidget(self.toggleDataBtn)


        self.verticalLayout_2.addWidget(self.ds_box)

        self.featuresBox = QGroupBox(self.right_container)
        self.featuresBox.setObjectName(u"featuresBox")

        self.verticalLayout_2.addWidget(self.featuresBox)

        self.splitter.addWidget(self.right_container)

        self.splitterLayout.addWidget(self.splitter)

        self.bottomBar = QFrame(self.container)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 40))
        self.bottomBar.setMaximumSize(QSize(16777215, 40))
        self.bottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.statusLabel = QFrame(self.bottomBar)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setStyleSheet(u"QFrame{\n"
"	border: none\n"
"}")
        self.statusLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusLabel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.statusLabel)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.statusText = QLabel(self.statusLabel)
        self.statusText.setObjectName(u"statusText")

        self.horizontalLayout.addWidget(self.statusText)

        self.statusVal = QLabel(self.statusLabel)
        self.statusVal.setObjectName(u"statusVal")

        self.horizontalLayout.addWidget(self.statusVal)


        self.horizontalLayout_3.addWidget(self.statusLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.splitterLayout.addWidget(self.bottomBar, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addWidget(self.container)

        AppWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AppWindow)

        QMetaObject.connectSlotsByName(AppWindow)
    # setupUi

    def retranslateUi(self, AppWindow):
        AppWindow.setWindowTitle(QCoreApplication.translate("AppWindow", u"NID-24 Analysis Software", None))
        self.boardBtn.setText("")
        self.ds_box.setTitle(QCoreApplication.translate("AppWindow", u"Data Simulator", None))
        self.deviceSelectionBox.setItemText(0, QCoreApplication.translate("AppWindow", u"Simulated", None))

        self.freqLabel.setText(QCoreApplication.translate("AppWindow", u"Frequency:", None))
        self.noiseLabel.setText(QCoreApplication.translate("AppWindow", u"Noise Level:", None))
        self.toggleDataBtn.setText(QCoreApplication.translate("AppWindow", u"Start", None))
        self.featuresBox.setTitle(QCoreApplication.translate("AppWindow", u"Features", None))
        self.statusText.setText(QCoreApplication.translate("AppWindow", u"Status:", None))
        self.statusVal.setText(QCoreApplication.translate("AppWindow", u"Disconnected", None))
    # retranslateUi

