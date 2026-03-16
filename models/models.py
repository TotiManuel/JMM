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

    modulo = db.relationship("Modulo", back_populates="clases")

    bloques = db.relationship(
        "BloqueClase",
        back_populates="clase",
        cascade="all, delete"
    )
class BloqueClase(db.Model):

    __tablename__ = "bloque_clase"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    contenido = db.Column(db.Text)
    orden = db.Column(db.Integer)

    clase_id = db.Column(
        db.Integer,
        db.ForeignKey("clases.id"),
        nullable=False
    )

    clase = db.relationship(
        "Clase",
        back_populates="bloques"
    )
class Modulo(db.Model):

    __tablename__ = "modulos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)

    clases = db.relationship(
        "Clase",
        back_populates="modulo",
        cascade="all, delete"
    )
class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text)

    modulo_codigo = db.Column(db.String(50), db.ForeignKey("modulos.codigo"))

    def __repr__(self):
        return f"<Nota {self.titulo}>"
class Archivo(db.Model):
    __tablename__ = "archivos"
    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(200))

    url = db.Column(db.String(500))

    modulo_id = db.Column(
        db.Integer,
        db.ForeignKey("modulos.id")
    )
    modulo = db.relationship("Modulo", backref=db.backref("archivos", lazy=True))
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