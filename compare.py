import os
from plyer import notification
import time
#from notifypy import Notify

# def notify(title, text):
#      os.system("""
#              osascript -e 'display alert "{}" with title "{}" '""".format(text, title))

# def sendNotification(title, text):
#     notification = Notify()
#     notification.title = title
#     notification.message = text
#     notification.icon = os.getcwd()+"/icon.png"
#     notification.send()

def display(lines):
    for line in lines:
        l = line.split("{$£þ}")
        s = l[0]+" was added in "+l[2]
        notification.notify(title="Moodle File Added", message=s,timeout=2, app_icon=r"icon.ico")
        time.sleep(1)
        

def compare(file1,file2,lst):
    tree1=file1.readlines()[1:]
    tree2=file2.readlines()[1:]
    added=[]
    for i in tree1:
        if i not in tree2:
            added.append(i)
            l = i.split("{$£þ}")
            lst.append(l[0]+" was added in "+l[2][:-1]+".\nLink: "+l[1]+".")
    display(added)