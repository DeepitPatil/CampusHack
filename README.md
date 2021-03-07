# Moodle Notifications
<img src="icon.png" align="right" width="100" height="100">

We noticed that moodle does not have a notification system to notify the user whenever a new file or quiz has been uploaded on moodle by the instructor. So, we implemented our own notification system for moodle using web scraping. The user will receive a notification whenever an instructor has uploaded a new file/quiz. Our application also sends a daily e-mail digest to the user's e-mail id. This e-mail digest will contain all the activities that happened in moodle on that day, along with the corresponding links for better accessibility.
<br/>
## Note: Run main.py
<br/>

## Table of Contents  
 - [User Login](#user-login)  
 - [Notifications](#notifications)
 - [Daily Digest](#daily-digest)  
 - [Future References](#future-features)

<br/>
<a name="user-login"/>

## User Login
On starting the code, a form is shown which askes the user their moodle username, password and email id.

<br/>
<img src="screenshots/ui.png" width="636" height="429"> 
<br/>
<a name="notifications"/>
<br/><br/>

## Notifications

Whenever a new file is added to the user's moodle account, the user receives a notification on their screen.
<br/><br/>
<img src="screenshots/notification.png" width="483" height="182">
<br/>
<a name="mail"/>
<br/><br/><br/>
## Daily Digest
At the end of the day(between 8 and 9 pm), the user receives a mail containing all the files added on that day along with the links in a digested format.
<br/><br/>
<img src="screenshots/mail2.png" > <br/>
<img src="screenshots/mail.png" width="536" height="336"> 
<br/>
<a name="future-references"/>

<br/><br/>
## Future Features

 - Getting access to moodle API and making a moodle plugin.
 - Making a mobile version.
 - Include  chats from contacts.
 - Making the application more memory and time efficient
