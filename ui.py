from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate,QTime

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'Add_reminder')
        self.label = self.findChild(QtWidgets.QLabel, 'debug')
        self.datetime=self.findChild(QtWidgets.QDateTimeEdit,'DateTime_Picker')
        self.remtext=self.findChild(QtWidgets.QDateTimeEdit,'rem_text')
        self.datetime.setMinimumDate(QDate.currentDate())       #you can't bring back the dead
        self.datetime.setMinimumTime(QTime.currentTime())       #you can't bring back the dead :)
        self.datetime.setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        # self.button.clicked.connect(self.printButtonPressed)

        self.show()

#     def ButtonPressed(self):
#         self.label.setText(str(self.datetime.dateTime().toString()))
