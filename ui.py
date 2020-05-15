from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate,QTime

class Ui(QtWidgets.QMainWindow):

    

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        # self.PenJobList 

        self.Add = self.findChild(QtWidgets.QPushButton, 'Button_Add')
        self.Delete = self.findChild(QtWidgets.QPushButton, 'Button_Delete')    

        self.datetime = self.findChild(QtWidgets.QDateTimeEdit, 'DateTime_Picker')
        
        self.label = self.findChild(QtWidgets.QLabel, 'debug')  

        self.RemTitle = self.findChild(QtWidgets.QLineEdit, 'Text_Title')
        self.RemContent = self.findChild(QtWidgets.QLineEdit, 'Text_Content')

        self.PenJobList = self.findChild(QtWidgets.QListWidget, 'ListW_PendingJobs')
        self.HstJobList = self.findChild(QtWidgets.QListWidget, 'ListW_HistoryJobs')

        self.datetime.setMinimumDate(QDate.currentDate())       #you can't bring back the dead
        self.datetime.setMinimumTime(QTime.currentTime())       #you can't bring back the dead :)
        self.datetime.setDisplayFormat('yyyy-MM-dd hh:mm:ss')

        self.show()

    def Update_List(self, Item_list):

        self.PenJobList.clear()

        for item in Item_list:
            self.PenJobList.addItem(item.name)

