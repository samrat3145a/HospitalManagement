
# Hospital Management System




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
