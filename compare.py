import os
#from notifypy import Notify

def notify(title, text):
     os.system("""
             osascript -e 'display notification "{}" with title "{}" '""".format(text, title))

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
        notify("Moodle File Added", s)
        

def compare(file1,file2):
    tree1=file1.readlines()[1:]
    tree2=file2.readlines()[1:]
    added=[]
    for i in tree1:
        if i not in tree2:
            added.append(i)
    display(added)

curr = open("curr.txt","r")
prev = open("prev.txt","r")
compare(curr,prev)


