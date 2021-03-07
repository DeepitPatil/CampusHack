from get_from_moodle import main
from compare import compare
import os
import shutil
import getpass
import tkinter as tk
from tkinter import simpledialog
import smtplib
from email_text import sendmail
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import os

userName=password=email=window=None
def login():
    username = userName.get()
    Pass = password.get()
    em = email.get()
    with open("user_info.txt","w") as file:
        file.write(username+"\n"+Pass+"\n"+em)
    global window
    window.destroy()

def ui():
    global userName
    global password
    global email
    global window
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

    window.mainloop()