from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Base de datos
db = SQLAlchemy()

# Login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Debes iniciar sesión para acceder."

# Migraciones
migrate = Migrate()