from pyvault import app, login_manager, db, bcrypt
from flask import render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user
from pyvault.models import User
from pyvault.forms import LoginForm, RegisterForm
from uuid import uuid4

# Login

@login_manager.user_loader
def load_user(user_id):

    user = db.collection('users').where('id', '==', user_id).get()

    if len(user) == 0:
        return None

    user = user[0].to_dict()
    return User.from_dict(user)

@app.route('/')
def index():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    # Render dashboard if user is logged in
    return render_template('dashboard.html', user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.collection('users').where('email', '==', form.email.data).get()

        if len(user) == 0:
            flash('That email address is not registered.', 'error')
            return redirect(url_for('login'))

        user = User.from_dict(user[0].to_dict())


        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            return redirect(url_for('index'))

        else:
            flash('Incorrect password.', 'error')

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        # Query email from firestore

        user = db.collection('users').where('email', '==', form.email.data).get()

        if len(user) > 0:
            flash('That email address is already registered.', 'error')
            return redirect(url_for('register'))

        # Generate a unique UUID for the user

        user_id = uuid4().hex

        # Encrypt user's password

        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(
            id = user_id,
            email = form.email.data,
            password = hashed_password,
            first_name=form.first_name.data,
            last_name=form.last_name.data
            )

        # Add user to firestore

        db.collection('users').document(user.id).set(user.to_dict())

        flash('Account created successully! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/firestore')
def firestore():

    doc_ref = db.collection('users').document('jfernandohernandez28@gmail.com').get()

    if doc_ref.exists:
        print('found')

    else:
        print('not found')

    return 'Hello world'