from config import Config
from flask import Flask, session, redirect, url_for
from functools import wraps
from extensions import db
from routes.auth import auth
from routes.clases import clases
from routes.main import main

app = Flask(__name__)
app.config.from_object(Config)

ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","webp"}

def archivo_permitido(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------- Inicializar DB ----------------
db.init_app(app)

# ---------------- Blueprints ----------------
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(clases, url_prefix="/clases")
app.register_blueprint(main)


# ---------------- Crear tablas ----------------
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)