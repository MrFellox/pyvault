from pyvault import app, login_manager, db, bcrypt
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from pyvault.models import Users, Passwords
from pyvault.forms import LoginForm, RegisterForm
from uuid import uuid4

# Login


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


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
        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))

        else:
            flash('Invalid email or password.')

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user:
            flash('That email is already registered.', category='error')
            print('Email is already registerd ============')
            return redirect(url_for('register'))

        # Generate a unique UUID for the user

        user_id = uuid4().hex

        # Encrypt user's password

        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = Users(
            id=user_id,
            email=form.email.data,
            password=hashed_password,
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )

        db.session.add(user)
        db.session.commit()

        flash('Account created successully! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
