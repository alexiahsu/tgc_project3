# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import pymongo
# from dotenv import load_dotenv
# from bson import ObjectId
# import os
# import datetime

# # load in the variables in the .env file into our operating system environment
# load_dotenv()

# app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# # connect to mongo
# MONGO_URI = os.environ.get('MONGO_URI')
# client = pymongo.MongoClient(MONGO_URI)

# # define my db_name
# DB_NAME = "tgc_project3"

# # read in the SESSION_KEY variable from the operating system environment
# SESSION_KEY = os.environ.get('SESSION_KEY')

# # set the session key
# app.secret_key = SESSION_KEY

# # CRUD begins here

# # Index

# @app.route('/')
# def index():
#     vol_listings = client[DB_NAME].volunteer_prog.find().limit(1)
#     return render_template('index.template.html', vol_listings=vol_listings)

# # Login

# @app.route('/login')
# def login():
#     return render_template('login.template.html')

# # Register page

# @app.route('/register')
# def register():
#     return render_template('register.template.html')

# # Register input
# @app.route('/register', methods=['POST'])
# def create_register():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     org_email = request.form.get('org_email')
#     org_name = request.form.get('org_name')
#     org_desc = request.form.get('org_desc')

#     client[DB_NAME].users.insert_one({
#         'username': username,
#         'password': password,
#         'org_email': org_email,
#         'org_name': org_name,
#         'org_desc': org_desc
#     })
#     flash(f'Thank you for registering with us!')
#     return render_template('login.template.html')

# # Participating Organisation List


# # Volunteer activities summary


# # Create volunteer activity
# @app.route('/volunteer/create')
# def create_volunteer_form():
#     users = client[DB_NAME].users.find_one()
#     return render_template('create_volunteer.template.html', users=users)

# @app.route('/volunteer/create', methods=['POST'])
# def create_volunteer():
#     prog_name = request.form.get('prog_name')
#     prog_desc = request.form.get('prog_desc')
#     prog_org = request.form.get('prog_org')
#     duration = request.form.get('duration')
#     num_volunteer_req = request.form.get('num_volunteer_req')
#     prog_date = request.form.get('prog_date')
#     client[DB_NAME].volunteer_prog.insert_one({
#         'prog_name': prog_name,
#         'prog_date': datetime.datetime.strptime(prog_date, "%Y-%m-%d"),
#         'prog_desc': prog_desc,
#         'duration': duration,
#         'num_volunteer_req': num_volunteer_req,
#         'prog_org': prog_org
#     })
#     flash(f'Your event has been created!')
#     return render_template('volunteer.template.html')

# # Update event
# @app.route('/volunteer/update/<activity_id>')
# def update_activity(activity_id):
#     activity = client[DB_NAME].volunteer_prog.find_one({
#         "_id": ObjectId
#     })
#     return render_template('update_activity.template.html', activity=activity)

# @app.route('/volunteer/update<activity_id>', methods=['POST'])
# def process_update_activity(activity_id):
#     prog_name = request.form.get('prog_name')
#     prog_desc = request.form.get('prog_desc')
#     prog_org = request.form.get('prog_org')
#     duration = request.form.get('duration')
#     num_volunteer_req = request.form.get('num_volunteer_req')
#     prog_date = request.form.get('prog_date')
#     client[DB_NAME].volunteer_prog.insert_one({
#         "_id": ObjectId(activity_id)
#     }, {
#         "$set": {
#             'prog_name': prog_name,
#             'prog_date': datetime.datetime.strptime(prog_date, "%Y-%m-%d"),
#             'prog_desc': prog_desc,
#             'duration': duration,
#             'num_volunteer_req': num_volunteer_req,
#             'prog_org': prog_org
#         }
#     })
#     flash(f'Your event has been updated!')
#     return render_template('volunteer.template.html')
    

# # Show individual volunteers
# @app.route('/volunteer/details/<activity_id>')
# def show_activity_details(activity_id):
#     vol = client[DB_NAME].volunteer_prog.find_one({
#         "_id": ObjectId(activity_id)
#     })
#     return render_template('activity_details.template.html', vol=vol)

# # Post individual volunteers
# @app.route('/volunteer/details/<activity_id>', methods=['POST'])
# def process_activity_volunteer(activity_id):
#     vol_name= request.form.get('vol_name')
#     vol_dob = request.form.get('vol_dob')
#     vol_email = request.form.get('vol_email')
#     vol_phone = request.form.get('vol_phone')
#     vol_desc = request.form.get('vol_desc')
#     vol_activity = activity_id
#     client[DB_NAME].volunteer_register.insert_one({
#     'vol_name': vol_name,
#     'vol_dob': datetime.datetime.strptime(vol_dob, "%Y-%m-%d"),
#     'vol_desc': vol_desc,
#     'vol_email': vol_email,
#     'vol_activity': vol_activity,
#     'vol_phone': vol_phone
#     })
#     flash(f'You have registered for the event!')
#     return render_template('volunteer.template.html')

# # "magic code" -- boilerplate
# if __name__ == '__main__':
#     app.run(host=os.environ.get('IP'),
#             port=int(os.environ.get('PORT')),
#             debug=True)
