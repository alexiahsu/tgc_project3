from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
import bcrypt
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)

# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = "tgc_project3"

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# set the session key
app.secret_key = SESSION_KEY

# CRUD begins here

# Index

@app.route('/')
def index():
    return render_template('index.template.html')

# Login

@app.route('/login')
def login():
    return render_template('login.template.html')

# Register

@app.route('/register')
def register():
    return render_template('register.template.html')

# About us
@app.route('/about-us')
def about_us():
    return render_template('about_us.template.html')

#Participating Organisation List
@app.route('/organisations')
def show_organisations():
    return render_template('organisations.template.html')

# Activity details
@app.route('/details/<activity_id>')
def show_activity_details():
    return render_template('activity_details.template.html')

# Activity posted
@app.route('/posted/<activity_id>')
def show_activity_posted():
    return render_template('activity_posted.template.html')

# Activity Summary
@app.route('/posted/<activity_id>/summary')
def show_activity_summary():
    return render_template('activity_summary.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
