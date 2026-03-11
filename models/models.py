from extensions import db
from datetime import datetime

class Clase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(300))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    bloques = db.relationship('BloqueClase', backref='clase', cascade="all, delete")


class BloqueClase(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    clase_id = db.Column(db.Integer, db.ForeignKey('clase.id'))

    tipo = db.Column(db.String(50))
    contenido = db.Column(db.Text)

    orden = db.Column(db.Integer)