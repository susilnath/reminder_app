def save(text):
    f=open('hist.db','a+')

    f.writelines(text+"\n")
    f.close()

def clear():
    f=open('hist.db','w').close()

def show(ui):
    f=open('hist.db','r')
    ui.HstJobList.clear()
    for line in f:
        ui.HstJobList.addItem(line.strip("\n"))
