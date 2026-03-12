from flask import Blueprint, render_template
from utils.auth import login_required

main = Blueprint("main", __name__)


@main.route('/')
def home():
    return render_template('home.html', title="Home")


@main.route('/organizacion')
@login_required
def organizacion():
    return render_template('organizacion.html', title="Organizacion")


@main.route('/recordatorios')
@login_required
def recordatorios():
    return render_template('recordatorios.html', title="Recordatorios")


@main.route('/pruebas')
def pruebas():
    return render_template('pruebas.html', title="Pruebas")