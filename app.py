from config import Config
from flask import Flask
from extensions import db
from routes.tareas import tareas
from routes.clases import clases
from routes.notas import notas
from routes.auth import auth
from routes.main import main
from routes.dashboard import dashboard
from routes.modulos import modulos
from routes.archivos import archivos
from routes.enlaces import enlaces
from models.models import *

app = Flask(__name__)
app.config.from_object(Config)

ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","webp"}

def archivo_permitido(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------- Inicializar DB ----------------
db.init_app(app)

# ---------------- Blueprints ----------------
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(main)
app.register_blueprint(dashboard, url_prefix="/dashboard")
app.register_blueprint(clases, url_prefix="/clases")
app.register_blueprint(notas, url_prefix="/notas")
app.register_blueprint(archivos)
app.register_blueprint(enlaces)
app.register_blueprint(tareas)
app.register_blueprint(modulos)

@app.context_processor
def inject_modulos():

    modulos = Modulo.query.all()

    return dict(modulos_navbar=modulos)

# ---------------- Crear tablas ----------------
with app.app_context():
    
    #db.reflect()
    #db.drop_all()
    db.create_all() 


if __name__ == '__main__':
    app.run(debug=True)