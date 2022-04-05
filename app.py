#!bin/env python3
# Author(s): cryptopal85
# Version history: April 05 2022 - Initialising main structure
#                                - building authentication - preparing routing and html templates
#
#
# Remarks: app.py is a main block that will be used routing the requests such as
# viewing, sharing, uploading files, etc. to appropriate URLs.
# End-user facing requests, including input forms will mostly done within relevant html templates.

import re
from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file, current_app
from markupsafe import escape
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from os import environ, path
# from . import db, getconnectiondata, newdburi - will uncomment once it's completed
# from . models import DataUser, User, DataGroup - will uncomment once models are completed
import io
# other custom functions and module classes
# placeholder will be listed here


app = Blueprint('app.py', __name__)



########## Authentication ##########


# Landing page for unauthenticated users, login block shown here
@app.route('/')
def index():
	return render_template('index.html')

# This is the traditional home page for the authenticated users
# It will validate login and will route to the other variant of the same page once authentication confirmed.
# The second variant of the same page then will also list authorised groups (group membership) and logged user details.
# Failed authentication will redirect to the unauthenticated users landing page (index.html)
# Flask has a built-in method called login_required where protects access to routes that including login_required.
# This method is one of the other safeguard that mitigates major part of the OWASP broken authentication threats.
#
# Flask-login get_id returns the authenticated individual's numeric ID
# which can be used to extract attributes from classes like DataUser, User, etc. (needs to be clarified)

@app.route('/home')
@login_required
def presenthome():
	print("inside presenthome")
	if current_user.is_authenticated:
		uid=current_user.get_id()
		thisdatauser=DataUser.query.filter_by(userid=uid).first()
	if thisdatauser:
		dname=thisdatauser.userdisplayname
		azglist=thisdatauser.authgroups
		if azglist is None:
			azglist="No group membership found"
	return render_template('home-logged.html', displayname=dname, grouplist=azglist)


