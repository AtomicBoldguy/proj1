# import time
# import subprocess

# def end_skype_call():
#     subprocess.run(["taskkill", "/f", "/im", "Skype.exe"])

# def end_telegram_call():
#     subprocess.run(["taskkill", "/f", "/im", "Telegram.exe"])

# def end_microsip_call():
#     subprocess.run(["taskkill", "/f", "/im", "MicroSIP.exe"])

# def end_whatsapp_call():
#     subprocess.run(["taskkill", "/f", "/im", "WhatsApp.exe"])

# def end_viber_call():
#     subprocess.run(["taskkill", "/f", "/im", "Viber.exe"])


# for i in range(10, -1, -1):
#     print(i)
#     time.sleep(1)

# end_skype_call()
# end_telegram_call()
# end_microsip_call()
# end_whatsapp_call()
# end_viber_call()

# https://www.geeksforgeeks.org/
# https://doc.qt.io/qtforpython-6/
# https://pythonpyqt.com/

# subprocess.Popen(
#                  ['C:\\Users\\User\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe',
#                   'callto:' + '+37529555555'])
# subprocess.Popen(
#                  ['C:\Users\User\AppData\Local\WhatsApp\WhatsApp.exe',
#                   'callto:' + '+37529555555'])
# subprocess.Popen(
#                  ['C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype.exe',
#                   'callto:' + '+37529555555'])
# subprocess.Popen(
#                  ['C:\Users\User\AppData\Local\Viber\Viber.exe',
#                   'callto:' + '+37529555555'])
# subprocess.Popen(
#                  ['C:\\Users\\User\\AppData\\Local\MicroSIP\\microsip.exe',
#                   'callto:' + '95555555'])
# time.sleep(20)
# end_microsip_call()

# importing libraries


from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 400, 600)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# variables
		# count variable
		self.count = 0

		# start flag
		self.start = False

		# creating push button to get time in seconds
		button = QPushButton("Set time(s)", self)

		# setting geometry to the push button
		button.setGeometry(125, 100, 150, 50)

		# adding action to the button
		button.clicked.connect(self.get_seconds)

		# creating label to show the seconds
		self.label = QLabel("//TIMER//", self)

		# setting geometry of label
		self.label.setGeometry(100, 200, 200, 50)

		# setting border to the label
		self.label.setStyleSheet("border : 3px solid black")

		# setting font to the label
		self.label.setFont(QFont('Times', 15))

		# setting alignment to the label
		# self.label.setAlignment(QtCore.AlignCenter)

		# creating start button
		start_button = QPushButton("Start", self)

		# setting geometry to the button
		start_button.setGeometry(125, 350, 150, 40)

		# adding action to the button
		start_button.clicked.connect(self.start_action)

		# creating pause button
		pause_button = QPushButton("Pause", self)

		# setting geometry to the button
		pause_button.setGeometry(125, 400, 150, 40)

		# adding action to the button
		pause_button.clicked.connect(self.pause_action)

		# creating reset button
		reset_button = QPushButton("Reset", self)

		# setting geometry to the button
		reset_button.setGeometry(125, 450, 150, 40)

		# adding action to the button
		reset_button.clicked.connect(self.reset_action)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.showTime)

		timer.start(1000)

	def showTime(self):
		# checking if flag is true
		if self.start:
			# incrementing the counter
			self.count -= 1

			# timer is completed
			if self.count == 0:
				# making flag false
				self.start = False
				# setting text to the label
				self.label.setText("Completed !!!! ")

		if self.start:
			# getting text from count
			text = str(self.count / 10) + " s"
			# showing text
			self.label.setText(text)


	# method called by the push button
	def get_seconds(self):

		# making flag false
		self.start = False
		# getting seconds and flag
		second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

		# if flag is true
		if done:
			# changing the value of count
			self.count = second * 10
			# setting text to the label
			self.label.setText(str(second))

	def start_action(self):
		# making flag true
		self.start = True
		# count = 0
		if self.count == 0:
			self.start = False

	def pause_action(self):
		# making flag false
		self.start = False

	def reset_action(self):
		# making flag false
		self.start = False
		# setting count value to 0
		self.count = 0

		# setting label text
		self.label.setText("//TIMER//")


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())

# ///


# import sys
# from PyQt6.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
# from PyQt6.QtCore import QTimer,QDateTime

# class WinForm(QWidget):
#     def __init__(self,parent=None):
#         super(WinForm, self).__init__(parent)
#         self.setWindowTitle('QTimer demonstration')

#         self.listFile=QListWidget()
#         self.label=QLabel('Label')
#         self.startBtn=QPushButton('Start')
#         self.endBtn=QPushButton('Stop')

#         layout=QGridLayout()

#         self.timer=QTimer()
#         self.timer.timeout.connect(self.showTime)

#         layout.addWidget(self.label,0,0,1,2)
#         layout.addWidget(self.startBtn,1,0)
#         layout.addWidget(self.endBtn,1,1)

#         self.startBtn.clicked.connect(self.startTimer)
#         self.endBtn.clicked.connect(self.endTimer)

#         self.setLayout(layout)

#     def showTime(self):
#         current_time=QDateTime.currentDateTime()
#         formatted_time=current_time.toString('yyyy-MM-dd hh:mm:ss dddd')
#         self.label.setText(formatted_time)

#     def startTimer(self):
#         self.timer.start(1000)
#         self.startBtn.setEnabled(False)
#         self.endBtn.setEnabled(True)

#     def endTimer(self):
#         self.timer.stop()
#         self.startBtn.setEnabled(True)
#         self.endBtn.setEnabled(False)

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     form=WinForm()
#     form.show()
#     sys.exit(app.exec())