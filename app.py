from flask import Flask, render_template, session, request, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = "super-secret-key"

# ---------------- Auth helpers ----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ---------------- Auth routes ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'Julian' and request.form['password'] == 'admin':
            session['user'] = 'Julian'
            return redirect(url_for('dashboard'))
    return render_template('login.html', title="Login")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")
# ---------------- Public routes ----------------

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/tutoriales')
@login_required
def tutoriales():
    return render_template('tutoriales.html', title="Tutoriales")

@app.route('/organizacion')
@login_required
def organizacion():
    return render_template('organizacion.html', title="Organizacion")

@app.route('/recordatorios')
@login_required
def recordatorios():
    return render_template('recordatorios.html', title="Recordatorios")

@app.route('/pruebas')
def pruebas():
    return render_template('pruebas.html', title="Pruebas")


if __name__ == '__main__':
    app.run(debug=True)
