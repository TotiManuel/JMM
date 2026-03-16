import uuid
from flask import Blueprint, request, redirect
from models.models import Archivo, Modulo
from extensions import db
from utils.supabase_client import get_supabase

archivos = Blueprint("archivos", __name__)


@archivos.route("/archivo/crear/<int:modulo_id>", methods=["POST"])
def crear_archivo(modulo_id):

    modulo = Modulo.query.get_or_404(modulo_id)

    nombre = request.form.get("nombre")
    file = request.files.get("archivo")

    if not file:
        return redirect(f"/modulo/{modulo.codigo}/archivos")

    supabase = get_supabase()

    # nombre único
    filename = f"{uuid.uuid4()}_{file.filename}"

    # subir archivo
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
        modulo_id=modulo_id
    )

    db.session.add(archivo)
    db.session.commit()

    return redirect(f"/modulo/{modulo.codigo}/archivos")

@archivos.route("/archivo/eliminar/<int:id>")
def eliminar_archivo(id):

    archivo = Archivo.query.get_or_404(id)

    modulo = Modulo.query.get(archivo.modulo_id)

    db.session.delete(archivo)
    db.session.commit()

    return redirect(f"/modulo/{modulo.codigo}/archivos")