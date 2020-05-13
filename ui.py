from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'Add_reminder')
        self.label = self.findChild(QtWidgets.QLabel, 'debug')
        self.datetime=self.findChild(QtWidgets.QDateTimeEdit,'DateTime_Picker')

        # self.button.clicked.connect(self.printButtonPressed)

        self.show()

#     def ButtonPressed(self):
#         self.label.setText(str(self.datetime.dateTime().toString()))
