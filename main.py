import sys
from PyQt5 import QtWidgets,QtCore,QtGui,uic
from PyQt5.Qt import QApplication, QLabel, QWidget
from PyQt5.QtCore import QRunnable,QThreadPool,pyqtSignal,QObject
import sys,time,traceback
import schedule

def job():
    print("Schedule Working")

schedule.every().seconds.do(job)
for i in range(10):
    print(str(i)+":",end='')
    schedule.run_pending()
    time.sleep(1)
