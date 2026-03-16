import os
import uuid
from flask import Blueprint, request, redirect
from supabase import create_client
from werkzeug.utils import secure_filename
from models.models import Archivo, Modulo
from extensions import db
from config import Config

archivos = Blueprint("archivos", __name__)

# Supabase client usando la Service Role Key
SUPABASE_URL = Config.SUPABASE_URL
SUPABASE_KEY = Config.SUPABASE_SERVICE_ROLE_KEY  # ✅ Service role key para subir archivos

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@archivos.route("/archivo/crear/<codigo>", methods=["POST"])
def crear_archivo(codigo):

    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    nombre = request.form.get("nombre")
    file = request.files.get("archivo")

    if not file or not nombre:
        return redirect(f"/modulo/{codigo}/archivos")

    # nombre seguro y único para evitar problemas
    filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"

    # subir archivo a Supabase Storage
    try:
        supabase.storage.from_("archivos").upload(
            filename,
            file.read(),
            {"content-type": file.content_type}
        )
    except Exception as e:
        print("Error subiendo a Supabase:", e)
        return redirect(f"/modulo/{codigo}/archivos")

    # obtener URL pública
    url = supabase.storage.from_("archivos").get_public_url(filename)

    # guardar en Neon
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

    # opcional: borrar archivo de Supabase
    try:
        supabase.storage.from_("archivos").remove([archivo.url.split("/")[-1]])
    except Exception as e:
        print("Error borrando de Supabase:", e)

    db.session.delete(archivo)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/archivos")