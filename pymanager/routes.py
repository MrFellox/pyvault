from pymanager import app
from flask import render_template, redirect, url_for, flash


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/login')
def login():
    return render_template('login.html')
