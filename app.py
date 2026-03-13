from config import Config
from flask import Flask, session, redirect, url_for
from functools import wraps
from extensions import db
from routes.auth import auth
from routes.main import main
from routes.dashboard import dashboard
from routes.modulos import modulos
from models.models import Modulo

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
app.register_blueprint(modulos)

@app.context_processor
def inject_modulos():

    modulos = Modulo.query.all()

    return dict(modulos_navbar=modulos)

# ---------------- Crear tablas ----------------
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)