from functools import wraps
from flask import redirect, session, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:
            flash("Debes iniciar sesión")
            return redirect(url_for("auth.auth_page"))

        return f(*args, **kwargs)

    return decorated_function