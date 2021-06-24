
# Hospital Management System

This blood test management application aims at helping people for their better health.  Lab tests are a swift and easy way to take control of your health. The time has evolved in such a word where everyone wants every service at its doorstep with total convenient and secure. keeping in mind the present scenario. So to resolve one of our major issues that is going out for blood test is main concern because “Health is our first priority” and if we can get that with our home comfort then nothing can be best than that. None of the easiest ways to check your health is with a drop of blood. The basic blood tests performed at doctor’s offices and wellness fairs play a big role in managing our health and preventing common diseases like diabetes and heart disease. Monitoring your inner health can be challenging. But not with “MedCheck” App – Your Inner Health Buddy. You can know how healthy you are with our “MedCheck” app.


## Features

- User Registration
- Hospital Registration
- Dynamic Search for Hospital
- Hot Modules
- Slot Booking

  
## Installation 

Installing Xampp

- Install Xampp (Download Link) -> https://sourceforge.net/projects/xampp/

Installing all the dependencies :

```bash 
   pip install django, mysqlclient
```
- Open Xampp Control Panel
- Turn on Apache and Mysql in Xampp
- Go to project directory and open a terminal

- Create a database name "Hospital_Management" (You can change this name in settings.py)

```bash 
  python manage.py migrate 
  python manage.py runserver
```

- If any error shows up run the following commands :

```bash 
   python manage.py drop
   python manage.py sqlflush
```
