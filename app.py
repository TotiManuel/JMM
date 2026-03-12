import uuid

from flask import Flask, render_template, session, request, redirect, url_for
from functools import wraps
from extensions import db
from models.models import BloqueClase, Clase
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","webp"}

def archivo_permitido(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS
db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- Auth helpers ----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user" not in session:
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
@app.route("/clases/<int:id>/bloque", methods=["POST"])
@login_required
def agregar_bloque(id):

    tipo = request.form["tipo"]
    contenido = request.form.get("contenido")

    archivo = request.files.get("imagen")

    # si se sube imagen desde la PC
    if archivo and archivo.filename != "":

        nombre = str(uuid.uuid4()) + "_" + secure_filename(archivo.filename)

        ruta = os.path.join(app.config["UPLOAD_FOLDER"], nombre)

        archivo.save(ruta)

        contenido = "/" + ruta


    ultimo = BloqueClase.query.filter_by(clase_id=id)\
        .order_by(BloqueClase.orden.desc()).first()

    orden = 1
    if ultimo:
        orden = ultimo.orden + 1

    bloque = BloqueClase(
        clase_id=id,
        tipo=tipo,
        contenido=contenido,
        orden=orden
    )

    db.session.add(bloque)
    db.session.commit()

    return redirect(url_for("editar_clase", id=id))

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
@app.route("/clase/<int:id>/eliminar", methods=["POST"])
def eliminar_clase(id):

    clase = Clase.query.get_or_404(id)

    db.session.delete(clase)
    db.session.commit()

    return redirect(url_for("clases"))
@app.route("/api/agregar_bloque/<int:clase_id>", methods=["POST"])
@login_required
def api_agregar_bloque(clase_id):

    tipo = request.form["tipo"]
    contenido = request.form["contenido"]

    ultimo = BloqueClase.query.filter_by(
        clase_id=clase_id
    ).order_by(BloqueClase.orden.desc()).first()

    orden = 1
    if ultimo:
        orden = ultimo.orden + 1

    bloque = BloqueClase(
        clase_id=clase_id,
        tipo=tipo,
        contenido=contenido,
        orden=orden
    )

    db.session.add(bloque)
    db.session.commit()

    return {"status": "ok"}
@app.route('/clases/<int:id>/editar', methods=['GET','POST'])
@login_required
def editar_clase(id):

    clase = Clase.query.get_or_404(id)

    bloques = BloqueClase.query.filter_by(
        clase_id=id
    ).order_by(BloqueClase.orden).all()

    if request.method == 'POST':

        clase.titulo = request.form['titulo']
        clase.descripcion = request.form['descripcion']

        db.session.commit()

    return render_template(
        "editar_clase.html",
        clase=clase,
        bloques=bloques
    )
@app.route("/bloque/<int:id>/eliminar", methods=["POST"])
def eliminar_bloque(id):

    bloque = BloqueClase.query.get_or_404(id)

    clase_id = bloque.clase_id

    db.session.delete(bloque)
    db.session.commit()

    return redirect(url_for("editar_clase", id=clase_id))
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
