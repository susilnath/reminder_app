# Imports
import sys
import dateutil.parser
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from PyQt5 import QtWidgets
from PyQt5.Qt import Qt, QVariant

from ui import Ui

import history

# Reminder Functions

def Rem_fin(text,Title):
    MyUI.label.setText(Title+"\n\n"+text)
    MyUI.Update_List(sched.get_jobs())
    history.save(Title)

def call_hist():
    history.show(MyUI)

def clear_hist():
    history.clear()
    history.show(MyUI)

def Add_Rem(Title, date_time,content):
    sched.add_job(name= Title, trigger= 'date', run_date= date_time, func= Rem_fin, args=[content,Title])
    
    MyUI.Update_List(sched.get_jobs())

def Delete_Rem(Job_Id):
    sched.remove_job()

# UI Handlers1

def Add_button_Pressed():
    try:
        #Add_Rem(Title= MyUI.RemTitle.text(), date_time= str(datetime.fromisoformat(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss')))))
        Add_Rem(Title= MyUI.RemTitle.text(),date_time=dateutil.parser.isoparse(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss'))),content=MyUI.RemContent.text())
        MyUI.label.setText(str(MyUI.datetime.dateTime().toString('yyyy-MM-dd hh:mm:ss')))  
    except:
        print("Empty String Found!!!")
 

def Delete_Button_Clicked():
    Items = MyUI.PenJobList.selectedItems()
    
    joblist = sched.get_jobs()

    for item in Items:
        job_id = QVariant(item.data(Qt.UserRole)).value()
        sched.remove_job(job_id)

    MyUI.Update_List(sched.get_jobs())


# Main Function
if __name__ == '__main__':
    sched = BackgroundScheduler()                   # initialize scheduler
    sched.add_jobstore('sqlalchemy',url= 'sqlite:///jobstore.db')

    app = QtWidgets.QApplication(sys.argv)          # Define QT app

    MyUI = Ui()                                     # Initialize UI
    MyUI.Add.clicked.connect(Add_button_Pressed)    # Connect Push Button to Handler
    MyUI.Delete.clicked.connect(Delete_Button_Clicked)
    MyUI.clear.clicked.connect(clear_hist)
    MyUI.tab.currentChanged.connect(call_hist)

    sched.start()

    MyUI.Update_List(sched.get_jobs())

    # MyUI.PenJobList.addItem("Item 1")
    # MyUI.PenJobList.addItem("Item 2")
    # MyUI.PenJobList.addItem("Item 3")
    # MyUI.PenJobList.addItem("Item 4")

    app.exec_()
