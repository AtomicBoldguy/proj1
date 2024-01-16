from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QScreen, QGuiApplication
import sys
import time
import subprocess

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1920, 1080)
        Form.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/img/endcall.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.9)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background: no-repeat url(\'endcall.png\');background-color:#000; background-position:center;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
 

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(281, 218)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background:rgba(0,0,0,1);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        # MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background:rgba(0,0,0,1)")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 221, 81))
        self.label.setStyleSheet("color:white;font-weight:bold;font-size:85px;background:none;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 160, 41, 31))
        self.spinBox.setStyleSheet("font-size:18px; font-weight:bold;border: 2px solid white;color:white;border-radius:5px;background:transparent;")
        self.spinBox.setObjectName("spinBox")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 90, 51))
        self.pushButton.setStyleSheet("font-size:25px;color:white; font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('СТАРТ')
        
        self.pushButton1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(150, 100, 90, 51))
        self.pushButton1.setStyleSheet("font-size:23px;color:white; font-weight:bold; border:3px solid white;border-radius:5px;background:none;display:none;")
        self.pushButton1.setDefault(False)
        self.pushButton1.setFlat(False)
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setText('ПАУЗА')

        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 160, 41, 31))
        self.spinBox_2.setStyleSheet("font-size:18px; font-weight:bold;border: 2px solid white;color:white;border-radius:5px;background:transparent;")
        self.spinBox_2.setObjectName("spinBox_2")

        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(190, 160, 50, 31))
        self.spinBox_3.setStyleSheet("font-size:18px;color:white; font-weight:bold;border: 2px solid white;border-radius:5px;background:transparent;")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(10)

        MainWindow.setCentralWidget(self.centralwidget)

        screen = QGuiApplication.primaryScreen()
        geometry = screen.geometry()
        screen_size = geometry.size()
        MainWindow.move(screen_size.width() - MainWindow.width(), screen_size.height() - MainWindow.height() - 40)

        self.timer = QtCore.QTimer()

        
        self.remaining_time = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update_timer)
        # self.timer.start(1000)

        minutes = self.spinBox_3.value()
        self.spinBox.setValue(minutes)
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds

        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

        self.spinBox_3.valueChanged.connect(self.change_def_time)

        self.pushButton.clicked.connect(self.start_timer)

        self.pushButton1.setStyleSheet("font-size:23px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
        self.pushButton1.blockSignals(True)

        Form.show()


    #     Form.keyPressEvent = self.handle_key_press

    # def handle_key_press(self, event):
    #     if event.key() == Qt.Key.Key_Alt:
    #         print('zazazazazzazazzazaz')

    #         Form.hide()

        # self.pushButton1.clicked.connect(self.pause_timer)
    def start_timer(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setStyleSheet("color:white;font-weight:bold;font-size:85px;background:none;")
        # self.timer1 = QtCore.QTimer()

        self.pushButton1.setStyleSheet("font-size:23px;color:white; font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton1.blockSignals(False)

        self.pushButton.setText('СБРОС')

        self.pushButton.setStyleSheet("font-size:20px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
        self.pushButton.blockSignals(True)

        minutes = self.spinBox.value()
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

        self.spinBox.setDisabled(True)
        self.spinBox_2.setDisabled(True)
        self.spinBox_3.setDisabled(True)
        
  
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        # self.pushButton.clicked.connect(self.stop1_timer)

    def stop_timer(self):
        _translate = QtCore.QCoreApplication.translate
        # self.timer = QtCore.QTimer()

        self.pushButton.setStyleSheet("font-size:25px;color:white;font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton.blockSignals(False)
        self.pushButton.clicked.connect(self.start_timer)

        self.pushButton1.setStyleSheet("font-size:23px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
        self.pushButton1.blockSignals(True)
        
        self.pushButton1.setText('ПАУЗА')
        self.pushButton.setText('СТАРТ')

        self.spinBox.setValue(self.spinBox_3.value())
        self.spinBox_2.setValue(0)

        self.spinBox.setDisabled(False)
        self.spinBox_2.setDisabled(False)
        self.spinBox_3.setDisabled(False)

        minutes = self.spinBox.value()
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds
        # self.remaining_time = minutes * 60 + seconds
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))
        # del self.timer

        # self.timer = QtCore.QTimer()
        self.timer.stop()
        # self.timer1.stop()

    # def stop1_timer(self):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.timer = QtCore.QTimer()

    #     self.pushButton.setText('СТАРТ')

    #     self.pushButton1.setStyleSheet("font-size:25px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
    #     self.pushButton1.blockSignals(True)

    #     minutes = self.label.text()
    #     seconds = self.remaining_time % 60

    #     self.timer.stop()

    #     self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

    #     self.pushButton.clicked.connect(self.start_timer)

    def update_timer(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton1.setStyleSheet("font-size:23px;color:white;font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton1.setText('ПАУЗА')
        self.pushButton1.clicked.connect(self.pause_timer)
        self.remaining_time -= 1
        if self.remaining_time >= 0:
            if self.remaining_time < 10:
                self.label.setStyleSheet("color:red;font-weight:bold;font-size:85px;background:none;")
            self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))
        else:
            # self.open_fullscreen_window()
            subprocess.run(["taskkill", "/f", "/im", "MicroSIP.exe"])
            subprocess.run(["taskkill", "/f", "/im", "Telegram.exe"])
            subprocess.run(["taskkill", "/f", "/im", "Viber.exe"])
            subprocess.run(["taskkill", "/f", "/im", "Skype.exe"])
            self.timer.stop() 

            self.pushButton.setStyleSheet("font-size:25px;color:white;font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
            self.pushButton.blockSignals(False)
            self.pushButton.clicked.connect(self.start_timer)

            self.pushButton.setText('СТАРТ')

            # Form = QtWidgets.QWidget()
            # ui = Ui_Form()
            # ui.setupUi(Form)
            Form.show()
            MainWindow.keyPressEvent = self.handle_key_press

    def handle_key_press(self, event):
        _translate = QtCore.QCoreApplication.translate
        
        if event.key() == Qt.Key.Key_Alt:
            self.label.setStyleSheet("color:white;font-weight:bold;font-size:85px;background:none;")
            self.pushButton.setText('СТАРТ')
            self.pushButton1.blockSignals(False)

            self.pushButton1.setStyleSheet("font-size:25px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
            self.pushButton1.blockSignals(True)

            self.spinBox.setDisabled(False)
            self.spinBox_2.setDisabled(False)
            self.spinBox_3.setDisabled(False)
            
            self.spinBox.setValue(self.spinBox_3.value())
            self.spinBox_2.setValue(0)
            minutes = self.spinBox_3.value()
            seconds = 0
            self.remaining_time = minutes * 60 + seconds
            self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))
            self.pushButton.clicked.connect(self.start_timer)

            Form.close()
            
            # self.end_microsip_call() 

    # def open_fullscreen_window(self):
    #     fullscreen_window = FullScreenWindow()
    #     fullscreen_window.showFullScreen()
    def pause_timer(self):
        _translate = QtCore.QCoreApplication.translate

        print(self.label.text())
        
        # self.remaining_time = int(self.label.text())
        self.pushButton1.setText('СТАРТ')
        self.label.setText(_translate("MainWindow", f"{self.label.text()}"))

        self.pushButton.setStyleSheet("font-size:20px;color:white;font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton.blockSignals(False)
        self.pushButton.setText('СБРОС')

        self.spinBox.setValue(int(self.label.text()[0:2]))
        self.spinBox_2.setValue(int(self.label.text()[3:5]))

        self.spinBox.valueChanged.connect(self.add_time_min)
        self.spinBox_2.valueChanged.connect(self.add_time_min)

        self.spinBox.setDisabled(False)
        self.spinBox_2.setDisabled(False)
        self.spinBox_3.setDisabled(False)

        # del self.timer

        # self.remaining_time = minutes * 60 + seconds
        # self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

        self.timer.stop()

 
        # self.remaining_time = int(self.label.text())
        self.pushButton.clicked.connect(self.stop_timer)

        self.pushButton1.clicked.connect(self.unpause_timer)

    def add_time_min(self):
        _translate = QtCore.QCoreApplication.translate
        minutes = self.spinBox.value()
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds
        self.spinBox.setValue(minutes)
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))
    

    
    def unpause_timer(self):
        _translate = QtCore.QCoreApplication.translate


        self.pushButton1.setText('ПАУЗА')
        self.pushButton1.setStyleSheet("font-size:23px;color:white;font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton1.clicked.connect(self.pause_timer)

        self.pushButton.setStyleSheet("font-size:20px;color:grey;font-weight:bold; border:3px solid grey;border-radius:5px;background:none;")
        self.pushButton.blockSignals(True)

        minutes = int(self.label.text()[0:2])
        seconds = int(self.label.text()[3:5])
        self.remaining_time = minutes * 60 + seconds
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

        self.spinBox.setDisabled(True)
        self.spinBox_2.setDisabled(True)
        self.spinBox_3.setDisabled(True)

        # self.pushButton.clicked.connect(self.stop_timer)  
     
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.update_timer)
        # self.timer.start(1000)
        # self.pushButton.clicked.connect(self.stop1_timer)

    def change_def_time(self):
        _translate = QtCore.QCoreApplication.translate
        minutes = self.spinBox_3.value()
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds
        self.spinBox.setValue(minutes)
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))

    def end_microsip_call():
        subprocess.run(["taskkill", "/f", "/im", "MicroSIP.exe"])
        subprocess.run(["taskkill", "/f", "/im", "Telegram.exe"])
        subprocess.run(["taskkill", "/f", "/im", "Viber.exe"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FcknTimer"))
                
        # self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.pushButton1.setStyleSheet("font-size:23px;color:white; font-weight:bold; border:3px solid white;border-radius:5px;background:none;")
        self.pushButton1.blockSignals(False)
        # self.timer.start(1000)

        minutes = self.spinBox.value()
        seconds = self.spinBox_2.value()
        self.remaining_time = minutes * 60 + seconds
    
        # self.remaining_time = 10  
        # self.timer.start(1000)  
    
        self.label.setText(_translate("MainWindow", f"{self.remaining_time // 60:02d}:{self.remaining_time % 60:02d}"))




if __name__ == "__main__":  

    import sys

    app1 = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui1 = Ui_Form()
    ui1.setupUi(Form)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    Form.hide()
         
    sys.exit(app.exec())
