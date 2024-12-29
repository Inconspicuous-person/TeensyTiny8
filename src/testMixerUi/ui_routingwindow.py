# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'routingwindow.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)

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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 130, 321, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_12, 4, 1, 1, 1)

        self.checkBox_20 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_20.setObjectName(u"checkBox_20")
        sizePolicy.setHeightForWidth(self.checkBox_20.sizePolicy().hasHeightForWidth())
        self.checkBox_20.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_20, 3, 4, 1, 1)

        self.checkBox_49 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_49.setObjectName(u"checkBox_49")
        sizePolicy.setHeightForWidth(self.checkBox_49.sizePolicy().hasHeightForWidth())
        self.checkBox_49.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_49, 6, 6, 1, 1)

        self.checkBox_25 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_25.setObjectName(u"checkBox_25")
        sizePolicy.setHeightForWidth(self.checkBox_25.sizePolicy().hasHeightForWidth())
        self.checkBox_25.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_25, 2, 5, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_13, 5, 1, 1, 1)

        self.checkBox_45 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_45.setObjectName(u"checkBox_45")
        sizePolicy.setHeightForWidth(self.checkBox_45.sizePolicy().hasHeightForWidth())
        self.checkBox_45.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_45, 6, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.checkBox_29 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_29.setObjectName(u"checkBox_29")
        sizePolicy.setHeightForWidth(self.checkBox_29.sizePolicy().hasHeightForWidth())
        self.checkBox_29.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_29, 3, 8, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_8, 1, 6, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)

        self.checkBox_42 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_42.setObjectName(u"checkBox_42")
        sizePolicy.setHeightForWidth(self.checkBox_42.sizePolicy().hasHeightForWidth())
        self.checkBox_42.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_42, 6, 4, 1, 1)

        self.checkBox_55 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_55.setObjectName(u"checkBox_55")
        sizePolicy.setHeightForWidth(self.checkBox_55.sizePolicy().hasHeightForWidth())
        self.checkBox_55.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_55, 7, 6, 1, 1)

        self.checkBox_60 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_60.setObjectName(u"checkBox_60")
        sizePolicy.setHeightForWidth(self.checkBox_60.sizePolicy().hasHeightForWidth())
        self.checkBox_60.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_60, 8, 3, 1, 1)

        self.checkBox_36 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_36.setObjectName(u"checkBox_36")
        sizePolicy.setHeightForWidth(self.checkBox_36.sizePolicy().hasHeightForWidth())
        self.checkBox_36.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_36, 4, 7, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_4, 3, 2, 1, 1)

        self.checkBox_31 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_31.setObjectName(u"checkBox_31")
        sizePolicy.setHeightForWidth(self.checkBox_31.sizePolicy().hasHeightForWidth())
        self.checkBox_31.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_31, 4, 3, 1, 1)

        self.checkBox_15 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_15, 7, 1, 1, 1)

        self.checkBox_16 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_16, 8, 1, 1, 1)

        self.checkBox_30 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_30.setObjectName(u"checkBox_30")
        sizePolicy.setHeightForWidth(self.checkBox_30.sizePolicy().hasHeightForWidth())
        self.checkBox_30.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_30, 3, 5, 1, 1)

        self.checkBox_52 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_52.setObjectName(u"checkBox_52")
        sizePolicy.setHeightForWidth(self.checkBox_52.sizePolicy().hasHeightForWidth())
        self.checkBox_52.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_52, 7, 2, 1, 1)

        self.checkBox_33 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_33.setObjectName(u"checkBox_33")
        sizePolicy.setHeightForWidth(self.checkBox_33.sizePolicy().hasHeightForWidth())
        self.checkBox_33.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_33, 4, 4, 1, 1)

        self.checkBox_24 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_24.setObjectName(u"checkBox_24")
        sizePolicy.setHeightForWidth(self.checkBox_24.sizePolicy().hasHeightForWidth())
        self.checkBox_24.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_24, 2, 3, 1, 1)

        self.checkBox_38 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_38.setObjectName(u"checkBox_38")
        sizePolicy.setHeightForWidth(self.checkBox_38.sizePolicy().hasHeightForWidth())
        self.checkBox_38.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_38, 4, 6, 1, 1)

        self.checkBox_35 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_35.setObjectName(u"checkBox_35")
        sizePolicy.setHeightForWidth(self.checkBox_35.sizePolicy().hasHeightForWidth())
        self.checkBox_35.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_35, 4, 5, 1, 1)

        self.checkBox_46 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_46.setObjectName(u"checkBox_46")
        sizePolicy.setHeightForWidth(self.checkBox_46.sizePolicy().hasHeightForWidth())
        self.checkBox_46.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_46, 5, 7, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_9, 1, 7, 1, 1)

        self.checkBox_27 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_27.setObjectName(u"checkBox_27")
        sizePolicy.setHeightForWidth(self.checkBox_27.sizePolicy().hasHeightForWidth())
        self.checkBox_27.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_27, 2, 4, 1, 1)

        self.checkBox_22 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_22.setObjectName(u"checkBox_22")
        sizePolicy.setHeightForWidth(self.checkBox_22.sizePolicy().hasHeightForWidth())
        self.checkBox_22.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_22, 2, 2, 1, 1)

        self.checkBox_23 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_23.setObjectName(u"checkBox_23")
        sizePolicy.setHeightForWidth(self.checkBox_23.sizePolicy().hasHeightForWidth())
        self.checkBox_23.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_23, 2, 8, 1, 1)

        self.checkBox_11 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_11, 3, 1, 1, 1)

        self.checkBox_17 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_17, 3, 7, 1, 1)

        self.checkBox_34 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_34.setObjectName(u"checkBox_34")
        sizePolicy.setHeightForWidth(self.checkBox_34.sizePolicy().hasHeightForWidth())
        self.checkBox_34.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_34, 5, 3, 1, 1)

        self.checkBox_48 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_48.setObjectName(u"checkBox_48")
        sizePolicy.setHeightForWidth(self.checkBox_48.sizePolicy().hasHeightForWidth())
        self.checkBox_48.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_48, 7, 3, 1, 1)

        self.checkBox_19 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_19.setObjectName(u"checkBox_19")
        sizePolicy.setHeightForWidth(self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_19, 4, 2, 1, 1)

        self.checkBox_50 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_50.setObjectName(u"checkBox_50")
        sizePolicy.setHeightForWidth(self.checkBox_50.sizePolicy().hasHeightForWidth())
        self.checkBox_50.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_50, 7, 5, 1, 1)

        self.checkBox_44 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_44.setObjectName(u"checkBox_44")
        sizePolicy.setHeightForWidth(self.checkBox_44.sizePolicy().hasHeightForWidth())
        self.checkBox_44.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_44, 5, 8, 1, 1)

        self.checkBox_47 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_47.setObjectName(u"checkBox_47")
        sizePolicy.setHeightForWidth(self.checkBox_47.sizePolicy().hasHeightForWidth())
        self.checkBox_47.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_47, 6, 5, 1, 1)

        self.checkBox_14 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName(u"checkBox_14")
        sizePolicy.setHeightForWidth(self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_14, 6, 1, 1, 1)

        self.checkBox_63 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_63.setObjectName(u"checkBox_63")
        sizePolicy.setHeightForWidth(self.checkBox_63.sizePolicy().hasHeightForWidth())
        self.checkBox_63.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_63, 8, 7, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_7, 1, 5, 1, 1)

        self.checkBox_56 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_56.setObjectName(u"checkBox_56")
        sizePolicy.setHeightForWidth(self.checkBox_56.sizePolicy().hasHeightForWidth())
        self.checkBox_56.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_56, 8, 4, 1, 1)

        self.checkBox_41 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_41.setObjectName(u"checkBox_41")
        sizePolicy.setHeightForWidth(self.checkBox_41.sizePolicy().hasHeightForWidth())
        self.checkBox_41.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_41, 5, 5, 1, 1)

        self.checkBox_32 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_32.setObjectName(u"checkBox_32")
        sizePolicy.setHeightForWidth(self.checkBox_32.sizePolicy().hasHeightForWidth())
        self.checkBox_32.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_32, 4, 8, 1, 1)

        self.checkBox_64 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_64.setObjectName(u"checkBox_64")
        sizePolicy.setHeightForWidth(self.checkBox_64.sizePolicy().hasHeightForWidth())
        self.checkBox_64.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_64, 8, 8, 1, 1)

        self.checkBox_37 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_37.setObjectName(u"checkBox_37")
        sizePolicy.setHeightForWidth(self.checkBox_37.sizePolicy().hasHeightForWidth())
        self.checkBox_37.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_37, 5, 2, 1, 1)

        self.checkBox_43 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_43.setObjectName(u"checkBox_43")
        sizePolicy.setHeightForWidth(self.checkBox_43.sizePolicy().hasHeightForWidth())
        self.checkBox_43.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_43, 5, 6, 1, 1)

        self.checkBox_51 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_51.setObjectName(u"checkBox_51")
        sizePolicy.setHeightForWidth(self.checkBox_51.sizePolicy().hasHeightForWidth())
        self.checkBox_51.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_51, 6, 7, 1, 1)

        self.checkBox_62 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_62.setObjectName(u"checkBox_62")
        sizePolicy.setHeightForWidth(self.checkBox_62.sizePolicy().hasHeightForWidth())
        self.checkBox_62.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_62, 8, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.checkBox_59 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_59.setObjectName(u"checkBox_59")
        sizePolicy.setHeightForWidth(self.checkBox_59.sizePolicy().hasHeightForWidth())
        self.checkBox_59.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_59, 7, 8, 1, 1)

        self.checkBox_54 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_54.setObjectName(u"checkBox_54")
        sizePolicy.setHeightForWidth(self.checkBox_54.sizePolicy().hasHeightForWidth())
        self.checkBox_54.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_54, 6, 8, 1, 1)

        self.checkBox_40 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_40.setObjectName(u"checkBox_40")
        sizePolicy.setHeightForWidth(self.checkBox_40.sizePolicy().hasHeightForWidth())
        self.checkBox_40.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_40, 6, 2, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_5, 1, 3, 1, 1)

        self.checkBox_58 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_58.setObjectName(u"checkBox_58")
        sizePolicy.setHeightForWidth(self.checkBox_58.sizePolicy().hasHeightForWidth())
        self.checkBox_58.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_58, 8, 6, 1, 1)

        self.checkBox_18 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_18.setObjectName(u"checkBox_18")
        sizePolicy.setHeightForWidth(self.checkBox_18.sizePolicy().hasHeightForWidth())
        self.checkBox_18.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_18, 3, 3, 1, 1)

        self.checkBox_10 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_10, 1, 8, 1, 1)

        self.checkBox_28 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_28.setObjectName(u"checkBox_28")
        sizePolicy.setHeightForWidth(self.checkBox_28.sizePolicy().hasHeightForWidth())
        self.checkBox_28.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_28, 3, 6, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.checkBox_39 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_39.setObjectName(u"checkBox_39")
        sizePolicy.setHeightForWidth(self.checkBox_39.sizePolicy().hasHeightForWidth())
        self.checkBox_39.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_39, 5, 4, 1, 1)

        self.checkBox_57 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_57.setObjectName(u"checkBox_57")
        sizePolicy.setHeightForWidth(self.checkBox_57.sizePolicy().hasHeightForWidth())
        self.checkBox_57.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_57, 7, 7, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_6, 1, 4, 1, 1)

        self.checkBox_53 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_53.setObjectName(u"checkBox_53")
        sizePolicy.setHeightForWidth(self.checkBox_53.sizePolicy().hasHeightForWidth())
        self.checkBox_53.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_53, 7, 4, 1, 1)

        self.checkBox_21 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_21.setObjectName(u"checkBox_21")
        sizePolicy.setHeightForWidth(self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_21, 2, 6, 1, 1)

        self.checkBox_26 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_26.setObjectName(u"checkBox_26")
        sizePolicy.setHeightForWidth(self.checkBox_26.sizePolicy().hasHeightForWidth())
        self.checkBox_26.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_26, 2, 7, 1, 1)

        self.checkBox_61 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_61.setObjectName(u"checkBox_61")
        sizePolicy.setHeightForWidth(self.checkBox_61.sizePolicy().hasHeightForWidth())
        self.checkBox_61.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.checkBox_61, 8, 5, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_13, 0, 5, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_14, 0, 6, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_15, 0, 7, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_16, 0, 8, 1, 1)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(160, 110, 71, 16))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 190, 21, 171))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(390, 190, 21, 171))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(540, 110, 71, 16))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(420, 130, 321, 291))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_65 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_65.setObjectName(u"checkBox_65")
        sizePolicy.setHeightForWidth(self.checkBox_65.sizePolicy().hasHeightForWidth())
        self.checkBox_65.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_65, 4, 1, 1, 1)

        self.checkBox_66 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_66.setObjectName(u"checkBox_66")
        sizePolicy.setHeightForWidth(self.checkBox_66.sizePolicy().hasHeightForWidth())
        self.checkBox_66.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_66, 3, 4, 1, 1)

        self.checkBox_67 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_67.setObjectName(u"checkBox_67")
        sizePolicy.setHeightForWidth(self.checkBox_67.sizePolicy().hasHeightForWidth())
        self.checkBox_67.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_67, 6, 6, 1, 1)

        self.checkBox_68 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_68.setObjectName(u"checkBox_68")
        sizePolicy.setHeightForWidth(self.checkBox_68.sizePolicy().hasHeightForWidth())
        self.checkBox_68.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_68, 2, 5, 1, 1)

        self.checkBox_69 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_69.setObjectName(u"checkBox_69")
        sizePolicy.setHeightForWidth(self.checkBox_69.sizePolicy().hasHeightForWidth())
        self.checkBox_69.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_69, 2, 1, 1, 1)

        self.checkBox_70 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_70.setObjectName(u"checkBox_70")
        sizePolicy.setHeightForWidth(self.checkBox_70.sizePolicy().hasHeightForWidth())
        self.checkBox_70.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_70, 5, 1, 1, 1)

        self.checkBox_71 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_71.setObjectName(u"checkBox_71")
        sizePolicy.setHeightForWidth(self.checkBox_71.sizePolicy().hasHeightForWidth())
        self.checkBox_71.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_71, 6, 3, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_21, 4, 0, 1, 1)

        self.checkBox_72 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_72.setObjectName(u"checkBox_72")
        sizePolicy.setHeightForWidth(self.checkBox_72.sizePolicy().hasHeightForWidth())
        self.checkBox_72.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_72, 3, 8, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_22, 5, 0, 1, 1)

        self.checkBox_73 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_73.setObjectName(u"checkBox_73")
        sizePolicy.setHeightForWidth(self.checkBox_73.sizePolicy().hasHeightForWidth())
        self.checkBox_73.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_73, 1, 6, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_23, 8, 0, 1, 1)

        self.checkBox_74 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_74.setObjectName(u"checkBox_74")
        sizePolicy.setHeightForWidth(self.checkBox_74.sizePolicy().hasHeightForWidth())
        self.checkBox_74.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_74, 1, 2, 1, 1)

        self.checkBox_75 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_75.setObjectName(u"checkBox_75")
        sizePolicy.setHeightForWidth(self.checkBox_75.sizePolicy().hasHeightForWidth())
        self.checkBox_75.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_75, 6, 4, 1, 1)

        self.checkBox_76 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_76.setObjectName(u"checkBox_76")
        sizePolicy.setHeightForWidth(self.checkBox_76.sizePolicy().hasHeightForWidth())
        self.checkBox_76.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_76, 7, 6, 1, 1)

        self.checkBox_77 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_77.setObjectName(u"checkBox_77")
        sizePolicy.setHeightForWidth(self.checkBox_77.sizePolicy().hasHeightForWidth())
        self.checkBox_77.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_77, 8, 3, 1, 1)

        self.checkBox_78 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_78.setObjectName(u"checkBox_78")
        sizePolicy.setHeightForWidth(self.checkBox_78.sizePolicy().hasHeightForWidth())
        self.checkBox_78.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_78, 4, 7, 1, 1)

        self.checkBox_79 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_79.setObjectName(u"checkBox_79")
        sizePolicy.setHeightForWidth(self.checkBox_79.sizePolicy().hasHeightForWidth())
        self.checkBox_79.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_79, 3, 2, 1, 1)

        self.checkBox_80 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_80.setObjectName(u"checkBox_80")
        sizePolicy.setHeightForWidth(self.checkBox_80.sizePolicy().hasHeightForWidth())
        self.checkBox_80.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_80, 4, 3, 1, 1)

        self.checkBox_81 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_81.setObjectName(u"checkBox_81")
        sizePolicy.setHeightForWidth(self.checkBox_81.sizePolicy().hasHeightForWidth())
        self.checkBox_81.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_81, 7, 1, 1, 1)

        self.checkBox_82 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_82.setObjectName(u"checkBox_82")
        sizePolicy.setHeightForWidth(self.checkBox_82.sizePolicy().hasHeightForWidth())
        self.checkBox_82.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_82, 8, 1, 1, 1)

        self.checkBox_83 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_83.setObjectName(u"checkBox_83")
        sizePolicy.setHeightForWidth(self.checkBox_83.sizePolicy().hasHeightForWidth())
        self.checkBox_83.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_83, 3, 5, 1, 1)

        self.checkBox_84 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_84.setObjectName(u"checkBox_84")
        sizePolicy.setHeightForWidth(self.checkBox_84.sizePolicy().hasHeightForWidth())
        self.checkBox_84.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_84, 7, 2, 1, 1)

        self.checkBox_85 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_85.setObjectName(u"checkBox_85")
        sizePolicy.setHeightForWidth(self.checkBox_85.sizePolicy().hasHeightForWidth())
        self.checkBox_85.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_85, 4, 4, 1, 1)

        self.checkBox_86 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_86.setObjectName(u"checkBox_86")
        sizePolicy.setHeightForWidth(self.checkBox_86.sizePolicy().hasHeightForWidth())
        self.checkBox_86.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_86, 2, 3, 1, 1)

        self.checkBox_87 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_87.setObjectName(u"checkBox_87")
        sizePolicy.setHeightForWidth(self.checkBox_87.sizePolicy().hasHeightForWidth())
        self.checkBox_87.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_87, 4, 6, 1, 1)

        self.checkBox_88 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_88.setObjectName(u"checkBox_88")
        sizePolicy.setHeightForWidth(self.checkBox_88.sizePolicy().hasHeightForWidth())
        self.checkBox_88.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_88, 4, 5, 1, 1)

        self.checkBox_89 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_89.setObjectName(u"checkBox_89")
        sizePolicy.setHeightForWidth(self.checkBox_89.sizePolicy().hasHeightForWidth())
        self.checkBox_89.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_89, 5, 7, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.checkBox_90 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_90.setObjectName(u"checkBox_90")
        sizePolicy.setHeightForWidth(self.checkBox_90.sizePolicy().hasHeightForWidth())
        self.checkBox_90.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_90, 1, 7, 1, 1)

        self.checkBox_91 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_91.setObjectName(u"checkBox_91")
        sizePolicy.setHeightForWidth(self.checkBox_91.sizePolicy().hasHeightForWidth())
        self.checkBox_91.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_91, 2, 4, 1, 1)

        self.checkBox_92 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_92.setObjectName(u"checkBox_92")
        sizePolicy.setHeightForWidth(self.checkBox_92.sizePolicy().hasHeightForWidth())
        self.checkBox_92.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_92, 2, 2, 1, 1)

        self.checkBox_93 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_93.setObjectName(u"checkBox_93")
        sizePolicy.setHeightForWidth(self.checkBox_93.sizePolicy().hasHeightForWidth())
        self.checkBox_93.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_93, 2, 8, 1, 1)

        self.checkBox_94 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_94.setObjectName(u"checkBox_94")
        sizePolicy.setHeightForWidth(self.checkBox_94.sizePolicy().hasHeightForWidth())
        self.checkBox_94.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_94, 3, 1, 1, 1)

        self.checkBox_95 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_95.setObjectName(u"checkBox_95")
        sizePolicy.setHeightForWidth(self.checkBox_95.sizePolicy().hasHeightForWidth())
        self.checkBox_95.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_95, 3, 7, 1, 1)

        self.checkBox_96 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_96.setObjectName(u"checkBox_96")
        sizePolicy.setHeightForWidth(self.checkBox_96.sizePolicy().hasHeightForWidth())
        self.checkBox_96.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_96, 5, 3, 1, 1)

        self.checkBox_97 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_97.setObjectName(u"checkBox_97")
        sizePolicy.setHeightForWidth(self.checkBox_97.sizePolicy().hasHeightForWidth())
        self.checkBox_97.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_97, 7, 3, 1, 1)

        self.checkBox_98 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_98.setObjectName(u"checkBox_98")
        sizePolicy.setHeightForWidth(self.checkBox_98.sizePolicy().hasHeightForWidth())
        self.checkBox_98.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_98, 4, 2, 1, 1)

        self.checkBox_99 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_99.setObjectName(u"checkBox_99")
        sizePolicy.setHeightForWidth(self.checkBox_99.sizePolicy().hasHeightForWidth())
        self.checkBox_99.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_99, 7, 5, 1, 1)

        self.checkBox_100 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_100.setObjectName(u"checkBox_100")
        sizePolicy.setHeightForWidth(self.checkBox_100.sizePolicy().hasHeightForWidth())
        self.checkBox_100.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_100, 5, 8, 1, 1)

        self.checkBox_101 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_101.setObjectName(u"checkBox_101")
        sizePolicy.setHeightForWidth(self.checkBox_101.sizePolicy().hasHeightForWidth())
        self.checkBox_101.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_101, 6, 5, 1, 1)

        self.checkBox_102 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_102.setObjectName(u"checkBox_102")
        sizePolicy.setHeightForWidth(self.checkBox_102.sizePolicy().hasHeightForWidth())
        self.checkBox_102.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_102, 6, 1, 1, 1)

        self.checkBox_103 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_103.setObjectName(u"checkBox_103")
        sizePolicy.setHeightForWidth(self.checkBox_103.sizePolicy().hasHeightForWidth())
        self.checkBox_103.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_103, 8, 7, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_26, 7, 0, 1, 1)

        self.checkBox_104 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_104.setObjectName(u"checkBox_104")
        sizePolicy.setHeightForWidth(self.checkBox_104.sizePolicy().hasHeightForWidth())
        self.checkBox_104.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_104, 1, 5, 1, 1)

        self.checkBox_105 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_105.setObjectName(u"checkBox_105")
        sizePolicy.setHeightForWidth(self.checkBox_105.sizePolicy().hasHeightForWidth())
        self.checkBox_105.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_105, 8, 4, 1, 1)

        self.checkBox_106 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_106.setObjectName(u"checkBox_106")
        sizePolicy.setHeightForWidth(self.checkBox_106.sizePolicy().hasHeightForWidth())
        self.checkBox_106.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_106, 5, 5, 1, 1)

        self.checkBox_107 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_107.setObjectName(u"checkBox_107")
        sizePolicy.setHeightForWidth(self.checkBox_107.sizePolicy().hasHeightForWidth())
        self.checkBox_107.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_107, 4, 8, 1, 1)

        self.checkBox_108 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_108.setObjectName(u"checkBox_108")
        sizePolicy.setHeightForWidth(self.checkBox_108.sizePolicy().hasHeightForWidth())
        self.checkBox_108.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_108, 8, 8, 1, 1)

        self.checkBox_109 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_109.setObjectName(u"checkBox_109")
        sizePolicy.setHeightForWidth(self.checkBox_109.sizePolicy().hasHeightForWidth())
        self.checkBox_109.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_109, 5, 2, 1, 1)

        self.checkBox_110 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_110.setObjectName(u"checkBox_110")
        sizePolicy.setHeightForWidth(self.checkBox_110.sizePolicy().hasHeightForWidth())
        self.checkBox_110.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_110, 5, 6, 1, 1)

        self.checkBox_111 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_111.setObjectName(u"checkBox_111")
        sizePolicy.setHeightForWidth(self.checkBox_111.sizePolicy().hasHeightForWidth())
        self.checkBox_111.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_111, 6, 7, 1, 1)

        self.checkBox_112 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_112.setObjectName(u"checkBox_112")
        sizePolicy.setHeightForWidth(self.checkBox_112.sizePolicy().hasHeightForWidth())
        self.checkBox_112.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_112, 8, 2, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_27, 6, 0, 1, 1)

        self.checkBox_113 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_113.setObjectName(u"checkBox_113")
        sizePolicy.setHeightForWidth(self.checkBox_113.sizePolicy().hasHeightForWidth())
        self.checkBox_113.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_113, 1, 1, 1, 1)

        self.checkBox_114 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_114.setObjectName(u"checkBox_114")
        sizePolicy.setHeightForWidth(self.checkBox_114.sizePolicy().hasHeightForWidth())
        self.checkBox_114.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_114, 7, 8, 1, 1)

        self.checkBox_115 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_115.setObjectName(u"checkBox_115")
        sizePolicy.setHeightForWidth(self.checkBox_115.sizePolicy().hasHeightForWidth())
        self.checkBox_115.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_115, 6, 8, 1, 1)

        self.checkBox_116 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_116.setObjectName(u"checkBox_116")
        sizePolicy.setHeightForWidth(self.checkBox_116.sizePolicy().hasHeightForWidth())
        self.checkBox_116.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_116, 6, 2, 1, 1)

        self.checkBox_117 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_117.setObjectName(u"checkBox_117")
        sizePolicy.setHeightForWidth(self.checkBox_117.sizePolicy().hasHeightForWidth())
        self.checkBox_117.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_117, 1, 3, 1, 1)

        self.checkBox_118 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_118.setObjectName(u"checkBox_118")
        sizePolicy.setHeightForWidth(self.checkBox_118.sizePolicy().hasHeightForWidth())
        self.checkBox_118.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_118, 8, 6, 1, 1)

        self.checkBox_119 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_119.setObjectName(u"checkBox_119")
        sizePolicy.setHeightForWidth(self.checkBox_119.sizePolicy().hasHeightForWidth())
        self.checkBox_119.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_119, 3, 3, 1, 1)

        self.checkBox_120 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_120.setObjectName(u"checkBox_120")
        sizePolicy.setHeightForWidth(self.checkBox_120.sizePolicy().hasHeightForWidth())
        self.checkBox_120.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_120, 1, 8, 1, 1)

        self.checkBox_121 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_121.setObjectName(u"checkBox_121")
        sizePolicy.setHeightForWidth(self.checkBox_121.sizePolicy().hasHeightForWidth())
        self.checkBox_121.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_121, 3, 6, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_28, 2, 0, 1, 1)

        self.checkBox_122 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_122.setObjectName(u"checkBox_122")
        sizePolicy.setHeightForWidth(self.checkBox_122.sizePolicy().hasHeightForWidth())
        self.checkBox_122.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_122, 5, 4, 1, 1)

        self.checkBox_123 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_123.setObjectName(u"checkBox_123")
        sizePolicy.setHeightForWidth(self.checkBox_123.sizePolicy().hasHeightForWidth())
        self.checkBox_123.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_123, 7, 7, 1, 1)

        self.checkBox_124 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_124.setObjectName(u"checkBox_124")
        sizePolicy.setHeightForWidth(self.checkBox_124.sizePolicy().hasHeightForWidth())
        self.checkBox_124.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_124, 1, 4, 1, 1)

        self.checkBox_125 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_125.setObjectName(u"checkBox_125")
        sizePolicy.setHeightForWidth(self.checkBox_125.sizePolicy().hasHeightForWidth())
        self.checkBox_125.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_125, 7, 4, 1, 1)

        self.checkBox_126 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_126.setObjectName(u"checkBox_126")
        sizePolicy.setHeightForWidth(self.checkBox_126.sizePolicy().hasHeightForWidth())
        self.checkBox_126.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_126, 2, 6, 1, 1)

        self.checkBox_127 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_127.setObjectName(u"checkBox_127")
        sizePolicy.setHeightForWidth(self.checkBox_127.sizePolicy().hasHeightForWidth())
        self.checkBox_127.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_127, 2, 7, 1, 1)

        self.checkBox_128 = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_128.setObjectName(u"checkBox_128")
        sizePolicy.setHeightForWidth(self.checkBox_128.sizePolicy().hasHeightForWidth())
        self.checkBox_128.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.checkBox_128, 8, 5, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_29, 0, 1, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_30, 0, 2, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_31, 0, 3, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_32, 0, 4, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_33, 0, 5, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_34, 0, 6, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_35, 0, 7, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_36, 0, 8, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.setupButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.setupButton.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.checkBox_12.setText("")
        self.checkBox_20.setText("")
        self.checkBox_49.setText("")
        self.checkBox_25.setText("")
        self.checkBox_3.setText("")
        self.checkBox_13.setText("")
        self.checkBox_45.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.checkBox_29.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.checkBox_8.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.checkBox_2.setText("")
        self.checkBox_42.setText("")
        self.checkBox_55.setText("")
        self.checkBox_60.setText("")
        self.checkBox_36.setText("")
        self.checkBox_4.setText("")
        self.checkBox_31.setText("")
        self.checkBox_15.setText("")
        self.checkBox_16.setText("")
        self.checkBox_30.setText("")
        self.checkBox_52.setText("")
        self.checkBox_33.setText("")
        self.checkBox_24.setText("")
        self.checkBox_38.setText("")
        self.checkBox_35.setText("")
        self.checkBox_46.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.checkBox_9.setText("")
        self.checkBox_27.setText("")
        self.checkBox_22.setText("")
        self.checkBox_23.setText("")
        self.checkBox_11.setText("")
        self.checkBox_17.setText("")
        self.checkBox_34.setText("")
        self.checkBox_48.setText("")
        self.checkBox_19.setText("")
        self.checkBox_50.setText("")
        self.checkBox_44.setText("")
        self.checkBox_47.setText("")
        self.checkBox_14.setText("")
        self.checkBox_63.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.checkBox_7.setText("")
        self.checkBox_56.setText("")
        self.checkBox_41.setText("")
        self.checkBox_32.setText("")
        self.checkBox_64.setText("")
        self.checkBox_37.setText("")
        self.checkBox_43.setText("")
        self.checkBox_51.setText("")
        self.checkBox_62.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.checkBox.setText("")
        self.checkBox_59.setText("")
        self.checkBox_54.setText("")
        self.checkBox_40.setText("")
        self.checkBox_5.setText("")
        self.checkBox_58.setText("")
        self.checkBox_18.setText("")
        self.checkBox_10.setText("")
        self.checkBox_28.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.checkBox_39.setText("")
        self.checkBox_57.setText("")
        self.checkBox_6.setText("")
        self.checkBox_53.setText("")
        self.checkBox_21.setText("")
        self.checkBox_26.setText("")
        self.checkBox_61.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"INPUTS", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"C\n"
