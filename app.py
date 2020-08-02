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

# Connect to Cloudinary
CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

# Session Key
SESSION_KEY = os.environ.get('SESSION_KEY')
app.secret_key = SESSION_KEY

# Homepage (open access)


@app.route('/')
def index():
    vol_listings = db.volunteer_prog.find().limit(1)
    event_count = db.volunteer_register.count()
    activity_count = db.volunteer_prog.count()
    org_count = db.users.count()
    donations = db.donations.aggregate([ {
        "$group": {
            "_id": "_id",
            "totalDonations": {
                "$sum": "$donor_amount"
            }
        }
    }])
    return render_template('index.html', vol_listings=vol_listings,
                           event_count=event_count, activity_count=activity_count,
                           org_count=org_count, donations=donations)

# Event list (open access)


@app.route('/volunteer')
def show_events():
    vol_listings = db.volunteer_prog.find()
    return render_template('events.html', vol_listings=vol_listings)

# Individual Event (open access)


@app.route('/volunteer/signup/<activity_id>')
def show_activity_details(activity_id):
    vol = db.volunteer_prog.find_one({
        "_id": ObjectId(activity_id)
    })
    return render_template('event_signup.html', vol=vol)


@app.route('/volunteer/signup/<activity_id>', methods=['POST'])
def process_activity_volunteer(activity_id):
    vol_name = request.form.get('vol_name')
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
    flash("Thank you for registering, we will contact you should you be shortlisted for the event!")
    return redirect(url_for('show_events'))

# Participating organisations (open access)


@app.route('/organisations')
def show_organisations():
    users = db.users.find()
    return render_template('organisations.html', users=users)

# Make donations page (open access)


@app.route('/donate')
def show_donate_form():
    return render_template('make_donation.html')


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
    flash(
        f"Thank you for donating ${donor_amount} to us! Once we have received the donation, we'll send an email confirmation and invoice to you.")
    return redirect(url_for('index'))


from user import routes
from functools import wraps

# Login/Register Pages


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html', cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


# Setting up login function


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
    event = db.volunteer_prog.find_one({
        "_id": ObjectId(activity_id)
    })

    all_users = db.users.find()

    return render_template('update_event.html', event=event, all_users=all_users,
                           cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/volunteer/update/<activity_id>', methods=['POST'])
@login_required
def process_update_event(activity_id):
    prog_name = request.form.get('prog_name')
    prog_desc = request.form.get('prog_desc')
    prog_org = request.form.get('prog_org')
    duration = request.form.get('duration')
    num_volunteer_req = request.form.get('num_volunteer_req')
    prog_date = request.form.get('prog_date')
    uploaded_file_url = request.form.get('uploaded_file_url')

    db.volunteer_prog.update_one({
        "_id": ObjectId(activity_id)
    }, {
        "$set": {
            "prog_name": prog_name,
            "prog_desc": prog_desc,
            "prog_org": prog_org,
            "duration": duration,
            "num_volunteer_req": num_volunteer_req,
            "prog_date": prog_date,
            'uploaded_file_url': uploaded_file_url
        }
    })
    flash(f'The event has been updated!')
    return redirect(url_for('dashboard'))

# Delete event


@app.route('/volunteer/delete/<activity_id>')
@login_required
def delete_event(activity_id):
    vol = db.volunteer_prog.find_one({
        "_id": ObjectId(activity_id)
    })

    return render_template('confirm_delete_event.html', vol=vol)


@app.route('/volunteer/delete/<activity_id>', methods=['POST'])
@login_required
def process_delete_event(activity_id):
    db.volunteer_prog.remove({
        "_id": ObjectId(activity_id)
    })
    flash(f'You have successfully removed the event!')
    return redirect(url_for('dashboard'))

# Create event volunteer


@app.route('/volunteer/create')
@login_required
def create_event_form():
    all_users = db.users.find()
    return render_template('create_event.html', all_users=all_users,
                           cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/volunteer/create', methods=['POST'])
@login_required
def create_volunteer():
    prog_name = request.form.get('prog_name')
    prog_desc = request.form.get('prog_desc')
    prog_org = request.form.get('prog_org')
    duration = request.form.get('duration')
    num_volunteer_req = request.form.get('num_volunteer_req')
    prog_date = request.form.get('prog_date')
    uploaded_file_url = request.form.get('uploaded_file_url')
    db.volunteer_prog.insert_one({
        'prog_name': prog_name,
        'prog_date': datetime.datetime.strptime(prog_date, "%Y-%m-%d"),
        'prog_desc': prog_desc,
        'duration': duration,
        'num_volunteer_req': num_volunteer_req,
        'prog_org': prog_org,
        'uploaded_file_url': uploaded_file_url
    })
    return redirect(url_for('dashboard'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
