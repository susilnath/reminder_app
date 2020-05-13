import sys

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets, uic

if __name__ == '__main__':
    sched = BackgroundScheduler()

    app = QtWidgets.QApplication(sys.argv)
    
    window = uic.loadUi("main.ui")
    window.show()
    app.exec()