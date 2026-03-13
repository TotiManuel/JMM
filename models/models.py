from extensions import db
from datetime import datetime

class Clase(db.Model):
    
    __tablename__ = "clases"

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200))

    contenido = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id"),
        nullable=False
    )

    modulo = db.relationship("Modulo", backref="clases")

class Modulo(db.Model):

    __tablename__ = "modulos"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    codigo = db.Column(db.String(100), unique=True, nullable=False)

    descripcion = db.Column(db.Text)
    
class Nota(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200))

    contenido = db.Column(db.Text)

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )
    
class Archivo(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(200))

    ruta = db.Column(db.String(300))

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )
    
class Video(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200))

    url = db.Column(db.String(300))

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )
    
class Enlace(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200))

    url = db.Column(db.String(300))

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )
    
class Tarea(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200))

    completado = db.Column(db.Boolean, default=False)

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )