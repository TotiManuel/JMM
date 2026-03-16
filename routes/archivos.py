import uuid
from flask import Blueprint, request, redirect
from supabase import create_client
from models.models import Archivo, Modulo
from extensions import db
from config import SUPABASE_URL, SUPABASE_KEY

archivos = Blueprint("archivos", __name__)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@archivos.route("/archivo/crear/<int:modulo_id>", methods=["POST"])
def crear_archivo(modulo_id):

    modulo = Modulo.query.get_or_404(modulo_id)

    nombre = request.form.get("nombre")
    file = request.files.get("archivo")

    if not file:
        return redirect(f"/modulo/{modulo.codigo}/archivos")

    # nombre único para evitar conflictos
    filename = f"{uuid.uuid4()}_{file.filename}"

    # subir a supabase storage
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