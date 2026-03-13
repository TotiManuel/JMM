from flask import Blueprint, render_template
from models.models import Clase
from models.models import BloqueClase

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