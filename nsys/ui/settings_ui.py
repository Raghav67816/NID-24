# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(800, 600)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.themeTab = QWidget()
        self.themeTab.setObjectName(u"themeTab")
        self.verticalLayout_2 = QVBoxLayout(self.themeTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.generalBox = QGroupBox(self.themeTab)
        self.generalBox.setObjectName(u"generalBox")
        self.formLayout_2 = QFormLayout(self.generalBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(20)
        self.themeLabel = QLabel(self.generalBox)
        self.themeLabel.setObjectName(u"themeLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.themeLabel)

        self.theme = QComboBox(self.generalBox)
        self.theme.setObjectName(u"theme")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.theme)


        self.verticalLayout_2.addWidget(self.generalBox)

        self.gavBox = QGroupBox(self.themeTab)
        self.gavBox.setObjectName(u"gavBox")
        self.formLayout = QFormLayout(self.gavBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.updateIntLabel = QLabel(self.gavBox)
        self.updateIntLabel.setObjectName(u"updateIntLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.updateIntLabel)

        self.updateInterval = QLineEdit(self.gavBox)
        self.updateInterval.setObjectName(u"updateInterval")
        self.updateInterval.setReadOnly(False)
        self.updateInterval.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.updateInterval.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.updateInterval)


        self.verticalLayout_2.addWidget(self.gavBox)

        self.tabWidget.addTab(self.themeTab, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.saveDataLabel = QLabel(self.groupBox_3)
        self.saveDataLabel.setObjectName(u"saveDataLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.saveDataLabel)

        self.saveDataPath = QLineEdit(self.groupBox_3)
        self.saveDataPath.setObjectName(u"saveDataPath")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.saveDataPath)

        self.mPackIndexLabel = QLabel(self.groupBox_3)
        self.mPackIndexLabel.setObjectName(u"mPackIndexLabel")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mPackIndexLabel)

        self.maxPacketIndex = QLineEdit(self.groupBox_3)
        self.maxPacketIndex.setObjectName(u"maxPacketIndex")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.maxPacketIndex)

        self.serialPortLabel = QLabel(self.groupBox_3)
        self.serialPortLabel.setObjectName(u"serialPortLabel")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.serialPortLabel)

        self.serialPortBox = QComboBox(self.groupBox_3)
        self.serialPortBox.setObjectName(u"serialPortBox")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.serialPortBox)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.widget, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.btnBox = QFrame(self.centralwidget)
        self.btnBox.setObjectName(u"btnBox")
        self.btnBox.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.btnBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.discardBtn = QPushButton(self.btnBox)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setMinimumSize(QSize(0, 40))
        self.discardBtn.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.discardBtn)

        self.applyBtn = QPushButton(self.btnBox)
        self.applyBtn.setObjectName(u"applyBtn")
        self.applyBtn.setMinimumSize(QSize(0, 40))
        self.applyBtn.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.applyBtn)


        self.verticalLayout.addWidget(self.btnBox, 0, Qt.AlignmentFlag.AlignRight)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.generalBox.setTitle(QCoreApplication.translate("SettingsWindow", u"General", None))
        self.themeLabel.setText(QCoreApplication.translate("SettingsWindow", u"Theme:", None))
        self.gavBox.setTitle(QCoreApplication.translate("SettingsWindow", u"Graphs and Visualisation", None))
        self.updateIntLabel.setText(QCoreApplication.translate("SettingsWindow", u"Update Interval:", None))
        self.updateInterval.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"for ex. 60Hz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.themeTab), QCoreApplication.translate("SettingsWindow", u"Apperance", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsWindow", u"Data Recorder", None))
        self.saveDataLabel.setText(QCoreApplication.translate("SettingsWindow", u"Save Data In: ", None))
        self.saveDataPath.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"/path/to/dir", None))
        self.mPackIndexLabel.setText(QCoreApplication.translate("SettingsWindow", u"Max Packet Index:", None))
        self.maxPacketIndex.setPlaceholderText(QCoreApplication.translate("SettingsWindow", u"1000 by default", None))
        self.serialPortLabel.setText(QCoreApplication.translate("SettingsWindow", u"Serial Port: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("SettingsWindow", u"Project", None))
        self.discardBtn.setText(QCoreApplication.translate("SettingsWindow", u"Close", None))
        self.applyBtn.setText(QCoreApplication.translate("SettingsWindow", u"Apply", None))
    # retranslateUi

