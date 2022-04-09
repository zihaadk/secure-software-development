#!bin/env python3
# Author(s): cryptopal85
# Version history: April 09 2022 - Initialising main structure
#                                - https://flask.palletsprojects.com/en/2.1.x/appcontext/
#                                - https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
#
#

#####
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import environ, path
from flask_login import LoginManager
from datetime import timedelta
import mysql.connector
from mysql.connector import errorcode

# Monitoring requirements
import logging

db = SQLAlchemy()

# Load the environment file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

def getconnectiondata():
	condatalist =[]
	issdes = environ.get('dbinstance')
	username = environ.get('dbuser')
	cred = environ.get('dbcred')
	host = environ.get('dbhost')
	if not issdes:
		print("Incorrect or missing info: database instance name")
	else:
		condatalist.append(issdes)
	if not username:
		print("Incorrect or missing info: database user name")
	else:
		condatalist.append(username)
	if not cred:
		print("Incorrect or missing info: database credentials")
	else:
		condatalist.append(cred)
	if not host:
		print("Incorrect or missing info: database host information")
	else:
		condatalist.append(host)
	if len(condatalist) !=4:
		print("Incorrect or missing info")
		exit(1)
	else:
		return condatalist
	return False
	
def newdburi(connlist):
	user = connlist[1]
	pwd = connlist[2]
	host = connlist [3]
	dbinst = connlist [0]
	dburi = "mysql+mysqlconnector://{}:{}@{}:3306/{}".format(user, pwd, host, dbinst)
	return dburi
	
# Alternate connection driver to MySQL
def dbconnectalt(conlist):
	try:
		dbh = mysql.connector.connect(
			database = conlist[0],
			user = conlist[1],
			password = conlist[2],
			host = conlist[3],
		)
		return dbh
	except Exception as err:
		print(err)
		return None
		
def create_app():
	# getting environment variable to set database connection
	connlist = getconnectiondata()
	dburi = newdburi(connlist)
	
	app = Flask(__name__)
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_DATABASE_URI'] = dburi
	app.config['SQLALCHEMY_ECHO'] = False
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds = 900)
	
	# get secret key from env file
	app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
	
	logging.basicConfig(filename = '/var/tmp/issdes.log', level = logging.DEBUG)
	
	# enable SQLAlchemy
	db.init_app(app)
	# enable Flask_login LoginManager
	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)
	from .dbmodel import User
	from .dbmodel import DataUser
	# Authns database has the primary key User ID (for password hash & account status)
	
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
		
	# Import custom functions
	from .repetitives import getauthsfg, getauthsfiles, getauthsfilesql, newresultsdict, getfiledatasql, getmimetype, getfiledata, testuserstrps, testfileownersql, testfileownership, getgroupdetails, newsharedgroups
	
	with app.app_context():
		from .authentication import authentication as authentication_blueprint
		app.register_blueprint(authentication_blueprint)
		
		from .app import app as app_blueprint
		app.register_blueprint(app_blueprint)
		
		# app initialised
		return app