# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1st2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(281, 218)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(0.800000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background:rgba(0,0,0,0.5);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgba(0,0,0,0.5)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 221, 81))
        self.label.setStyleSheet(u"color:blue;font-weight:bold;font-size:85px;background:none;")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(40, 160, 41, 31))
        self.spinBox.setStyleSheet(u"font-size:18px; font-weight:bold;border: 2px solid blue;color:blue;border-radius:5px;background:transparent;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 100, 201, 51))
        self.pushButton.setStyleSheet(u"font-size:20px;color:darkblue; font-weight:bold; border:3px solid blue;border-radius:5px;background:none;")
        self.pushButton.setFlat(False)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(90, 160, 41, 31))
        self.spinBox_2.setStyleSheet(u"font-size:18px; font-weight:bold;border: 2px solid blue;color:blue;border-radius:5px;background:transparent;")
        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(190, 160, 51, 31))
        self.spinBox_3.setStyleSheet(u"font-size:18px;color:blue; font-weight:bold;border: 2px solid blue;border-radius:5px;background:transparent;;")
        self.spinBox_3.setValue(10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FcknTimer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422", None))
    # retranslateUi

