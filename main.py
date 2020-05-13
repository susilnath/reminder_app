# Imports
import sys
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets

from ui import Ui

# Reminder Functions
def Rem_fin(text):
    MyUI.label.setText(text)

def Add_Rem(date_time):
    sched.add_job(Rem_fin, trigger='date', run_date= date_time , args=['finished'])

# UI Handlers
def ButtonPressed(self):
    MyUI.label.setText(str(MyUI.datetime.dateTime().toString()))
    Add_Rem(datetime(2020,5,14,0,43,0))

# Main Function
if __name__ == '__main__':
    sched = BackgroundScheduler()                   # initialize scheduler
    
    app = QtWidgets.QApplication(sys.argv)          # Define QT app
    
    MyUI = Ui()                                     # Initialize UI
    MyUI.button.clicked.connect(ButtonPressed)      # Connect Push Button to Handler

    sched.start()

    app.exec_()
