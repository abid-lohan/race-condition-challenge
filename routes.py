from flask import render_template, url_for, flash, redirect, request
from app import app, db
from models import User, Burger, Purchase
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
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login falhou. Por favor, verifique seu usuário e senha.', 'danger')
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
        flash('Depósito realizado com sucesso!', 'success')
        return redirect(url_for('wallet'))
    return render_template('wallet.html', form=form)

@app.route('/buy/<int:burger_id>', methods=['POST'])
@login_required
def buy_burger(burger_id):
    burger = Burger.query.get_or_404(burger_id)
    if current_user.wallet >= burger.price:
        current_user.wallet -= burger.price
        purchase = Purchase(user_id=current_user.id, burger_id=burger.id)
        db.session.add(purchase)
        db.session.commit()
        flash(f'Você comprou um {burger.name} por ${burger.price}!', 'success')
    else:
        flash('Dinheiro insuficiente.', 'danger')
    return redirect(url_for('home'))

@app.route('/history')
@login_required
def history():
    purchases = Purchase.query.filter_by(user_id=current_user.id).order_by(Purchase.timestamp.desc()).all()
    return render_template('history.html', purchases=purchases)

@app.route('/cancel_purchase/<int:purchase_id>', methods=['POST'])
@login_required
def cancel_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    if purchase.buyer.id == current_user.id:
        current_user.wallet += purchase.burger.price
        db.session.delete(purchase)
        db.session.commit()
        flash(f'Você cancelou a compra de um {purchase.burger.name}.', 'success')
    else:
        flash('Você não está autorizado a cancelar essa compra.', 'danger')
    return redirect(url_for('history'))