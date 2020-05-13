import sys

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'Add_reminder')
        self.label = self.findChild(QtWidgets.QLabel, 'debug')

        self.button.clicked.connect(self.printButtonPressed)

        self.show()

    def printButtonPressed(self):
        self.label.setText("Working")

if __name__ == '__main__':
    sched = BackgroundScheduler()
    
    app = QtWidgets.QApplication(sys.argv)


    window = Ui()
    
    app.exec_()
