from flask import Blueprint, request, redirect
from models.models import Enlace, Modulo
from extensions import db

enlaces = Blueprint("enlaces", __name__)

# Crear enlace
@enlaces.route("/enlace/crear/<codigo>", methods=["POST"])
def crear_enlace(codigo):
    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    titulo = request.form["titulo"]
    url = request.form["url"]

    enlace = Enlace(
        titulo=titulo,
        url=url,
        modulo_id=modulo.id
    )

    db.session.add(enlace)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/enlaces")


# Editar enlace
@enlaces.route("/enlace/editar/<int:id>", methods=["POST"])
def editar_enlace(id):
    enlace = Enlace.query.get_or_404(id)

    enlace.titulo = request.form["titulo"]
    enlace.url = request.form["url"]

    db.session.commit()
    return redirect(f"/modulo/{enlace.modulo.codigo}/enlaces")


# Eliminar enlace
@enlaces.route("/enlace/eliminar/<int:id>")
def eliminar_enlace(id):
    enlace = Enlace.query.get_or_404(id)
    codigo = enlace.modulo.codigo

    db.session.delete(enlace)
    db.session.commit()
    return redirect(f"/modulo/{codigo}/enlaces")