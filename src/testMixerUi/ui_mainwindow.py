# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        MainWindow.setIconSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 20, 80, 24))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(720, 170, 20, 191))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMinimum(-90)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_2 = QProgressBar(self.centralwidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(750, 170, 20, 191))
        self.progressBar_2.setMinimum(-90)
        self.progressBar_2.setMaximum(0)
        self.progressBar_2.setValue(-90)
        self.progressBar_2.setOrientation(Qt.Orientation.Vertical)
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(80, 50, 41, 41))
        self.dial.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(85, 34, 31, 16))
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(334, 79, 222, 96))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.dial_4 = QDial(self.gridLayoutWidget)
        self.dial_4.setObjectName(u"dial_4")

        self.gridLayout.addWidget(self.dial_4, 1, 2, 1, 1)

        self.dial_5 = QDial(self.gridLayoutWidget)
        self.dial_5.setObjectName(u"dial_5")

        self.gridLayout.addWidget(self.dial_5, 1, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.dial_2 = QDial(self.gridLayoutWidget)
        self.dial_2.setObjectName(u"dial_2")

        self.gridLayout.addWidget(self.dial_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 0, 3, 1, 1)

        self.dial_3 = QDial(self.gridLayoutWidget)
        self.dial_3.setObjectName(u"dial_3")

        self.gridLayout.addWidget(self.dial_3, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(307, 198, 278, 96))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dial_9 = QDial(self.gridLayoutWidget_2)
        self.dial_9.setObjectName(u"dial_9")

        self.gridLayout_2.addWidget(self.dial_9, 1, 3, 1, 1)

        self.dial_7 = QDial(self.gridLayoutWidget_2)
        self.dial_7.setObjectName(u"dial_7")

        self.gridLayout_2.addWidget(self.dial_7, 1, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.dial_8 = QDial(self.gridLayoutWidget_2)
        self.dial_8.setObjectName(u"dial_8")

        self.gridLayout_2.addWidget(self.dial_8, 1, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)

        self.dial_10 = QDial(self.gridLayoutWidget_2)
        self.dial_10.setObjectName(u"dial_10")

        self.gridLayout_2.addWidget(self.dial_10, 1, 4, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 2, 4, 1, 1)

        self.dial_6 = QDial(self.gridLayoutWidget_2)
        self.dial_6.setObjectName(u"dial_6")

        self.gridLayout_2.addWidget(self.dial_6, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_20, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_21, 0, 2, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_22, 0, 3, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_23, 0, 4, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(367, 318, 166, 101))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.gridLayoutWidget_3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_26, 0, 2, 1, 1)

        self.dial_13 = QDial(self.gridLayoutWidget_3)
        self.dial_13.setObjectName(u"dial_13")

        self.gridLayout_3.addWidget(self.dial_13, 1, 2, 1, 1)

        self.dial_11 = QDial(self.gridLayoutWidget_3)
        self.dial_11.setObjectName(u"dial_11")

        self.gridLayout_3.addWidget(self.dial_11, 1, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 2, 2, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_25, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.dial_12 = QDial(self.gridLayoutWidget_3)
        self.dial_12.setObjectName(u"dial_12")

        self.gridLayout_3.addWidget(self.dial_12, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(423, 299, 49, 16))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(396, 179, 101, 20))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(430, 60, 31, 16))
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.progressBar.setFormat("")
        self.progressBar_2.setFormat("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"GAIN", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Hysterisis", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ratio", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Knee", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"LIMITER", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"COMPRESSOR", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"GATE", None))
    # retranslateUi

