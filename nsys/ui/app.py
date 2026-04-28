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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)
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
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, 0, 12, 0)
        self.recLabel = QLabel(self.topBar)
        self.recLabel.setObjectName(u"recLabel")

        self.horizontalLayout_4.addWidget(self.recLabel)

        self.recordBtn = QToolButton(self.topBar)
        self.recordBtn.setObjectName(u"recordBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-play-30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.recordBtn.setIcon(icon)
        self.recordBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.recordBtn)

        self.recordingTime = QLabel(self.topBar)
        self.recordingTime.setObjectName(u"recordingTime")

        self.horizontalLayout_4.addWidget(self.recordingTime)

        self.line = QFrame(self.topBar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.modeToggleBtn = QToolButton(self.topBar)
        self.modeToggleBtn.setObjectName(u"modeToggleBtn")
        self.modeToggleBtn.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.modeToggleBtn)

        self.settingsBtn = QToolButton(self.topBar)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-gear-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon1)
        self.settingsBtn.setIconSize(QSize(24, 24))
        self.settingsBtn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout_4.addWidget(self.settingsBtn)


        self.splitterLayout.addWidget(self.topBar)

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
        self.loadFilePathEdit = QLineEdit(self.ds_box)
        self.loadFilePathEdit.setObjectName(u"loadFilePathEdit")

        self.verticalLayout_3.addWidget(self.loadFilePathEdit)

        self.frame = QFrame(self.ds_box)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.latencyLabel = QLabel(self.frame)
        self.latencyLabel.setObjectName(u"latencyLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.latencyLabel)

        self.latencyVal = QLabel(self.frame)
        self.latencyVal.setObjectName(u"latencyVal")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.latencyVal)


        self.verticalLayout_3.addWidget(self.frame)

        self.toggleDataBtn = QPushButton(self.ds_box)
        self.toggleDataBtn.setObjectName(u"toggleDataBtn")

        self.verticalLayout_3.addWidget(self.toggleDataBtn)


        self.verticalLayout_2.addWidget(self.ds_box)

        self.featuresBox = QGroupBox(self.right_container)
        self.featuresBox.setObjectName(u"featuresBox")
        self.verticalLayout_4 = QVBoxLayout(self.featuresBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.featuresTabWidget = QTabWidget(self.featuresBox)
        self.featuresTabWidget.setObjectName(u"featuresTabWidget")
        self.channel_1_features = QWidget()
        self.channel_1_features.setObjectName(u"channel_1_features")
        self.featuresTabWidget.addTab(self.channel_1_features, "")
        self.channel_2_features = QWidget()
        self.channel_2_features.setObjectName(u"channel_2_features")
        self.featuresTabWidget.addTab(self.channel_2_features, "")
        self.channel_3_features = QWidget()
        self.channel_3_features.setObjectName(u"channel_3_features")
        self.featuresTabWidget.addTab(self.channel_3_features, "")

        self.verticalLayout_4.addWidget(self.featuresTabWidget)


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

        self.featuresTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppWindow)
    # setupUi

    def retranslateUi(self, AppWindow):
        AppWindow.setWindowTitle(QCoreApplication.translate("AppWindow", u"NID-24 Analysis Software", None))
        self.recLabel.setText(QCoreApplication.translate("AppWindow", u"Data Recorder: ", None))
        self.recordBtn.setText("")
        self.recordingTime.setText(QCoreApplication.translate("AppWindow", u"00:00", None))
        self.modeToggleBtn.setText(QCoreApplication.translate("AppWindow", u"NOR", None))
        self.settingsBtn.setText("")
        self.ds_box.setTitle(QCoreApplication.translate("AppWindow", u"Data Tools", None))
        self.loadFilePathEdit.setPlaceholderText(QCoreApplication.translate("AppWindow", u"Load From File....", None))
#if QT_CONFIG(tooltip)
        self.latencyLabel.setToolTip(QCoreApplication.translate("AppWindow", u"<html><head/><body><p>Ideal Value is 1 ms for 1KHz Frequency</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.latencyLabel.setText(QCoreApplication.translate("AppWindow", u"Latency:", None))
        self.latencyVal.setText(QCoreApplication.translate("AppWindow", u"0", None))
        self.toggleDataBtn.setText(QCoreApplication.translate("AppWindow", u"Start", None))
        self.featuresBox.setTitle(QCoreApplication.translate("AppWindow", u"Features", None))
        self.featuresTabWidget.setTabText(self.featuresTabWidget.indexOf(self.channel_1_features), QCoreApplication.translate("AppWindow", u"Channel 1", None))
        self.featuresTabWidget.setTabText(self.featuresTabWidget.indexOf(self.channel_2_features), QCoreApplication.translate("AppWindow", u"Channel 2", None))
        self.featuresTabWidget.setTabText(self.featuresTabWidget.indexOf(self.channel_3_features), QCoreApplication.translate("AppWindow", u"Channel 3", None))
        self.statusText.setText(QCoreApplication.translate("AppWindow", u"Status:", None))
        self.statusVal.setText(QCoreApplication.translate("AppWindow", u"Disconnected", None))
    # retranslateUi

