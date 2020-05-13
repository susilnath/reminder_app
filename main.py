import sys

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets, uic

def fun():
    window.debug.setText("Working")

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

if __name__ == '__main__':
    sched = BackgroundScheduler()
    
    window = Ui()
    window.Add_reminder.clicked.connect(fun)

    # window.Add_reminder
