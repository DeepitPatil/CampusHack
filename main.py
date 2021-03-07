#delete prev file
#rename curr file as prev file
#create curr file
#compare curr and prev files

from get_from_moodle import main
from compare import compare
import os
import shutil
import getpass
import tkinter as tk
import smtplib
from email_text import sendmail
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import os
from ui import *
import sys
from datetime import datetime
import time

def exists(username,password):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(os.getcwd()+"/chromedriver",options=chrome_options)

    driver.get("https://moodle.iitd.ac.in/login/index.php")

    ufield = driver.find_element_by_id("username")
    ufield.send_keys(username)
    pfield = driver.find_element_by_id("password")
    pfield.send_keys(password)
    captcha = driver.find_element_by_id("page-login-index").text.split("\n")[9].split()
    cfield = driver.find_element_by_id("valuepkg3")

    if "subtract" in captcha:
        captcha = str(int(captcha[-4])-int(captcha[-2]))
    elif "add" in captcha:
        captcha = str(int(captcha[-4])+int(captcha[-2]))
    elif "first" in captcha:
        captcha = captcha[-4]
    elif "second" in captcha:
        captcha = captcha[-2]

    cfield.send_keys(captcha)
    cfield.send_keys(Keys.RETURN)

    return (driver.current_url!="https://moodle.iitd.ac.in/login/index.php")

notifs=[]
prev=None

def login():
    username = userName.get()
    Pass = password.get()
    em = email.get()
    with open("user_info.txt","w") as file:
        file.write(username+"\n"+Pass+"\n"+em)
    time.sleep(5)

window = Tk()
window.geometry("800x500+300+100")
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Moodle Notifications")
window.iconbitmap(os.getcwd()+"/icon.png")
window.configure(background='orange')

label1 = Label(window, text = " Moodle Login Info ", fg = "white", bg="orange", font = ("new times roman", 40, "bold"))
label1.place(x = 230, y = 15)

label2 = Label(window, text = "Username :", fg = "black", bg="orange", font = ("arial", 16, "normal"))
label2.place(x = 190, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName,  width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", fg = "black", bg="orange", font = ("arial", 16, "normal"))
label3.place(x = 190, y = 200)

password = StringVar()
textBox2 = Entry(window, textvar = password, show="*", width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 200)

label4 = Label(window, text = "E-mail ID :", fg = "black", bg="orange", font = ("arial", 16, "normal"))
label4.place(x = 200, y = 250)

email = StringVar()
textBox3 = Entry(window, textvar = email, width = 30, font = ("arial", 16, "bold"))
textBox3.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "orange", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 370, y = 310)
#button2 = Button(window, text="Quit", command=window.destroy)
#button2.place(x = 450, y = 310)
window.mainloop()

info = open("user_info.txt", "r")
lines = info.readlines()
if(len(lines)==0 or lines[0]=="\n"):
    sys.exit()
username = lines[0][:-1]
password = lines[1][:-1]
email = lines[2]
while(not exists(username, password)):
    ui()
    info = open("user_info.txt", "r")
    lines = info.readlines()
    if(len(lines)==0 or lines[0]=="\n"):
        sys.exit()
    username = lines[0][:-1]
    password = lines[1][:-1]
    email = lines[2]
main(username, password)
while(True):
    os.system("rm -r prev.txt")
    os.rename("curr.txt", "prev.txt")
    main(username, password)
    curr = open("curr.txt", "r")
    prev = open("prev.txt", "r")
    compare(curr, prev, notifs)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time.split(":")[0] in ("20","21") and now.day!=prev and not notifs:
        prev=now.day
        sendmail(email,notifs)
        notifs=[]



