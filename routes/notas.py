from flask import Blueprint, render_template, url_for, request, redirect
from models.models import Nota
from extensions import db

notas = Blueprint("notas", __name__)

@notas.route("/nota/<int:id>")
def ver_nota(id):

    nota = Nota.query.get_or_404(id)

    return render_template(
        "nota.html",
        nota=nota
    )


@notas.route("/nota/crear/<codigo>", methods=["POST"])
def crear_nota(codigo):

    titulo = request.form["titulo"]
    contenido = request.form["contenido"]

    nota = Nota(
        titulo=titulo,
        contenido=contenido,
        modulo_codigo=codigo
    )

    db.session.add(nota)
    db.session.commit()

    return redirect(url_for("notas.ver_nota", id=nota.id))


@notas.route("/nota/editar/<int:id>", methods=["POST"])
def editar_nota(id):

    nota = Nota.query.get_or_404(id)

    nota.titulo = request.form["titulo"]
    nota.contenido = request.form["contenido"]

    db.session.commit()

    return redirect(url_for("notas.ver_nota", id=nota.id))


@notas.route("/nota/eliminar/<int:id>")
def eliminar_nota(id):

    nota = Nota.query.get_or_404(id)

    db.session.delete(nota)
    db.session.commit()

    return redirect("/")