"H\n"
"A\n"
"N\n"
"N\n"
"E\n"
"L\n"
"S", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"C\n"
"H\n"
"A\n"
"N\n"
"N\n"
"E\n"
"L\n"
"S", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"OUTPUTS", None))
        self.checkBox_65.setText("")
        self.checkBox_66.setText("")
        self.checkBox_67.setText("")
        self.checkBox_68.setText("")
        self.checkBox_69.setText("")
        self.checkBox_70.setText("")
        self.checkBox_71.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.checkBox_72.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.checkBox_73.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.checkBox_74.setText("")
        self.checkBox_75.setText("")
        self.checkBox_76.setText("")
        self.checkBox_77.setText("")
        self.checkBox_78.setText("")
        self.checkBox_79.setText("")
        self.checkBox_80.setText("")
        self.checkBox_81.setText("")
        self.checkBox_82.setText("")
        self.checkBox_83.setText("")
        self.checkBox_84.setText("")
        self.checkBox_85.setText("")
        self.checkBox_86.setText("")
        self.checkBox_87.setText("")
        self.checkBox_88.setText("")
        self.checkBox_89.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.checkBox_90.setText("")
        self.checkBox_91.setText("")
        self.checkBox_92.setText("")
        self.checkBox_93.setText("")
        self.checkBox_94.setText("")
        self.checkBox_95.setText("")
        self.checkBox_96.setText("")
        self.checkBox_97.setText("")
        self.checkBox_98.setText("")
        self.checkBox_99.setText("")
        self.checkBox_100.setText("")
        self.checkBox_101.setText("")
        self.checkBox_102.setText("")
        self.checkBox_103.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.checkBox_104.setText("")
        self.checkBox_105.setText("")
        self.checkBox_106.setText("")
        self.checkBox_107.setText("")
        self.checkBox_108.setText("")
        self.checkBox_109.setText("")
        self.checkBox_110.setText("")
        self.checkBox_111.setText("")
        self.checkBox_112.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.checkBox_113.setText("")
        self.checkBox_114.setText("")
        self.checkBox_115.setText("")
        self.checkBox_116.setText("")
        self.checkBox_117.setText("")
        self.checkBox_118.setText("")
        self.checkBox_119.setText("")
        self.checkBox_120.setText("")
        self.checkBox_121.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.checkBox_122.setText("")
        self.checkBox_123.setText("")
        self.checkBox_124.setText("")
        self.checkBox_125.setText("")
        self.checkBox_126.setText("")
        self.checkBox_127.setText("")
        self.checkBox_128.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"8", None))
    # retranslateUi

