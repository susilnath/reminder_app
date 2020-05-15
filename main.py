# Imports
import sys
# import dateutil.parser
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets

from ui import Ui

# Reminder Functions

def Rem_fin(text):
    MyUI.label.setText(text)
    MyUI.Update_List(sched.get_jobs())

def Add_Rem(Title, date_time):
    sched.add_job(name= Title, trigger= 'date', run_date= date_time, func= Rem_fin, args= ['finished'])
    
    MyUI.Update_List(sched.get_jobs())

# UI Handlers1

def ButtonPressed():
    Add_Rem(Title= MyUI.RemTitle.text(), date_time= str(datetime.fromisoformat(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss')))))
    # Add_Rem(dateutil.parser.isoparse(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss'))))
    
    MyUI.label.setText(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss')))   

# Main Function
if __name__ == '__main__':
    sched = BackgroundScheduler()                   # initialize scheduler
    sched.add_jobstore('sqlalchemy',url= 'sqlite:///jobstore.db')

    app = QtWidgets.QApplication(sys.argv)          # Define QT app

    MyUI = Ui()                                     # Initialize UI
    MyUI.Add.clicked.connect(ButtonPressed)    # Connect Push Button to Handler
    
    sched.start()
    sched.print_jobs()

    MyUI.Update_List(sched.get_jobs())

    app.exec_()
