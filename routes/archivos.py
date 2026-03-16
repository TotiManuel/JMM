import os
from flask import Blueprint, request, redirect, url_for
from werkzeug.utils import secure_filename
from models.models import Archivo
from extensions import db

archivos = Blueprint("archivos", __name__)

UPLOAD_FOLDER = "static/uploads"


@archivos.route("/archivo/crear/<int:modulo_id>", methods=["POST"])
def crear_archivo(modulo_id):

    nombre = request.form["nombre"]
    file = request.files["archivo"]

    if file:

        filename = secure_filename(file.filename)

        ruta = os.path.join(UPLOAD_FOLDER, filename)

        file.save(ruta)

        archivo = Archivo(
            nombre=nombre,
            ruta=filename,
            modulo_id=modulo_id
        )

        db.session.add(archivo)
        db.session.commit()

    return redirect(request.referrer)


@archivos.route("/archivo/eliminar/<int:id>")
def eliminar_archivo(id):

    archivo = Archivo.query.get_or_404(id)

    ruta = os.path.join("static/uploads", archivo.ruta)

    if os.path.exists(ruta):
        os.remove(ruta)

    db.session.delete(archivo)
    db.session.commit()

    return redirect(request.referrer)