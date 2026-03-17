from flask import Blueprint, request, redirect
from models.models import Tarea, Subtarea, Modulo
from extensions import db

tareas = Blueprint("tareas", __name__)

# Crear tarea
@tareas.route("/tarea/crear/<codigo>", methods=["POST"])
def crear_tarea(codigo):
    modulo = Modulo.query.filter_by(codigo=codigo).first_or_404()

    tarea = Tarea(
        titulo=request.form["titulo"],
        descripcion=request.form.get("descripcion"),
        encargado=request.form.get("encargado"),
        modulo_id=modulo.id
    )

    db.session.add(tarea)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/tareas")


# Eliminar tarea
@tareas.route("/tarea/eliminar/<int:id>")
def eliminar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    codigo = tarea.modulo.codigo

    db.session.delete(tarea)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/tareas")


# Toggle completada
@tareas.route("/tarea/toggle/<int:id>")
def toggle_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.completada = not tarea.completada
    db.session.commit()

    return redirect(f"/modulo/{tarea.modulo.codigo}/tareas")


# -------- SUBTAREAS --------

@tareas.route("/subtarea/crear/<int:tarea_id>", methods=["POST"])
def crear_subtarea(tarea_id):
    subtarea = Subtarea(
        titulo=request.form["titulo"],
        tarea_id=tarea_id
    )

    db.session.add(subtarea)
    db.session.commit()

    tarea = Tarea.query.get(tarea_id)
    return redirect(f"/modulo/{tarea.modulo.codigo}/tareas")


@tareas.route("/subtarea/toggle/<int:id>")
def toggle_subtarea(id):
    subtarea = Subtarea.query.get_or_404(id)
    subtarea.completada = not subtarea.completada
    db.session.commit()

    return redirect(f"/modulo/{subtarea.tarea.modulo.codigo}/tareas")


@tareas.route("/subtarea/eliminar/<int:id>")
def eliminar_subtarea(id):
    subtarea = Subtarea.query.get_or_404(id)
    codigo = subtarea.tarea.modulo.codigo

    db.session.delete(subtarea)
    db.session.commit()

    return redirect(f"/modulo/{codigo}/tareas")