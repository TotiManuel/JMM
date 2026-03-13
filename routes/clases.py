from flask import Blueprint, render_template, url_for
from models.models import Clase
from models.models import BloqueClase
from flask import request, redirect
from extensions import db

clases = Blueprint("clases", __name__)

@clases.route("/<int:id>")
def ver_clase(id):

    clase = Clase.query.get_or_404(id)

    bloques = BloqueClase.query.filter_by(
        clase_id=id
    ).order_by(BloqueClase.orden).all()

    return render_template(
        "clase.html",
        clase=clase,
        bloques=bloques
    )
@clases.route("/bloque/<int:clase_id>", methods=["POST"])
def crear_bloque(clase_id):

    clase = Clase.query.get_or_404(clase_id)

    tipo = request.form.get("tipo")
    contenido = request.form.get("contenido")

    orden = BloqueClase.query.filter_by(
        clase_id=clase.id
    ).count()

    bloque = BloqueClase(
        tipo=tipo,
        contenido=contenido,
        orden=orden,
        clase_id=clase.id
    )

    db.session.add(bloque)
    db.session.commit()

    return redirect(url_for("clases.ver_clase", id=clase.id))