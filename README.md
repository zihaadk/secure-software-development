# University of Essex - MSc CyberSecurity - Secure Software Development Module - March 2022

## Introduction ##

An application was developed for securely exchanging data between the ISS (International Space Station) and the ground centre staff. The application is written in Python 3.10.3 and provides the following functionalities:

* User Registration and Login
* File Search & Download
* File Upload
* File Share

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
* gunicorn 20.1.0

## Code Structure ##

The code structure is as follows:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/codestructure.png)

`app.py` - This is the main application used to route searching, sharing, uploading and downloading requests to the appropriate URL's. Front end forms are displayed using html templates obtained from Bulma (2022).

`authentication.py` - This code is required for authenticating end users as well as perform input validations. When a user's password is entered during the registration process it is encrypted using the werkzeug.security module and stored in a MySQL database with the corresponding user id. Screenshot below:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/dbs1.png)

## User Registration ##

Files named ***usermanagementutil.py*** and ***makeissdesuser.py*** are used to register users to the system. It is assumed that the CLI will be used to perform user registration. The code is executed as follows: `python3 makeissdesuser.py` and produces the following output:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/userreg.png)

Users are created and placed into Authgroups allowing only users within an Authgroup to share files with each other. In the case where a user's profile has been hacked, the attacker would not gain access to files uploaded from other users, minimising the attack surface. The following Authorisation Groups are used:

Auth Group    | Country
------------- | -------------
14            | Europe
11            | USA
19            | Canada
15            | Japan
12            | Russia

Once completed the user will be required to save thier AccessID and Password. These credentials will be used to login to the application.

## Main Application ##

The main application is executed by running: `flask run` and produces the following output:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/flaskoutput.png)

Once successful, the application will be accessible from the web browser on: `http://127.0.0.1:8080`

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/issdesui.png)

## Discussion - Design & Coding Differences ##


## Functional Testing Images ##




## References ##

Bulma (2022) Bulma: the modern CSS framework that just works. Available from: https://bulma.io/ [Accessed 29 March 2022].













![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/nova.png)
