# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataControlWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QToolButton,
    QWidget)
from ui import resources_rc

class Ui_dataControlWidget(object):
    def setupUi(self, dataControlWidget):
        if not dataControlWidget.objectName():
            dataControlWidget.setObjectName(u"dataControlWidget")
        dataControlWidget.resize(226, 64)
        self.horizontalLayout = QHBoxLayout(dataControlWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevBtn = QToolButton(dataControlWidget)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.prevBtn)

        self.toggleBtn = QToolButton(dataControlWidget)
        self.toggleBtn.setObjectName(u"toggleBtn")
        self.toggleBtn.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-play-30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toggleBtn)

        self.forwardBtn = QToolButton(dataControlWidget)
        self.forwardBtn.setObjectName(u"forwardBtn")
        self.forwardBtn.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forwardBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.forwardBtn)


        self.retranslateUi(dataControlWidget)

        QMetaObject.connectSlotsByName(dataControlWidget)
    # setupUi

    def retranslateUi(self, dataControlWidget):
        dataControlWidget.setWindowTitle(QCoreApplication.translate("dataControlWidget", u"Form", None))
        self.prevBtn.setText(QCoreApplication.translate("dataControlWidget", u"...", None))
        self.toggleBtn.setText(QCoreApplication.translate("dataControlWidget", u"...", None))
        self.forwardBtn.setText("")
    # retranslateUi

