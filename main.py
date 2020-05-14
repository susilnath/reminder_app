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
    rem_date,rem_time=MyUI.dateparser()             #get date and time from Ui
    print("Date:"+str(rem_date))
    print("Time:"+str(rem_time))
    Add_Rem(datetime(int(rem_date[0]),int(rem_date[1]),int(rem_date[2]),int(rem_time[0]),int(rem_time[1]),int(rem_time[2])))

# Main Function
if __name__ == '__main__':
    sched = BackgroundScheduler()                   # initialize scheduler
    
    app = QtWidgets.QApplication(sys.argv)          # Define QT app
    
    MyUI = Ui()                                     # Initialize UI
    MyUI.button.clicked.connect(ButtonPressed)      # Connect Push Button to Handler

    sched.start()

    app.exec_()
