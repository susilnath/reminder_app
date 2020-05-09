import sys
from PyQt5 import QtWidgets,QtCore,QtGui,uic
from PyQt5.Qt import QApplication, QLabel, QWidget
from PyQt5.QtCore import QRunnable,QThreadPool
import sys,time

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)

class WorkerSignals(QObject):
    

class rems():
    rem=[]
    tim=[]
    curr_pos=len(rem)
    length=len(rem)
    first_save=0

def test():
    myapp.label.setText("Checked!!!")
    myapp.textEdit.setEnabled(True)
    myapp.textEdit.setText("")

def save():
    rem=myapp.textEdit.toPlainText()
    tim=myapp.timer.value()
    rem1.rem.append(str(rem))
    rem1.tim.append(tim)
    myapp.textEdit.setText("")
    rem1.length=len(rem1.rem)
    rem1.curr_pos=len(rem1.rem)-1
    myapp.timer.setValue(0)
    myapp.textEdit.setEnabled(False)
    print(rem1.rem)
    print(rem1.tim)

def prev():
    if rem1.length>=1:
        print("Current pos:"+str(rem1.curr_pos))
        if rem1.curr_pos > 0:
            rem1.curr_pos=rem1.curr_pos-1
        pos=rem1.curr_pos
        myapp.textEdit.setText(str(rem1.rem[pos]))
        myapp.timer.setValue(rem1.tim[pos])

def nxt():
    if rem1.length>=1:
        print("Current pos:"+str(rem1.curr_pos))
        if rem1.curr_pos < rem1.length-1:
            rem1.curr_pos=rem1.curr_pos+1
        pos=rem1.curr_pos
        myapp.textEdit.setText(str(rem1.rem[pos]))
        myapp.timer.setValue(rem1.tim[pos])

def delete():
    print(rem1.rem)
    if rem1.length > 0:
        pos=rem1.curr_pos
        rem1.rem.pop(pos)
        rem1.tim.pop(pos)
        rem1.length=len(rem1.rem)
        rem1.curr_pos=len(rem1.rem)-1
    myapp.textEdit.setText("[Deleted]")
    myapp.timer.setValue(0)
    
def tim_inc():
    if rem1.length>0:
        for i in range(rem1.length):
            print("Looping through")
            if rem1.tim[i]==0:
                myapp.label.setText("Remainder!!!!")
                continue
            rem1.tim[i]=rem1.tim[i]-1
        time.sleep(1)

if __name__=="__main__":
    app = QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
 
    myapp = uic.loadUi("C:/Users/Black Hound/Documents/Visual Code Projects/.vscode/Forge/Rem/main.ui")
    myapp.setWindowTitle("QThread Application")
    myapp.setWindowOpacity(1)
    myapp.setMinimumWidth(resolution.width() / 3)
    myapp.setMinimumHeight(resolution.height() / 1.5)
    myapp.move(resolution.center() - myapp.rect().center())
    style_main="QWidget {"
    style_main+="background-color: rgba(0,41,59,255);}"
    style_main+="QScrollBar:horizontal {width: 1px;height: 1px;"
    style_main+="background-color: rgba(0,41,59,255);}"
    style_main+="QScrollBar:vertical {width: 1px;"
    style_main+="height: 1px;"
    style_main+="background-color: rgba(0,41,59,255);}"
    myapp.setStyleSheet(style_main)
    myapp.pushButton.setStyleSheet("margin: 1px; padding: 20px;background- color: rgba(1,255,255,100);color: rgba(0,190,255,255);border-style: solid;border-radius: 3px;border-width: 0.5px;border-color: rgba(127,127,255,255);")
    myapp.pushButton.clicked.connect(test)
    myapp.textEdit.setEnabled(False)
    myapp.save_btn.clicked.connect(save)
    myapp.prev.clicked.connect(prev)
    myapp.nxt.clicked.connect(nxt)
    myapp.del_btn.clicked.connect(delete)
    myapp.show()
    rem1=rems
    app.exec_()
    print("App started")
#threadpool=QThreadPool()
#print("Multithreading with maximum %d threads" % threadpool.maxThreadCount())
#worker=Worker()
#threadpool.start(worker)