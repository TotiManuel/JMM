from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.models import Usuario
from extensions import db

auth = Blueprint("auth", __name__)

@auth.route('/auth', methods=['GET'])
def auth_page():
    return render_template('auth.html')


# -------- LOGIN --------
@auth.route('/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = Usuario.query.filter_by(username=username).first()

    if user and user.check_password(password):
        session['user'] = user.username
        return redirect(url_for('main.home'))

    flash("Credenciales incorrectas")
    return redirect(url_for('auth.auth_page'))


# -------- REGISTER --------
@auth.route('/register', methods=['POST'])
def register():

    username = request.form.get('username')
    password = request.form.get('password')

    existing = Usuario.query.filter_by(username=username).first()

    if existing:
        flash("El usuario ya existe")
        return redirect(url_for('auth.auth_page'))

    user = Usuario(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    flash("Cuenta creada, ahora inicia sesión")
    return redirect(url_for('auth.auth_page'))


# -------- LOGOUT --------
@auth.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.auth_page'))