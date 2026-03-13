from flask import Blueprint, render_template, request, redirect, url_for, session
from models.models import BloqueClase, Clase
from utils.auth import login_required

clases = Blueprint("clases", __name__)

@clases.route("/clase/<int:id>")
@login_required
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