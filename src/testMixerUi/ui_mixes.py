# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mixes.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"background-color: rgb(44, 44, 44);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.setupButton = QPushButton(self.centralwidget)
        self.setupButton.setObjectName(u"setupButton")
        self.setupButton.setGeometry(QRect(710, 10, 80, 24))
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(10)
        font.setBold(True)
        self.setupButton.setFont(font)
        self.setupButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton.setAutoDefault(False)
        self.setupButton.setFlat(False)
        self.setupButton_2 = QPushButton(self.centralwidget)
        self.setupButton_2.setObjectName(u"setupButton_2")
        self.setupButton_2.setGeometry(QRect(10, 90, 71, 24))
        self.setupButton_2.setFont(font)
        self.setupButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_2.setAutoDefault(False)
        self.setupButton_2.setFlat(False)
        self.setupButton_3 = QPushButton(self.centralwidget)
        self.setupButton_3.setObjectName(u"setupButton_3")
        self.setupButton_3.setGeometry(QRect(90, 90, 71, 24))
        self.setupButton_3.setFont(font)
        self.setupButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_3.setAutoDefault(False)
        self.setupButton_3.setFlat(False)
        self.setupButton_4 = QPushButton(self.centralwidget)
        self.setupButton_4.setObjectName(u"setupButton_4")
        self.setupButton_4.setGeometry(QRect(170, 90, 71, 24))
        self.setupButton_4.setFont(font)
        self.setupButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_4.setAutoDefault(False)
        self.setupButton_4.setFlat(False)
        self.setupButton_5 = QPushButton(self.centralwidget)
        self.setupButton_5.setObjectName(u"setupButton_5")
        self.setupButton_5.setGeometry(QRect(250, 90, 71, 24))
        self.setupButton_5.setFont(font)
        self.setupButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_5.setAutoDefault(False)
        self.setupButton_5.setFlat(False)
        self.setupButton_6 = QPushButton(self.centralwidget)
        self.setupButton_6.setObjectName(u"setupButton_6")
        self.setupButton_6.setGeometry(QRect(330, 90, 71, 24))
        self.setupButton_6.setFont(font)
        self.setupButton_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_6.setAutoDefault(False)
        self.setupButton_6.setFlat(False)
        self.setupButton_7 = QPushButton(self.centralwidget)
        self.setupButton_7.setObjectName(u"setupButton_7")
        self.setupButton_7.setGeometry(QRect(410, 90, 71, 24))
        self.setupButton_7.setFont(font)
        self.setupButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_7.setAutoDefault(False)
        self.setupButton_7.setFlat(False)
        self.setupButton_8 = QPushButton(self.centralwidget)
        self.setupButton_8.setObjectName(u"setupButton_8")
        self.setupButton_8.setGeometry(QRect(490, 90, 71, 24))
        self.setupButton_8.setFont(font)
        self.setupButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_8.setAutoDefault(False)
        self.setupButton_8.setFlat(False)
        self.setupButton_9 = QPushButton(self.centralwidget)
        self.setupButton_9.setObjectName(u"setupButton_9")
        self.setupButton_9.setGeometry(QRect(570, 90, 71, 24))
        self.setupButton_9.setFont(font)
        self.setupButton_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_9.setAutoDefault(False)
        self.setupButton_9.setFlat(False)
        self.setupButton_10 = QPushButton(self.centralwidget)
        self.setupButton_10.setObjectName(u"setupButton_10")
        self.setupButton_10.setGeometry(QRect(650, 90, 71, 24))
        self.setupButton_10.setFont(font)
        self.setupButton_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.setupButton_10.setAutoDefault(False)
        self.setupButton_10.setFlat(False)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(460, 180, 61, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_4, 3, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_8, 7, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_6, 5, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_7, 6, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_5, 4, 1, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 2, 0, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 3, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 5, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 6, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 7, 0, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(90, 220, 91, 22))
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(90, 240, 91, 22))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(570, 180, 61, 291))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_9 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_9, 3, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_10, 7, 1, 1, 1)

        self.checkBox_11 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_11, 5, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_12, 6, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_13, 1, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_14.setObjectName(u"checkBox_14")
        sizePolicy.setHeightForWidth(self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_14, 2, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_15, 4, 1, 1, 1)

        self.checkBox_16 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_16, 0, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_29, 1, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_32, 4, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_33, 5, 0, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_34, 6, 0, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_35, 7, 0, 1, 1)

        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(451, 160, 71, 16))
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(561, 160, 71, 16))
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(90, 310, 91, 22))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(90, 330, 91, 22))
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.setupButton.setDefault(False)
        self.setupButton_2.setDefault(False)
        self.setupButton_3.setDefault(False)
        self.setupButton_4.setDefault(False)
        self.setupButton_5.setDefault(False)
        self.setupButton_6.setDefault(False)
        self.setupButton_7.setDefault(False)
        self.setupButton_8.setDefault(False)
        self.setupButton_9.setDefault(False)
        self.setupButton_10.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.setupButton.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.setupButton_2.setText(QCoreApplication.translate("MainWindow", u"MAIN", None))
        self.setupButton_3.setText(QCoreApplication.translate("MainWindow", u"AUX 1", None))
        self.setupButton_4.setText(QCoreApplication.translate("MainWindow", u"AUX 2", None))
        self.setupButton_5.setText(QCoreApplication.translate("MainWindow", u"AUX 3", None))
        self.setupButton_6.setText(QCoreApplication.translate("MainWindow", u"AUX 4", None))
        self.setupButton_7.setText(QCoreApplication.translate("MainWindow", u"AUX 5", None))
        self.setupButton_8.setText(QCoreApplication.translate("MainWindow", u"AUX 6", None))
        self.setupButton_9.setText(QCoreApplication.translate("MainWindow", u"AUX 7", None))
        self.setupButton_10.setText(QCoreApplication.translate("MainWindow", u"AUX 8", None))
        self.checkBox_4.setText("")
        self.checkBox_8.setText("")
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_5.setText("")
        self.checkBox.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"STEREO", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"MONO", None))
        self.checkBox_9.setText("")
        self.checkBox_10.setText("")
        self.checkBox_11.setText("")
        self.checkBox_12.setText("")
        self.checkBox_13.setText("")
        self.checkBox_14.setText("")
        self.checkBox_15.setText("")
        self.checkBox_16.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"PRE FADE", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"POST FADE", None))
    # retranslateUi

