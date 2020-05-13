import sys
from PyQt5 import QtWidgets,QtCore,QtGui,uic
from PyQt5.Qt import QApplication, QLabel, QWidget
from PyQt5.QtCore import QRunnable,QThreadPool,pyqtSignal,QObject
import sys,time,traceback
import schedule

class store:
    rem=[]
    tim=[]

def job():
    print("Schedule Working")


schedule.every().seconds.do(job)

def add_rem():
    #rem1.rem.append(input("Enter a Reminder:"))
    #rem1.tim.append(input("Enter "))
    print("Check Hello")
if __name__=="__main__":
    rem1=store
    add_rem()
    print(rem1.rem)

for i in range(10):
    schedule.run_pending()
    time.sleep(1)