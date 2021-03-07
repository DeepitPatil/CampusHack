#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import getpass
from Node import Node
import os
import datetime

def main(username, password):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(os.getcwd()+"/chromedriver",options=chrome_options)
    driver.get("https://moodle.iitd.ac.in/login/index.php")

    username_input = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id("username"))
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(password)

    login = driver.find_element_by_id("login")
    captcha = str(login.text).splitlines()[-2].split()

    captcha_answer = ""
    if captcha[1] != "enter" :
        a = int(captcha[2])
        b = int(captcha[4])
        solve = {"add" : a+b, "subtract" : a-b}
        captcha_answer = solve[captcha[1]]
    else :
        a = int(captcha[4])
        b = int(captcha[6])    
        solve = {"first" : a, "second" : b}
        captcha_answer = solve[captcha[2]]

    captcha_input = driver.find_element_by_id("valuepkg3")
    captcha_input.clear()
    captcha_input.send_keys(captcha_answer)

    loginbtn = driver.find_element_by_id("loginbtn")
    loginbtn.click()

    # Making the navigation tree
    pages = driver.find_elements_by_class_name("page-link")
    page_text = [p.text for p in pages]
    total_pages = 0
    while page_text[total_pages].strip() != "»":
        total_pages += 1
    total_pages -= 1
    #total_pages = len(driver.find_elements_by_class_name("page-link"))-2
    root = Node("root", None, None)
    myCourses = Node("My Courses", driver.current_url, root)
    #print("total pages", total_pages)
    for page in range(total_pages):
        driver.find_elements_by_class_name("page-link")[page+1].click()
        courses_elements = driver.find_elements_by_class_name("media-heading")
        courses_elements = [x for x in courses_elements if x.text]
        L = len(courses_elements)
        for i in range(L):
            courses_elements = driver.find_elements_by_class_name("media-heading")
            courses_elements = [x for x in courses_elements if x.text]
            C_name = courses_elements[i].text
            courses_elements[i].click()
            C_link = driver.current_url
            a = Node(C_name, C_link, myCourses)
            files_elements = driver.find_elements_by_css_selector(".activityinstance [href]")
            files_elements = [f for f in files_elements if f.text]
            l = len(files_elements)
            #print(l)
            for j in range(l):
                #files_elements = driver.find_elements_by_class_name("activityinstance")
                files_elements = driver.find_elements_by_css_selector(".activityinstance [href]")
                files_elements = [f for f in files_elements if f.text]
                F_name = files_elements[j].text
                F_link = files_elements[j].get_attribute("href")
                #F_link = driver.current_url
                d = Node(F_name, F_link, a)
                if(F_name == "Impartus" or F_name == "Gradescope"):
                    F_link = files_elements[j].click()
                    window_name = driver.window_handles[1]
                    driver.switch_to.window(window_name)
                    driver.close()
                    window_name = driver.window_handles[0]
                    driver.switch_to.window(window_name)
            driver.get(myCourses.getLink())
            driver.find_elements_by_class_name("page-link")[page+1].click()

    with open("curr.txt","w") as file:
        file.write(str(datetime.datetime.now())+"\n")
        root.save(file)


