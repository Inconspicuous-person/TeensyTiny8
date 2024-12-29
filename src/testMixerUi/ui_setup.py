# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainButton = QPushButton(self.centralwidget)
        self.mainButton.setObjectName(u"mainButton")
        self.mainButton.setGeometry(QRect(10, 10, 80, 24))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(10)
        font.setBold(True)
        self.mainButton.setFont(font)
        self.mainButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.quit = QPushButton(self.centralwidget)
        self.quit.setObjectName(u"quit")
        self.quit.setGeometry(QRect(700, 10, 80, 24))
        self.quit.setFont(font)
        self.quit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.quit.setFlat(False)
        self.routingButton = QPushButton(self.centralwidget)
        self.routingButton.setObjectName(u"routingButton")
        self.routingButton.setGeometry(QRect(100, 10, 80, 24))
        self.routingButton.setFont(font)
        self.routingButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.mixesButton = QPushButton(self.centralwidget)
        self.mixesButton.setObjectName(u"mixesButton")
        self.mixesButton.setGeometry(QRect(190, 10, 80, 24))
        self.mixesButton.setFont(font)
        self.mixesButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.overviewButton = QPushButton(self.centralwidget)
        self.overviewButton.setObjectName(u"overviewButton")
        self.overviewButton.setGeometry(QRect(280, 10, 80, 24))
        self.overviewButton.setFont(font)
        self.overviewButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainButton.setText(QCoreApplication.translate("MainWindow", u"MAIN", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
        self.routingButton.setText(QCoreApplication.translate("MainWindow", u"ROUTING", None))
        self.mixesButton.setText(QCoreApplication.translate("MainWindow", u"MIXES", None))
        self.overviewButton.setText(QCoreApplication.translate("MainWindow", u"OVERVIEW", None))
    # retranslateUi

