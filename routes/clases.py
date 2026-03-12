import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from extensions import db
from utils.auth import login_required
from models.models import BloqueClase, Clase
from werkzeug.utils import secure_filename

clases = Blueprint("clases", __name__)
#region Enfermeria
# routes/clases.py
@clases.route('/')
@login_required
def lista_clases():
    clases = Clase.query.order_by(Clase.fecha.desc()).all()
    return render_template('clases.html', clases=clases)

@clases.route('/<int:id>')
@login_required
def ver_clase(id):
    clase = Clase.query.get_or_404(id)
    bloques = BloqueClase.query.filter_by(clase_id=id).order_by(BloqueClase.orden).all()
    return render_template('ver_clase.html', clase=clase, bloques=bloques)
@clases.route('/clases/nueva', methods=['GET','POST'])
@login_required
def nueva_clase():

    if request.method == 'POST':

        titulo = request.form['titulo']
        descripcion = request.form['descripcion']

        clase = Clase(
            titulo=titulo,
            descripcion=descripcion
        )

        db.session.add(clase)
        db.session.commit()

        return redirect(url_for('clases.editar_clase', id=clase.id))

    return render_template('nueva_clase.html')
@clases.route("/clases/<int:id>/bloque", methods=["POST"])
@login_required
def agregar_bloque(id):

    tipo = request.form["tipo"]
    contenido = request.form.get("contenido")

    archivo = request.files.get("imagen")

    # si se sube imagen desde la PC
    if archivo and archivo.filename != "":

        nombre = str(uuid.uuid4()) + "_" + secure_filename(archivo.filename)

        ruta = os.path.join(current_app.config["UPLOAD_FOLDER"], nombre)

        archivo.save(ruta)

        contenido = "/" + ruta


    ultimo = BloqueClase.query.filter_by(clase_id=id)\
        .order_by(BloqueClase.orden.desc()).first()

    orden = 1
    if ultimo:
        orden = ultimo.orden + 1

    bloque = BloqueClase(
        clase_id=id,
        tipo=tipo,
        contenido=contenido,
        orden=orden
    )

    db.session.add(bloque)
    db.session.commit()

    return redirect(url_for("clases.editar_clase", id=id))
@clases.route("/clase/<int:id>/eliminar", methods=["POST"])
@login_required
def eliminar_clase(id):

    clase = Clase.query.get_or_404(id)

    db.session.delete(clase)
    db.session.commit()

    return redirect(url_for("clases.lista_clases"))
@clases.route("/api/agregar_bloque/<int:clase_id>", methods=["POST"])
@login_required
def api_agregar_bloque(clase_id):

    tipo = request.form["tipo"]
    contenido = request.form["contenido"]

    ultimo = BloqueClase.query.filter_by(
        clase_id=clase_id
    ).order_by(BloqueClase.orden.desc()).first()

    orden = 1
    if ultimo:
        orden = ultimo.orden + 1

    bloque = BloqueClase(
        clase_id=clase_id,
        tipo=tipo,
        contenido=contenido,
        orden=orden
    )

    db.session.add(bloque)
    db.session.commit()

    return {"status": "ok"}
@clases.route('/clases/<int:id>/editar', methods=['GET','POST'])
@login_required
def editar_clase(id):

    clase = Clase.query.get_or_404(id)

    bloques = BloqueClase.query.filter_by(
        clase_id=id
    ).order_by(BloqueClase.orden).all()

    if request.method == 'POST':

        clase.titulo = request.form['titulo']
        clase.descripcion = request.form['descripcion']

        db.session.commit()

    return render_template(
        "editar_clase.html",
        clase=clase,
        bloques=bloques
    )
@clases.route("/bloque/<int:id>/eliminar", methods=["POST"])
@login_required
def eliminar_bloque(id):

    bloque = BloqueClase.query.get_or_404(id)

    clase_id = bloque.clase_id

    db.session.delete(bloque)
    db.session.commit()

    return redirect(url_for("clases.editar_clase", id=clase_id))
#endregion