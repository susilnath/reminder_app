from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate,QTime

class Ui(QtWidgets.QMainWindow):

    

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        # self.joblist 

        self.button = self.findChild(QtWidgets.QPushButton, 'Add_reminder')
        self.label = self.findChild(QtWidgets.QLabel, 'debug')
        self.datetime = self.findChild(QtWidgets.QDateTimeEdit, 'DateTime_Picker')
        self.RemTitle = self.findChild(QtWidgets.QLineEdit, 'Reminder_Title')
        self.joblist = self.findChild(QtWidgets.QListWidget, 'Job_List')

        self.datetime.setMinimumDate(QDate.currentDate())       #you can't bring back the dead
        self.datetime.setMinimumTime(QTime.currentTime())       #you can't bring back the dead :)
        self.datetime.setDisplayFormat('yyyy-MM-dd hh:mm:ss')

        self.show()

    def Update_List(self, Item_list):

        self.joblist.clear()

        for item in Item_list:
            self.joblist.addItem(item.name)

