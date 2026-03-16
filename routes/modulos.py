from flask import Blueprint, render_template
from utils.auth import login_required
from extensions import db
from models.models import Clase, Modulo, Nota, Archivo, Video, Enlace, Tarea

modulos = Blueprint("modulos", __name__)


@modulos.route("/modulo/<codigo>")
@login_required
def ver_modulo(codigo):

    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    notas = Nota.query.filter_by(modulo_codigo=modulo.codigo).all()
    archivos = Archivo.query.filter_by(modulo_id=modulo.id).all()
    videos = Video.query.filter_by(modulo_id=modulo.id).all()
    enlaces = Enlace.query.filter_by(modulo_id=modulo.id).all()
    tareas = Tarea.query.filter_by(modulo_id=modulo.id).all()
    clases = Clase.query.filter_by(modulo_id=modulo.id).all()

    return render_template(
        "modulo.html",
        modulo=modulo,
        notas=notas,
        archivos=archivos,
        videos=videos,
        enlaces=enlaces,
        clases=clases,
        tareas=tareas
    )


@modulos.route("/modulo/<codigo>/<seccion>")
@login_required
def ver_seccion(codigo, seccion):

    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    data = {
        "notas": Nota.query.filter_by(modulo_codigo=modulo.codigo).all(),
        "archivos": Archivo.query.filter_by(modulo_id=modulo.id).all(),
        "videos": Video.query.filter_by(modulo_id=modulo.id).all(),
        "enlaces": Enlace.query.filter_by(modulo_id=modulo.id).all(),
        "tareas": Tarea.query.filter_by(modulo_id=modulo.id).all(),
        "clases": Clase.query.filter_by(modulo_id=modulo.id).all(),
    }

    return render_template(
        "seccion.html",
        modulo=modulo,
        seccion=seccion,
        **data
    )
    
@modulos.route("/clase/crear/<codigo>", methods=["POST"])
@login_required
def crear_clase(codigo):

    from flask import request, redirect

    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    titulo = request.form["titulo"]
    contenido = request.form["contenido"]

    nueva = Clase(
        titulo=titulo,
        contenido=contenido,
        modulo_id=modulo.id
    )

    db.session.add(nueva)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/clases")

@modulos.route("/clase/editar/<int:id>", methods=["POST"])
@login_required
def editar_clase(id):

    from flask import request, redirect

    clase = Clase.query.get_or_404(id)

    clase.titulo = request.form["titulo"]
    clase.contenido = request.form["contenido"]

    db.session.commit()

    return redirect(f"/modulo/{clase.modulo.codigo}/clases")

@modulos.route("/clase/eliminar/<int:id>")
@login_required
def eliminar_clase(id):

    from flask import redirect

    clase = Clase.query.get_or_404(id)
    codigo = clase.modulo.codigo

    db.session.delete(clase)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/clases")


