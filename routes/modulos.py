from flask import Blueprint, render_template
from utils.auth import login_required
from models.models import Modulo, Nota, Archivo, Video, Enlace, Tarea
from jinja2 import TemplateNotFound
import os

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

@modulos.route("/modulo/<codigo>/<seccion>")
@login_required
def ver_seccion(codigo, seccion):

    modulo = Modulo.query.filter_by(
        codigo=codigo
    ).first_or_404()

    template = f"secciones/{seccion}.html"

    try:

        return render_template(
            template,
            modulo=modulo
        )

    except TemplateNotFound:

        ruta = os.path.join("templates", "secciones", f"{seccion}.html")

        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as f:
            f.write(f"""
{{% extends 'base.html' %}}

{{% block content %}}

<h1>{{{{ modulo.nombre }}}}</h1>

<h2>{seccion.capitalize()}</h2>

<p>Página creada automáticamente.</p>

{{% endblock %}}
""")

        return render_template(
            template,
            modulo=modulo
        )