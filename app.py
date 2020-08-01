from flask import Flask, render_template, request, redirect, url_for, flash, session
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

load_dotenv()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect Mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.tgc_project3

# Session Key
SESSION_KEY = os.environ.get('SESSION_KEY')
app.secret_key = SESSION_KEY

# Homepage (open access)
@app.route('/')
def index():
    vol_listings = db.volunteer_prog.find().limit(1)
    return render_template('index.template.html', vol_listings=vol_listings)

# Event list (open access)
@app.route('/volunteer')
def show_volunteer():
    vol_listings = db.volunteer_prog.find()
    return render_template('volunteer.template.html', vol_listings=vol_listings)

# Individual Event (open access)
@app.route('/volunteer/signup/<activity_id>')
def show_activity_details(activity_id):
    vol = db.volunteer_prog.find_one({
        "_id": ObjectId(activity_id)
    })
    return render_template('activity_signup.html', vol=vol)

@app.route('/volunteer/details/<activity_id>', methods=['POST'])
def process_activity_volunteer(activity_id):
    vol_name= request.form.get('vol_name')
    vol_dob = request.form.get('vol_dob')
    vol_email = request.form.get('vol_email')
    vol_phone = request.form.get('vol_phone')
    vol_desc = request.form.get('vol_desc')
    vol_activity = activity_id
    db.volunteer_register.insert_one({
    'vol_name': vol_name,
    'vol_dob': datetime.datetime.strptime(vol_dob, "%Y-%m-%d"),
    'vol_desc': vol_desc,
    'vol_email': vol_email,
    'vol_activity': vol_activity,
    'vol_phone': vol_phone
    })
    flash(f'You have registered for the event!')
    return render_template('volunteer.template.html')

# Participating organisations (open access)
@app.route('/organisations')
def show_organisations():
    users = db.users.find()
    return render_template('organisations.template.html', users=users)

# Make donations page (open access)
@app.route('/donate')
def show_donate_form():
    return render_template('make_donation.template.html')

@app.route('/donate', methods=['POST'])
def donate_form():
    donor_name = request.form.get('donor_name')
    donor_dob = request.form.get('donor_dob')
    donor_email = request.form.get('donor_email')
    donor_amount = request.form.get('donor_amount')
    donor_phone = request.form.get('donor_phone')
    payment_method = request.form.get('payment_method')
    donor_memo = request.form.get('donor_message')

    db.donation.insert_one({
    'donor_name': donor_name,
    'donor_dob': datetime.datetime.strptime(donor_dob, "%Y-%m-%d"),
    'donor_email': donor_email,
    'donor_phone': donor_phone,
    'donor_amount': donor_amount,
    'payment_method': payment_method,
    'donor_memo': donor_memo
    })
    flash(f'Thank you for donating {donor_amount} to us!')
    return render_template('index.template.html')

# Login/Register Pages
@app.route('/login')
def login_page():
    return render_template('login.template.html')

@app.route('/register')
def register_page():
    return render_template('signup.template.html')

# Setting up login function
from functools import wraps
from user import routes

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login')
    return wrap

# Events dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    vol_listings = db.volunteer_prog.find()
    return render_template('events_dashboard.html', vol_listings=vol_listings)

# Update event
@app.route('/volunteer/update/<activity_id>')
@login_required
def update_event(activity_id):
    vol = db.volunteer_prog.find_one({
        "_id": ObjectId(activity_id)
    })
    return render_template('activity_signup_edit.html', vol=vol)

@app.route('/volunteer/update/<activity_id>', methods=['POST'])
@login_required
def process_update_event(activity_id):
    prog_name = request.form.get('prog_name')
    prog_desc = request.form.get('prog_desc')
    prog_org = request.form.get('prog_org')
    duration = request.form.get('duration')
    num_volunteer_req = request.form.get('num_volunteer_req')
    prog_date = request.form.get('prog_date')

    db.volunteer_prog.update_one({
        "_id": ObjectId(activity_id)
    }, {
        "$set": {
            "prog_name": prog_name,
            "prog_desc": prog_desc,
            "prog_org": prog_org,
            "duration": duration,
            "num_volunteer_req": num_volunteer_req,
            "prog_date": prog_date
        }
    })
    return render_template('events_dashboard.html')


# Create event volunteer
@app.route('/volunteer/create')
@login_required
def create_volunteer_form():
    all_users = db.users.find()
    return render_template('create_volunteer.template.html', all_users=all_users)

@app.route('/volunteer/create', methods=['POST'])
@login_required
def create_volunteer():
    prog_name = request.form.get('prog_name')
    prog_desc = request.form.get('prog_desc')
    prog_org = request.form.get('prog_org')
    duration = request.form.get('duration')
    num_volunteer_req = request.form.get('num_volunteer_req')
    prog_date = request.form.get('prog_date')
    db.volunteer_prog.insert_one({
        'prog_name': prog_name,
        'prog_date': datetime.datetime.strptime(prog_date, "%Y-%m-%d"),
        'prog_desc': prog_desc,
        'duration': duration,
        'num_volunteer_req': num_volunteer_req,
        'prog_org': prog_org
    })
    flash(f'Your event has been created!')
    return render_template('events_dashboard.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)