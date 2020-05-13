import sys
from PyQt5 import QtWidgets,QtCore,QtGui,uic
from PyQt5.Qt import QApplication, QLabel, QWidget
from PyQt5.QtCore import QRunnable,QThreadPool,pyqtSignal,QObject
import sys,time,traceback
import schedule

class store:
    
def job():
    print("Schedule Working")

def scheduler():
    schedule.every().seconds.do(job)

def add_rem():
    rem1.append(input("Enter a Reminder:"))

