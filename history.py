def save(text):
    f=open('hist.db','a')

    f.writelines(text+"\n")
    f.close()

def clear():
    f=open('hist.db','w').close()