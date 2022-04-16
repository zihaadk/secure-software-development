# Secure Software Development
MSc Cybersecurity - Secure Software Development Module - March 2022

## Introduction ##

An Application is required for securely exchanging data between the ISS (International Space Station) and the ground centre staff. The application is written in Python 3.10.3 and provides the following functionalities:

### Pre-Requisites

The following pre-requisites are required to successfully run the code:

* Python 3.10.3
* MySQL Database - a script called ***issdes.sql*** is provided to create the database schema using Querious (https://www.araelium.com/support/querious/download-previous-versions)
 
The following python libraries are required:

* Flask 2.1.1
* Flask-Login 0.60
* Flask-SQLAlchemy 2.5.1
* mysql-connector-python 8.0.28
* Werkzeug 2.1.1
* MarkupSafe 2.1.1
* Python-dotenv 0.20.0
* 
 

### User Registration

Files named ***usermanagementutil.py*** and ***makeissdesuser.py*** are used to register users to the system. It is assumed that the CLI will be used to perform user registration. The code is executed as follows: `python3 makeissdesuser.py` and produces the following output:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/userreg.png)

Once completed the user will be required to save thier AccessID and password.

## Main Application ##

The main application is executed by running: `flask run` and produces the following output:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/flaskoutput.png)

thereafter the application is accessible from the web browser on: `http://127.0.0.1:8080`

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/issdesui.png)













1. Differences between Design Document & Final Code
2. How to Execute Code
3. 

Users are created and places into Authgroups allowing only users within an Authgroup to share files with each other. In the case where a user's profile has been hacked, the attacker would not gain access to files uploaded from other users, minizing the attack surface. the following Authorisation Groups are used:

Auth Group    | Country
------------- | -------------
14            | Europe
11            | USA
19            | Canada
15            | Japan
12            | Russia



![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/nova.png)
