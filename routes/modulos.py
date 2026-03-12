from flask import Blueprint, render_template
from utils.auth import login_required
from models.models import Modulo
from models.models import Nota
from models.models import Archivo
from models.models import Video
from models.models import Enlace
from models.models import Tarea

modulos = Blueprint("modulos", __name__)


@modulos.route("/modulo/<codigo>")
@login_required
def ver_modulo(codigo):

    modulo = Modulo.query.filter_by(
        codigo=codigo
    ).first_or_404()

    notas = Nota.query.filter_by(modulo_id=modulo.id).all()

    archivos = Archivo.query.filter_by(modulo_id=modulo.id).all()

    videos = Video.query.filter_by(modulo_id=modulo.id).all()

    enlaces = Enlace.query.filter_by(modulo_id=modulo.id).all()

    tareas = Tarea.query.filter_by(modulo_id=modulo.id).all()

    return render_template(
        "modulo.html",
        modulo=modulo,
        notas=notas,
        archivos=archivos,
        videos=videos,
        enlaces=enlaces,
        tareas=tareas
    )