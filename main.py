import sys

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets, uic

def fun():
    window.debug.setText("Working")

if __name__ == '__main__':
    sched = BackgroundScheduler()

    app = QtWidgets.QApplication(sys.argv)
    
    window = uic.loadUi("main.ui")
    window.Add_reminder.clicked.connect(fun)
    window.show()
    app.exec()