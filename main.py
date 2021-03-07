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
from tkinter import simpledialog
import smtplib
from email_text import sendmail
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import os
from ui import ui

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

ui()
info = open("user_info.txt", "r")
lines = info.readlines()
username = lines[0][:-1]
password = lines[1][:-1]
email = lines[2]
while(not exists(username, password)):
    ui()
    info = open("user_info.txt", "r")
    lines = info.readlines()
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



