import sys
import ui

from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5 import QtWidgets

if __name__ == '__main__':
    sched = BackgroundScheduler()
    
    app = QtWidgets.QApplication(sys.argv)

    window = ui.Ui()
    
    app.exec_()
