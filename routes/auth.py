from flask import Blueprint, render_template, request, redirect, url_for, session
from utils.auth import login_required

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        if request.form.get('username') == 'Julian' and request.form.get('password') == 'admin':
            session['user'] = 'Julian'

            return redirect(url_for('main.home'))

    return render_template('login.html', title="Login")


@auth.route('/logout')
def logout():

    session.pop('user', None)

    return redirect(url_for('main.home'))
