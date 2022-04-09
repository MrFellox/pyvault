from pyvault import app, login_manager, db, bcrypt
from flask import render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required, login_user, logout_user
from pyvault.models import User, Password
from pyvault.forms import AddPasswordForm, LoginForm, RegisterForm
from uuid import uuid4

# Login

@login_manager.user_loader
def load_user(user_id):

    user = db.collection('users').where('id', '==', user_id).get()

    if len(user) == 0:
        return None

    user = user[0].to_dict()
    return User.from_dict(user)

def unauthorized():
    return redirect(url_for('index'))

login_manager.unauthorized_handler(unauthorized)

@app.route('/')
def index():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))


    # Get user passwords
    passwords = db.collection('passwords').where('user_id', '==', current_user.id).get()

    password_objects = []
    for password in passwords:        
        password_objects.append(Password.from_dict(password.to_dict()))

    # Render dashboard if user is logged in
    return render_template('dashboard.html', user=current_user, passwords = password_objects)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():

        # Check that collection exists

        col_ref = db.collection('users').get()

        if len(col_ref) == 0:
            flash('That email address is not registered.', 'error')
            return redirect(url_for('login'))

        # Collection exists, keep going

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

    if current_user.is_authenticated:
        return redirect('/')

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
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_password', methods = ['GET', 'POST'])
def add_password():
    form = AddPasswordForm()

    if form.validate_on_submit():
            
            # Generate a unique UUID for the password
    
            password_id = uuid4().hex
    
            # Encrypt password

            password = Password(
                id = password_id,
                service_name = form.service_name.data,
                service_email = form.service_email.data,
                password = form.service_password.data,
                user_id = current_user.id
                )
    
            # Add password to firestore
    
            db.collection('passwords').document(password.id).set(password.to_dict())
    
            flash('Password added successully!')
            return redirect(url_for('index'))

    return render_template('add_password.html', form = form)

@app.route('/delete_password/<password_id>', methods = ['GET', 'POST'])
def delete_password(password_id):
    db.collection('passwords').document(password_id).delete()
    return redirect(url_for('index'))