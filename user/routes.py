from flask import Flask
# from app file import the app flask
from app import app
from user.models import User

@app.route('/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/signout')
def signout():
    return User().signout()

@app.route('/signin', methods=['POST'])
def signin():
    return User().signin()