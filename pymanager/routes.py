from pymanager import app
from flask import render_template, redirect, url_for, flash


@app.route('/')
def index():
    
    # Render dashboard if user is logged in
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')
