import sys
import ui
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5 import QtWidgets

def Rem_fin(text):
    print("hello")
    window.label.setText(text)

def Add_Rem():
    sched.add_job(Rem_fin, trigger='date', run_date= datetime(2020,5,14,0,0,0) , args=['text'])

if __name__ == '__main__':
    sched = BackgroundScheduler()
    
    app = QtWidgets.QApplication(sys.argv)

    window = ui.Ui()
    

    sched.start()

    Add_Rem()

    app.exec_()
