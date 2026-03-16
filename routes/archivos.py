import os
from flask import Blueprint, request, redirect, current_app
from werkzeug.utils import secure_filename
from models.models import Archivo, Modulo
from extensions import db

archivos = Blueprint("archivos", __name__)


@archivos.route("/archivo/crear/<int:modulo_id>", methods=["POST"])
def crear_archivo(modulo_id):

    modulo = Modulo.query.get_or_404(modulo_id)

    nombre = request.form.get("nombre")
    file = request.files.get("archivo")

    if not file or file.filename == "":
        return redirect(f"/modulo/{modulo.codigo}/archivos")

    filename = secure_filename(file.filename)

    upload_folder = os.path.join(current_app.root_path, "static", "uploads")

    # crea carpeta si no existe
    os.makedirs(upload_folder, exist_ok=True)

    ruta_completa = os.path.join(upload_folder, filename)

    file.save(ruta_completa)

    archivo = Archivo(
        nombre=nombre,
        ruta=filename,
        modulo_id=modulo_id
    )

    db.session.add(archivo)
    db.session.commit()

    return redirect(f"/modulo/{modulo.codigo}/archivos")


@archivos.route("/archivo/eliminar/<int:id>")
def eliminar_archivo(id):

    archivo = Archivo.query.get_or_404(id)
    modulo = Modulo.query.get(archivo.modulo_id)

    ruta = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        archivo.ruta
    )

    if os.path.exists(ruta):
        os.remove(ruta)

    db.session.delete(archivo)
    db.session.commit()

    return redirect(f"/modulo/{modulo.codigo}/archivos")