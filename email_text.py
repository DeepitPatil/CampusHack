import smtplib

def sendmail(mail,notifs):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("moodlenotifications123@gmail.com", "hackathon")
    s="Your Moodle Daily Digest\n\n"
    for i in notifs:
        s+=i+"\n\n"
    server.sendmail("moodlenotifications123@gmail.com", mail, s)
    server.quit()