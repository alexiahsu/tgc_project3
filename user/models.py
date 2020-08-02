from flask import Flask, jsonify, request, session, redirect, flash
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        
        #Create the user object
        user = {
            "_id":uuid.uuid4().hex,
            "username": request.form.get('username'),
            "org_email": request.form.get('org_email'),
            "password": request.form.get('password'),
            "org_name": request.form.get('org_name'),
            "org_desc": request.form.get('org_desc'),
            "uploaded_file_url": request.form.get('uploaded_file_url')
        }

        #Encyrpt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #Check for existing email address
        if db.users.find_one({
            "org_email": user['org_email']
        }):
            return jsonify({
                "error": "Email address already in use"
            }), 400
        
        #Check for existing username
        if db.users.find_one({
            "username": user['username']
        }):
            return jsonify({
                "error": "Username already in use"
            }), 400

        #Check for existing org name
        if db.users.find_one({
            "org_name": user['org_name']
        }):
            return jsonify({
                "error": "Username already in use"
            }), 400

        if db.users.insert_one(user):
            flash(f'Welcome! Our database has verified your application, congratulations on becoming our administrator!')
            return self.start_session(user)


        return jsonify({
            "error": "Signup failed"
        }), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def signin(self):
        user = db.users.find_one({
            "username": request.form.get('username')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({
            "error": "Invalid login credentials"
        }), 401