import sqlite3

Conexion=sqlite3.connect("BaseDatos")

Cursor=Conexion.cursor()

Cursor.execute('''
	CREATE TABLE EMERGENCIAS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	AVISO_EFECTUADO VARCHAR(50),
	TELEFONO INTEGER,
	DNI INTEGER(9),
	RECEPCIONADO_POR VARCHAR(16),
	DIRECCION_EMERGENCIA VARCHAR(50),
	ENTRE_CALLES VARCHAR(50),
	LOCALIDAD VARCHAR(50),
	TIPO VARCHAR(500),
	MAGNITUD INTEGER,
	TOQUE_ALARMA VARCHAR(3),
	GENERAL VARCHAR(3),
	RESUMEN VARCHAR(5000))
	''')
	
variosproductos=[
	("Mandaio Julian", 353565443,41323167, "100","100", "100", "100", "100",1, "100", "100", "100"),
	("Mandaio Julian", 353565443,41323167, "100", "100", "100", "100", "100",1, "100", "100", "100")
]

Cursor.executemany("INSERT INTO EMERGENCIAS VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)", variosproductos)

Conexion.commit()

Conexion.close()
