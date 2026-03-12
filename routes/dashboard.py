from flask import Blueprint, render_template, request, redirect, url_for
from utils.auth import login_required
from extensions import db
from models.models import Modulo

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/")
@login_required
def dashboard_view():

    modulos = Modulo.query.all()

    return render_template(
        "dashboard.html",
        modulos=modulos
    )


@dashboard.route("/crear_modulo", methods=["POST"])
@login_required
def crear_modulo():

    nombre = request.form["nombre"]
    codigo = request.form["codigo"]
    descripcion = request.form["descripcion"]

    nuevo = Modulo(
        nombre=nombre,
        codigo=codigo,
        descripcion=descripcion
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for("dashboard.dashboard_view"))

@dashboard.route("/eliminar_modulo/<int:id>")
@login_required
def eliminar_modulo(id):

    modulo = Modulo.query.get_or_404(id)

    db.session.delete(modulo)
    db.session.commit()

    return redirect(url_for("dashboard.dashboard_view"))