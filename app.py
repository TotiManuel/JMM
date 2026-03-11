from flask import Flask, render_template, session, request, redirect, url_for
from functools import wraps
from extensions import db, login_manager, migrate
from models.models import BloqueClase, Clase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

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
        if request.form.get('username') == 'Julian' and request.form.get('password') == 'admin':
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

#region Enfermeria
@app.route('/clases')
@login_required
def clases():

    clases = Clase.query.order_by(Clase.fecha.desc()).all()

    return render_template(
        'clases.html',
        clases=clases
    )
@app.route('/clases/nueva', methods=['GET','POST'])
@login_required
def nueva_clase():

    if request.method == 'POST':

        titulo = request.form['titulo']
        descripcion = request.form['descripcion']

        clase = Clase(
            titulo=titulo,
            descripcion=descripcion
        )

        db.session.add(clase)
        db.session.commit()

        return redirect(url_for('editar_clase', id=clase.id))

    return render_template('nueva_clase.html')
@app.route('/clases/<int:id>/editar', methods=['GET','POST'])
@login_required
def editar_clase(id):

    clase = Clase.query.get_or_404(id)

    if request.method == 'POST':

        clase.titulo = request.form['titulo']
        clase.descripcion = request.form['descripcion']

        db.session.commit()

    return render_template(
        'editar_clase.html',
        clase=clase
    )
@app.route('/clases/<int:id>')
@login_required
def ver_clase(id):

    clase = Clase.query.get_or_404(id)

    bloques = BloqueClase.query.filter_by(
        clase_id=id
    ).order_by(BloqueClase.orden).all()

    return render_template(
        'ver_clase.html',
        clase=clase,
        bloques=bloques
    )
@app.route('/clases/<int:id>/eliminar')
@login_required
def eliminar_clase(id):

    clase = Clase.query.get_or_404(id)

    db.session.delete(clase)
    db.session.commit()

    return redirect(url_for('clases'))
#endregion

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
