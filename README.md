# Secure Software Development
MSc Cybersecurity - Secure Software Development Module - March 2022

## Introduction ##

An Application is required for securely exchanging data between the ISS (International Space Station) and the ground centre staff. The application is written in Python 3.10.3 and provides the following functionalities:

### User Registration

Files named ***usermanagementutil.py*** and ***makeissdesuser.py*** are used to register users to the system. It is assumed that the CLI will be used to perform user registration. The code is executed as follows: `python3 makeissdesuser.py` and produces the following output:

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/userreg.png)



1. Differences between Design Document & Final Code
2. How to Execute Code
3. 

Users are created and places into Authgroups allowing only users within an Authgroup to share files with each other. In the case where a user's profile has been hacked, the attacker would not gain access to files uploaded from other users, minizing the attack surface.

![This is an image](https://github.com/zihaadk/secure-software-development/blob/main/images/nova.png)
