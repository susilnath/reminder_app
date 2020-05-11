import sys
from PyQt5 import QtWidgets,QtCore,QtGui,uic
from PyQt5.Qt import QApplication, QLabel, QWidget
from PyQt5.QtCore import QRunnable,QThreadPool,pyqtSignal,QObject
import sys,time,traceback

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)

class WorkerSignals(QObject):
    rem_state=pyqtSignal(str)
    error=pyqtSignal(tuple)

class Worker(QRunnable):
    def __init__(self,fn):
        super(Worker,self).__init__()
        self.fn=fn
        self.signals = WorkerSignals()
        self.remainder=[]
        self.timing=[]
        self.rem_safe=[]
        self.tim_safe=[]

    def run(self):
        try:
            s="received"
            while True:
                self.safe_guard()     
                time.sleep(1)
                self.timer()
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

    def update_rem(self,rem,tim):
        self.rem_safe=rem
        self.tim_safe=tim
    
    def safe_guard(self):
        self.remainder=self.rem_safe
        self.timing=self.tim_safe

    def timer(self):
        for i in range(len(self.remainder)):
            print("Looping through")
            if self.timing[i]==0:
                myapp.label.setText("Remainder!!!!")
                continue
            self.timing[i]=self.timing[i]-1


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
    worker.update_rem(rem1.rem,rem1.tim)
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
    worker.update_rem(rem1.rem,rem1.tim)

def checked(text):
    #print("Checking")
    s="hello"

if __name__=="__main__":
    app = QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
 
    myapp = uic.loadUi("main.ui")
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
    #myapp.indicator.setText("Enter Remainders :)")
    myapp.show()
    rem1=rems

    threadpool=QThreadPool()
    print("Multithreading with maximum %d threads" % threadpool.maxThreadCount())
    worker=Worker(checked)
    worker.signals.rem_state.connect(checked)
    threadpool.start(worker)

    app.exec_()
    print("App started")
