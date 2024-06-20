from flask import render_template, url_for, flash, redirect, request
from app import app, db
from models import User, Burger
from forms import RegistrationForm, LoginForm, WalletForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    burgers = Burger.query.all()
    return render_template('home.html', burgers=burgers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/wallet', methods=['GET', 'POST'])
@login_required
def wallet():
    form = WalletForm()
    if form.validate_on_submit():
        current_user.wallet += form.amount.data
        db.session.commit()
        flash('Amount added to wallet!', 'success')
        return redirect(url_for('wallet'))
    return render_template('wallet.html', form=form)
