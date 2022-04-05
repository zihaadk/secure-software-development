#!bin/env python3
# Author(s): cryptopal85
# Version history: April 05 2022 - Initialising main structure
#                                - building authentication - preparing routing and html templates
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


##### Authentication #####


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
	print("inside present home")
	if current_user.is_authenticated:
		uid = current_user.get_id()
		thisdatauser = DataUser.query.filter_by(userid=uid).first()
	if thisdatauser:
		dname = thisdatauser.userdisplayname
		asglist = thisdatauser.authgroups
		if asglist is None:
			asglist = "No group membership found"
	return render_template('home-logged.html', displayname=dname, grouplist=asglist)


##### File Operations #####

# The app's search and download functionality handled here
# It will be the main block for authorised users when interacting with files
# Several file types will be presented to users
# Users will able to carry certain operations like downloading, sharing, deleting, etc.


@app.route('/search-download-1', methods=['GET'])
@login_required
def presentview():
	print("inside present view")
	if current_user.is_authenticated:
		uid = current_user.get_id()
		thisdatauser = DataUser.query.filter_by(userid=uid).first()
	if thisdatauser:
		asglist = thisdatauser.authgroups
		duaid = thisdatauser.useraccessid
		if asglist is None:
			flash("The user {} is not member of any authorised groups. Please contact the ISS ground centre to get support".format(duaid))
			asglist = "** No group membership **"
	return render_template('search.html', grouplist=asglist, aid=duaid)

	
@app.route('/search-download-1', methods=['POST'])
@login_required
def presentview2():
	print("inside present view2")
	if current_user.is_authenticated:
		uid = current_user.get_id()
		thisdatauser = DataUser.query.filter_by(userid=uid).first()
	if thisdatauser:
		thisaid = thisdatauser.useraccessid
		asglist = thisdatauser.authgroups
		if asglist is None:
			flash("The user {} is not member of any authorised groups. Please contact the ISS ground centre to get support").format(thisaid)
			duserfilegroups = ['122', '124']  # a workaround for users with no membership
		else:
			duserfilegroups = getauthsfg(asglist)
		# Use the authorisation-based function on the SQL userid and groups
		# Update SQL based on search queries
		sftype = request.form.get('selectedfiletype')
		sfname = request.form.get('filename')
		skeytag = request.form.get('keyword-tag')
		authsfilesql = getauthsfilesql(uid, duserfilegroups, sftype, sfname, skeytag)
		if len(sfname) == 0:
			sfname = "any file name"
		if len(skeytag) == 0:
			skeytag = "any keywords"
		# we need to process the SQL produced above - initialise db connection
		dbcondata = getconnectiondata()
		resultslist = getauthsfiles(dbcondata, authsfilesql)
		if resultslist is not None and len(resultslist) > 0:
			# let's convert the tuples into a dictionary - what are the tuples? https://www.w3schools.com/python/python_tuples.asp
			authsdict = newresultsdict(resultslist)
		else:
			authsdict = dict()
			authsdict['00000000000000000000000000000000'] = "No files found for this search: {}".format(sftype)
	return render_template('view2.html', asfiledict=authsdict, aid=thisaid, grouplist=asglist, searchfname=sfname, searchkeytag=skeytag, searchtype=sftype)
	
	
	