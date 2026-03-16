import os
import uuid
from flask import Blueprint, request, redirect
from supabase import create_client
from models.models import Archivo, Modulo
from extensions import db
from config import Config

archivos = Blueprint("archivos", __name__)

SUPABASE_URL = Config.SUPABASE_URL
SUPABASE_KEY = Config.SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@archivos.route("/archivo/crear/<codigo>", methods=["POST"])
def crear_archivo(codigo):

    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    nombre = request.form["nombre"]
    file = request.files.get("archivo")

    if not file:
        return redirect(f"/modulo/{codigo}/archivos")

    # nombre único para el archivo
    filename = f"{uuid.uuid4()}_{file.filename}"

    # subir archivo a supabase
    supabase.storage.from_("archivos").upload(
        filename,
        file.read(),
        {"content-type": file.content_type}
    )

    # obtener url pública
    url = supabase.storage.from_("archivos").get_public_url(filename)

    archivo = Archivo(
        nombre=nombre,
        url=url,
        modulo_id=modulo.id
    )

    db.session.add(archivo)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/archivos")


@archivos.route("/archivo/eliminar/<int:id>")
def eliminar_archivo(id):

    archivo = Archivo.query.get_or_404(id)

    codigo = archivo.modulo.codigo

    db.session.delete(archivo)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/archivos")