from tkinter import *
from tkinter import filedialog
from tkinter import messagebox, ttk
import tkinter as tk
import sqlite3
import datetime
hora_actual_completa = datetime.datetime.now()
Conexion=sqlite3.connect("BaseDatos")
Cursor=Conexion.cursor()
class ventanas():
	def __init__(self):
	
		def hora():	
			hora = hora_actual_completa.hour  
			minutos = hora_actual_completa.minute 
			segundos = hora_actual_completa.second
			if (len(str(hora))==1):
				hora = "0" + str(hora)
			if (len(str(minutos))==1):
				minutos = "0" + str(minutos)
			if (len(str(segundos))==1):
				segundos = "0" + str(segundos)
			horaActual=str(hora) +":"+ str(minutos) +":"+ str(segundos)
			return horaActual
			
		def check1(TipoSiniestro):
			if (CB11.get()==True):
				TipoSiniestro=TipoSiniestro + "Vivienda\n"
			if (CB12.get()==True):
				TipoSiniestro=TipoSiniestro + "Comercio\n"
			if (CB13.get()==True):
				TipoSiniestro=TipoSiniestro + "Industria\n"
			if (CB14.get()==True):
				TipoSiniestro=TipoSiniestro + "Vehiculo\n"
			if (CB15.get()==True):
				TipoSiniestro=TipoSiniestro + "Campos\n"
			if (CB16.get()==True):
				TipoSiniestro=TipoSiniestro + "Rollos\n"
			if (CB17.get()==True):
				TipoSiniestro=TipoSiniestro + "Otros\n"
		
			if (CB21.get()==True):
				TipoSiniestro=TipoSiniestro + "Urbano\n"
			if (CB22.get()==True):
				TipoSiniestro=TipoSiniestro + "Rural\n"
			if (CB23.get()==True):
				TipoSiniestro=TipoSiniestro + "Automovil\n"
			if (CB24.get()==True):
				TipoSiniestro=TipoSiniestro + "Colectivo\n"
			if (CB25.get()==True):
				TipoSiniestro=TipoSiniestro + "Moto\n"
			if (CB26.get()==True):
				TipoSiniestro=TipoSiniestro + "Tren\n"
			if (CB27.get()==True):
				TipoSiniestro=TipoSiniestro + "Animal\n"
			if (CB28.get()==True):
				TipoSiniestro=TipoSiniestro + "Otros Accidentes\n"
				
			if (CB31.get()==True):
				TipoSiniestro=TipoSiniestro + "Persona\n"
			if (CB32.get()==True):
				TipoSiniestro=TipoSiniestro + "Animal\n"
			if (CB33.get()==True):
				TipoSiniestro=TipoSiniestro + "Vivo\n"
			if (CB34.get()==True):
				TipoSiniestro=TipoSiniestro + "Muerto\n"
			if (CB35.get()==True):
				TipoSiniestro=TipoSiniestro + "Libre\n"
			if (CB36.get()==True):
				TipoSiniestro=TipoSiniestro + "Atrapado\n"
			if (CB37.get()==True):
				TipoSiniestro=TipoSiniestro + "Ahogado\n"
				
			if (CB41.get()==True):
				TipoSiniestro=TipoSiniestro + "Prevencion\n"
			if (CB42.get()==True):
				TipoSiniestro=TipoSiniestro + "Traslado\n"
			if (CB43.get()==True):
				TipoSiniestro=TipoSiniestro + "Arbol Caido\n"
			if (CB44.get()==True):
				TipoSiniestro=TipoSiniestro + "Cable Colgado\n"
			if (CB45.get()==True):
				TipoSiniestro=TipoSiniestro + "Derrumbe\n"
			if (CB46.get()==True):
				TipoSiniestro=TipoSiniestro + "Escape de Gas\n"
			if (CB47.get()==True):
				TipoSiniestro=TipoSiniestro + "Mat-Pel\n"
			if (CB48.get()==True):
				TipoSiniestro=TipoSiniestro + "Abejas/Avispas\n"
			if (CB49.get()==True):
				TipoSiniestro=TipoSiniestro + "Derrame de Combustible\n"
			if (CB411.get()==True):
				TipoSiniestro=TipoSiniestro + "Otros de Otros Servicios\n"
			return TipoSiniestro
		
		def check():
			TipoSiniestro="Tipo de Siniestro: \n" 
			if (CB1.get()==True):
				TipoSiniestro=TipoSiniestro + "INCENDIO\n"
			if (CB2.get()==True):
				TipoSiniestro=TipoSiniestro + "ACCIDENTES\n"
			if (CB3.get()==True):
				TipoSiniestro=TipoSiniestro + "RESCATE\n"
			if (CB4.get()==True):
				TipoSiniestro=TipoSiniestro + "OTROS SERVICIOS\n"
			if (CB5.get()==True):
				TipoSiniestro=TipoSiniestro + "FALSA ALARMA\n"
			TipoSiniestro=check1(TipoSiniestro)
			return TipoSiniestro
			
		def NuevoDocumento(event=None):
			Efectuado.set("")	
			teEfectuado.set("")
			DnEfectuado.set("")
			luSiniestro.set("")
			enCallesSiniestro.set("")
			combo.set("Villa Nueva")
			self.resumenSiniestro.delete(1.0,"end")
			RBAVISO.set(False)
			RBMAGNITUD.set(False)
			RBALARMA.set(False)
			RBSINO.set(False)
			
			CB1.set(False)
			CB2.set(False)
			CB3.set(False)
			CB4.set(False)
			CB5.set(False)
			
			CB11.set(False)
			CB12.set(False)
			CB13.set(False)
			CB14.set(False)
			CB15.set(False)
			CB16.set(False)
			CB17.set(False)
			
			CB21.set(False)
			CB22.set(False)
			CB23.set(False)
			CB24.set(False)
			CB25.set(False)
			CB26.set(False)
			CB27.set(False)
			CB28.set(False)
			
			CB31.set(False)
			CB32.set(False)
			CB33.set(False)
			CB34.set(False)
			CB35.set(False)
			CB36.set(False)
			CB37.set(False)
			
			CB41.set(False)
			CB42.set(False)
			CB43.set(False)
			CB44.set(False)
			CB45.set(False)
			CB46.set(False)
			CB47.set(False)
			CB48.set(False)
			CB49.set(False)
			CB411.set(False)
			
		def GuardarEmergencia(event=None):    
			archivo_guardado=filedialog.asksaveasfilename(initialdir = "/home/toti/Escritorio/Salidas",title = "Select file",defaultextension=".txt",filetypes = (("txt files","*.txt"),("all files","*.*")))
			TipoSiniestro=check()
			file = open(f"{archivo_guardado}", "w")
			file.write("Aviso efectuado por: " + Efectuado.get() + "\n") # + os.linesep
			file.write("Telefono :" + teEfectuado.get()+ "\n")
			file.write("DNI :" + DnEfectuado.get()+ "\n")
			file.write("Recepcionado por: " + str(RBAVISO.get())+ "\n")
			file.write("Lugar de Siniestro: " + luSiniestro.get()+ "\n")
			file.write("Entre Calles: " + enCallesSiniestro.get()+ "\n")
			file.write("En la Ciudad de: " + combo.get()+ "\n")   
			file.write(TipoSiniestro)
			file.write("Magnitud: " + RBMAGNITUD.get()+ "\n")
			file.write("Hubo toque de alarma: " + RBALARMA.get()+ "\n")
			file.write("General: " + RBSINO.get()+ "\n") 
			file.write("Resumen del Siniestro: \n" + self.resumenSiniestro.get(1.0,"end"))
			file.close()
			resumen=self.resumenSiniestro.get(1.0,"end")
			messagebox.showinfo(title="Emergencia Guardada",message="Emergencia Guardada con Exito!")
			
			Conexion=sqlite3.connect("BaseDatos")
			Cursor=Conexion.cursor()
			Cursor.execute(f"INSERT INTO EMERGENCIAS VALUES(NULL,'{Efectuado.get()}', {teEfectuado.get()},{DnEfectuado.get()}, '{RBAVISO.get()}', '{luSiniestro.get()}','{enCallesSiniestro.get()}', 'combo', '{TipoSiniestro}',{RBMAGNITUD.get()}, '{RBALARMA.get()}', '{RBSINO.get()}', '{resumen}')")
			Conexion.commit()
			Conexion.close()
			
		def AbrirEmergencia():
			archivo_abierto=filedialog.askopenfilename(initialdir = "/home/kali/Desktop/GestionBomberos",title = "Seleccione archivo",filetypes = (("all files","*.*"),("Python", "*.py")))
			file = open (f'{archivo_abierto}','r')
			linea=file.readline()
			Efectuado.set(linea[21:])
			for numero, linea in enumerate(file):
				if numero == 0:
					break
			teEfectuado.set(linea[10:])
			for numero, linea in enumerate(file):
				if numero == 0:
					break
			DnEfectuado.set(linea[5:])
			for numero, linea in enumerate(file):
				if numero == 0:
					if linea[18:] == 100:
						RBAVISO.set(value="100")
						break
					elif linea[18:] == 4913388:
						RBAVISO.set(value="4913388")
						break
					elif linea[18:] == "4911716":
						RBAVISO.set(value="4911716")
						break
					elif linea[18:29] == "353-4138833":
						RBAVISO.set(value="353-4138833")
						break
					elif linea[18:] == "Cuartel":
						RBAVISO.set(value="Cuartel")
						break
			for numero, linea in enumerate(file):
				if numero == 0:
					luSiniestro.set(linea[20:])
					break
			for numero, linea in enumerate(file):
				if numero == 0:
					enCallesSiniestro.set(linea[14:])
					break
			for numero, linea in enumerate(file):
				if numero == 0:
					if str(linea[17:28]) == "Villa Nueva":
						combo.set("Villa Nueva")
						break
					elif str(linea[17:28]) == "Villa Maria":
						combo.set("Villa Maria")
						break
					elif str(linea[17:24]) == "Cordoba":
						combo.set("Cordoba")
						break
					elif str(linea[17:21]) == "Otro":
						combo.set("Otro")
						break
			self.resumenSiniestro.delete(1.0,"end")
			RBMAGNITUD.set(False)
			RBALARMA.set(False)
			RBSINO.set(False)
			
			for numero, linea in enumerate(file):
				if numero == 1 :
					if str(linea[0:8]) == "INCENDIO":
						CB1.set(True)
						break
					elif str(linea[0:8]) == "Vivienda":
						CB2.set(True)
				#print(numero)
			#asd=file.readlines()
			#if asd in 'INCENDIO'):
			#	CB2.set(True)
			#	print("hola")
				
			CB3.set(False)
			CB4.set(False)
			CB5.set(False)
			
			CB11.set(False)
			CB12.set(False)
			CB13.set(False)
			CB14.set(False)
			CB15.set(False)
			CB16.set(False)
			CB17.set(False)
			
			CB21.set(False)
			CB22.set(False)
			CB23.set(False)
			CB24.set(False)
			CB25.set(False)
			CB26.set(False)
			CB27.set(False)
			CB28.set(False)
			
			CB31.set(False)
			CB32.set(False)
			CB33.set(False)
			CB34.set(False)
			CB35.set(False)
			CB36.set(False)
			CB37.set(False)
			
			CB41.set(False)
			CB42.set(False)
			CB43.set(False)
			CB44.set(False)
			CB45.set(False)
			CB46.set(False)
			CB47.set(False)
			CB48.set(False)
			CB49.set(False)
			CB411.set(False)
			file.close()
		
		def salir(event):
			self.destroy()
	
		self=tk.Tk()
		self.title("Gestion de Emergencias")		
		wventana=1370
		hventana=750
		wtotal = self.winfo_screenwidth()
		htotal = self.winfo_screenheight()
		pwidth = round(wtotal/2-wventana/2)
		pheight = round(htotal/2-hventana/2)
		#self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
		self.resizable(0,0)
		self.attributes("-fullscreen",True)
		
		#COMBOBOX
		combo = ttk.Combobox(values=["Villa Nueva", "Villa Maria", "Cordoba", "Otro"],state="readonly")
		combo.set("Villa Nueva")
		#combo.bind("<<ComboboxSelected>>", GuardarEmergencia)
		combo.place(x=725, y=130)
		
		##########################################################
		#BARRA MENUS
		##########################################################
		
		barra_menus = tk.Menu()  # Insertarla en la ventana principal.
		
		##########################################################
		#MENUS
		##########################################################
		
		menu_Menu = tk.Menu(barra_menus, tearoff=False)
		
		menu_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=NuevoDocumento,)
		self.bind_all("<Control-n>", NuevoDocumento)	
		
		menu_Menu.add_command(label="Guardar", accelerator="Ctrl+G", command=GuardarEmergencia,)
		self.bind_all("<Control-g>", GuardarEmergencia)
		
		menu_Menu.add_command(label="Modificar", accelerator="Ctrl+M", command=AbrirEmergencia,)
		self.bind_all("<Control-m>", AbrirEmergencia)
		
		menu_Menu.add_separator()
		
		menu_Menu.add_command(label="Salir", accelerator="Ctrl+Z", command=self.destroy)
		self.bind_all("<Control-z>", salir)
		
		
		menu_opciones = tk.Menu(barra_menus, tearoff=False)
		iniciar_con_sistema = tk.BooleanVar()
		menu_opciones.add_checkbutton(label="Iniciar con sistema",command=NuevoDocumento,variable=iniciar_con_sistema)
		menu_Sanciones = tk.Menu(barra_menus, tearoff=False)
		menu_Cursos = tk.Menu(barra_menus, tearoff=False)
		menu_Inventario = tk.Menu(barra_menus, tearoff=False)
		menu_Bombero = tk.Menu(barra_menus, tearoff=False)
		menu_ListadoEmergencia = tk.Menu(barra_menus, tearoff=False)
		menu_ElementosReparacion = tk.Menu(barra_menus, tearoff=False)
		menu_Archivo = tk.Menu(barra_menus, tearoff=False)
		
		##########################################################
		#FIN MENUS
		##########################################################
		
		##########################################################
		#SUBMENUS
		##########################################################
		
		menu_tema = tk.Menu(barra_menus, tearoff=False)
		tema_elegido = tk.IntVar()
		tema_elegido.set(1)  # Opción seleccionada por defecto ("Claro").
		menu_tema.add_radiobutton(label="Claro",variable=tema_elegido,value=1,command=GuardarEmergencia)
		menu_tema.add_radiobutton(label="Oscuro",value=2,variable=tema_elegido, command=NO)
		
		##########################################################
		#SUBMENU EQUIPAMENTO
		##########################################################
		
		menu_Equipamento = tk.Menu(barra_menus, tearoff=False)
		menu_Equipamento.add_command(label="En Uso",command=self.destroy)
		menu_Equipamento.add_command(label="En Desuso",command=self.destroy)
		menu_Equipamento.add_command(label="En Reparacion",command=self.destroy)
		
		##########################################################
		#FIN SUBMENU EQUIPAMENTO
		##########################################################
		
		menu_Archivo.add_cascade(menu=menu_tema, label="Tema")
		menu_opciones.add_cascade(menu=menu_tema, label="Tema")
		menu_Cursos.add_command(label="Primer Nivel", command=AbrirEmergencia)
		menu_Cursos.add_command(label="Segundo Nivel", command=self.destroy)
		menu_Cursos.add_command(label="Tercer Nivel", command=self.destroy)
		menu_Inventario.add_cascade(menu=menu_Equipamento, label="Equipamentos")
		menu_Inventario.add_cascade(menu=menu_Equipamento, label="Vehiculos")
		menu_Inventario.add_cascade(menu=menu_Equipamento, label="Materiales")
		menu_Bombero.add_command(label="Listado de Bomberos", command=self.destroy)
		menu_Bombero.add_command(label="Sanciones", command=salir)
		menu_ListadoEmergencia.add_cascade(menu=menu_tema, label="Tema")
		menu_ElementosReparacion.add_cascade(menu=menu_tema, label="Tema")
		
		##########################################################
		#FIN SUBMENUS
		##########################################################
		
		##########################################################
		#MENU COMPLETO
		##########################################################
		
		barra_menus.add_cascade(menu=menu_Menu, label="Menu")
		barra_menus.add_cascade(menu=menu_Archivo, label="Archivo")
		barra_menus.add_cascade(menu=menu_Cursos, label="Cursos")
		barra_menus.add_cascade(menu=menu_Inventario, label="Inventario")
		barra_menus.add_cascade(menu=menu_Bombero, label="Bomberos")
		barra_menus.add_cascade(menu=menu_ListadoEmergencia, label="Listado de Emergencias")
		barra_menus.add_cascade(menu=menu_ElementosReparacion, label="Elementos en Reparacion")
		barra_menus.add_cascade(menu=menu_opciones, label="Opciones")
		
		##########################################################
		#FIN MENU COMPLETO
		##########################################################
		
		self.config(menu=barra_menus)
		
		##########################################################
		#FIN CONFIGURACION MENU
		##########################################################
			
		##########################################################
		#SEPARADORES
		##########################################################
		
		ttk.Separator(self,orient="horizontal").place(x=10,y=25,width=9990,height=2)
		ttk.Separator(self,orient="vertical").place(x=900,y=25,width=1,height=50)
		ttk.Separator(self,orient="horizontal").place(x=10,y=75,width=9990,height=2)
		ttk.Separator(self,orient="horizontal").place(x=10,y=170,width=9990,height=2)
		ttk.Separator(self,orient="vertical").place(x=750,y=170,width=1,height=250)
		ttk.Separator(self,orient="horizontal").place(x=10,y=420,width=9990,height=2)
		
		##########################################################
		#FIN SEPARADORES
		##########################################################
		
		##########################################################
		#LABELS
		##########################################################

		Label(self, text="¡Bienvenido!").pack() 
		Label(self, text="Aviso efectuado por: ").place(x=10,y=40)
		Label(self, text="Telefono: ").place(x=355,y=40)
		Label(self, text="DNI: ").place(x=630,y=40)
		Label(self, text="Hora Actual: " + hora()).place(x=910,y=40)
		Label(self, text="Recepcionado por: ").place(x=10,y=90)
		Label(self,text="Lugar de Siniestro: ").place(x=10,y=130)
		Label(self,text="Entre calles: ").place(x=350,y=130)
		Label(self,text="Localidad: ").place(x=650,y=130)
		Label(self, text="Magnitud: ").place(x=760,y=200)
		Label(self, text="Toque de Alarma: ").place(x=760,y=230)
		Label(self, text="General: ").place(x=760,y=260)
		Label(self, text="RESUMEN: ").place(x=20,y=430)

		##########################################################
		#FIN LABELS
		##########################################################
		
		##########################################################
		#TEXTS
		##########################################################

		Efectuado=tk.StringVar()
		textEfectuado=tk.Entry(self,textvariable=Efectuado).place(x=150,y=35, width=200,height=30)
		teEfectuado=tk.StringVar()
		telEfectuado=tk.Entry(self,textvariable=teEfectuado).place(x=425,y=35, width=200, height=30)
		DnEfectuado=tk.StringVar()
		DniEfectuado=tk.Entry(self,textvariable=DnEfectuado).place(x=670,y=35, width=200, height=30)
		luSiniestro=tk.StringVar()
		lugSiniestro=tk.Entry(self,textvariable=luSiniestro).place(x=140,y=125,width=200,height=30)
		enCallesSiniestro=tk.StringVar()
		entreCalleSiniestro=tk.Entry(self,textvariable=enCallesSiniestro).place(x=440,y=125,width=200,height=30)
		self.resumenSiniestro=tk.Text(self)
		self.resumenSiniestro.place(x=20,y=450, width=1330, height=240)

		##########################################################
		#FIN TEXTS
		##########################################################
		
		##########################################################
		#BOTON
		##########################################################
		
		boton = ttk.Button(text="Guardar Emergencia", command=GuardarEmergencia)
		boton.bind("<Return>", GuardarEmergencia)
		boton.place(x=1200, y=700)
		
		##########################################################
		#FIN BOTON
		##########################################################
		
		##########################################################
		#RADIOBUTTON
		##########################################################
		
		RBAVISO=tk.StringVar()
		RBAVISO.set(None)
		RB100=Radiobutton(self, text="100",variable=RBAVISO,value="100").place(x=140,y=90)
		RB4913388=Radiobutton(self, text="Tel: 4913388",variable=RBAVISO,value="4913388").place(x=200,y=90)
		RB4911716=Radiobutton(self, text="Tel: 4911716",variable=RBAVISO,value="4911716").place(x=320,y=90)
		RB3534138833=Radiobutton(self, text="Cel: 353-4138833",variable=RBAVISO,value="353-4138833").place(x=440,y=90)
		RBCuartel=Radiobutton(self,text="Cuartel",variable=RBAVISO,value="Cuartel").place(x=590,y=90)
		RBMAGNITUD=tk.StringVar()
		RBMAGNITUD.set(None)
		RBMagnitud1=Radiobutton(self, text="1",variable=RBMAGNITUD,value="1").place(x=830,y=200)
		RBMagnitud2=Radiobutton(self, text="2",variable=RBMAGNITUD,value="2").place(x=880,y=200)
		RBMagnitud3=Radiobutton(self, text="3",variable=RBMAGNITUD,value="3").place(x=930,y=200)
		RBALARMA=tk.StringVar()
		RBALARMA.set(None)
		RBToqueAlarmaSi=Radiobutton(self, text="Si",variable=RBALARMA,value="Si").place(x=880,y=230)
		RBToqueAlarmaNo=Radiobutton(self, text="No",variable=RBALARMA,value="No").place(x=930,y=230)
		RBSINO=tk.StringVar()
		RBSINO.set(None)
		RBToqueAlarmaSi=Radiobutton(self, text="Si",variable=RBSINO, value="Si" ).place(x=830,y=260)
		RBToqueAlarmaNo=Radiobutton(self, text="No",variable=RBSINO, value="No" ).place(x=880,y=260)
	
		##########################################################
		#FIN RADIOBUTTON
		##########################################################
		
		##########################################################
		#CHECKBOX PRINCIPAL
		##########################################################
		
		CB1=tk.BooleanVar()
		CB1.set(False)
		cb1=ttk.Checkbutton(self, text="INCENDIO",variable=CB1)
		cb1.place(x=20,y=190)
		CB2=tk.BooleanVar()
		CB2.set(False)
		cb2=ttk.Checkbutton(self, text="ACCIDENTES",variable=CB2)
		cb2.place(x=140,y=190)
		CB3=tk.BooleanVar()
		CB3.set(False)
		cb3=ttk.Checkbutton(self, text="RESCATE",variable=CB3)
		cb3.place(x=270,y=190)
		CB4=tk.BooleanVar()
		CB4.set(False)
		cb4=ttk.Checkbutton(self, text="OTROS SERVICIOS",variable=CB4)
		cb4.place(x=380,y=190)
		CB5=tk.BooleanVar()
		CB5.set(False)
		cb5=ttk.Checkbutton(self, text="FALSA ALARMA",variable=CB5)
		cb5.place(x=590,y=190)
		
		##########################################################
		#FIN CHECKBOX PRINCIPAL
		##########################################################
		
		##########################################################
		#CHECKBOX SECUNDARIO
		##########################################################
		
		CB11=tk.BooleanVar()
		CB11.set(False)
		cb11=ttk.Checkbutton(self, text="Vivienda",variable=CB11)
		cb11.place(x=30,y=210)
		CB12=tk.BooleanVar()
		CB12.set(False)
		cb12=ttk.Checkbutton(self, text="Comercio",variable=CB12)
		cb12.place(x=30,y=230)
		CB13=tk.BooleanVar()
		CB13.set(False)
		cb13=ttk.Checkbutton(self, text="Industria",variable=CB13)
		cb13.place(x=30,y=250)
		CB14=tk.BooleanVar()
		CB14.set(False)
		cb14=ttk.Checkbutton(self, text="Vehiculo",variable=CB14)
		cb14.place(x=30,y=270)
		CB15=tk.BooleanVar()
		CB15.set(False)
		cb15=ttk.Checkbutton(self, text="Campos",variable=CB15)
		cb15.place(x=30,y=290)
		CB16=tk.BooleanVar()
		CB16.set(False)
		cb16=ttk.Checkbutton(self, text="Rollos",variable=CB16)
		cb16.place(x=30,y=310)
		CB17=tk.BooleanVar()
		CB17.set(False)
		cb17=ttk.Checkbutton(self, text="Otros",variable=CB17)
		cb17.place(x=30,y=330)
		
		CB21=tk.BooleanVar()
		CB21.set(False)
		cb21=ttk.Checkbutton(self, text="Urbano",variable=CB21)
		cb21.place(x=150,y=210)
		CB22=tk.BooleanVar()
		CB22.set(False)
		cb22=ttk.Checkbutton(self, text="Rural",variable=CB22)
		cb22.place(x=150,y=230)
		CB23=tk.BooleanVar()
		CB23.set(False)
		cb23=ttk.Checkbutton(self, text="Automovil",variable=CB23)
		cb23.place(x=150,y=250)
		CB24=tk.BooleanVar()
		CB24.set(False)
		cb24=ttk.Checkbutton(self, text="Colectivo",variable=CB24)
		cb24.place(x=150,y=270)
		CB25=tk.BooleanVar()
		CB25.set(False)
		cb25=ttk.Checkbutton(self, text="Moto",variable=CB25)
		cb25.place(x=150,y=290)
		CB26=tk.BooleanVar()
		CB26.set(False)
		cb26=ttk.Checkbutton(self, text="Tren",variable=CB26)
		cb26.place(x=150,y=310)
		CB27=tk.BooleanVar()
		CB27.set(False)
		cb27=ttk.Checkbutton(self, text="Animal",variable=CB27)
		cb27.place(x=150,y=330)
		CB28=tk.BooleanVar()
		CB28.set(False)
		cb28=ttk.Checkbutton(self, text="Otros",variable=CB28)
		cb28.place(x=150,y=350)
		
		CB31=tk.BooleanVar()
		CB31.set(False)
		cb31=ttk.Checkbutton(self, text="Persona",variable=CB31)
		cb31.place(x=280,y=210)
		CB32=tk.BooleanVar()
		CB32.set(False)
		cb32=ttk.Checkbutton(self, text="Animal",variable=CB32)
		cb32.place(x=280,y=230)
		CB33=tk.BooleanVar()
		CB33.set(False)
		cb33=ttk.Checkbutton(self, text="Vivo",variable=CB33)
		cb33.place(x=280,y=250)
		CB34=tk.BooleanVar()
		CB34.set(False)
		cb34=ttk.Checkbutton(self, text="Muerto",variable=CB34)
		cb34.place(x=280,y=270)
		CB35=tk.BooleanVar()
		CB35.set(False)
		cb35=ttk.Checkbutton(self, text="Libre",variable=CB35)
		cb35.place(x=280,y=290)
		CB36=tk.BooleanVar()
		CB36.set(False)
		cb36=ttk.Checkbutton(self, text="Atrapado",variable=CB36)
		cb36.place(x=280,y=310)
		CB37=tk.BooleanVar()
		CB37.set(False)
		cb37=ttk.Checkbutton(self, text="Ahogado",variable=CB37)
		cb37.place(x=280,y=330)
		
		CB41=tk.BooleanVar()
		CB41.set(False)
		cb41=ttk.Checkbutton(self, text="Prevencion",variable=CB41)
		cb41.place(x=390,y=210)
		CB42=tk.BooleanVar()
		CB42.set(False)
		cb42=ttk.Checkbutton(self, text="Traslado",variable=CB42)
		cb42.place(x=390,y=230)
		CB43=tk.BooleanVar()
		CB43.set(False)
		cb43=ttk.Checkbutton(self, text="Arbol Caido",variable=CB43)
		cb43.place(x=390,y=250)
		CB44=tk.BooleanVar()
		CB44.set(False)
		cb44=ttk.Checkbutton(self, text="Cable 	Colgado",variable=CB44)
		cb44.place(x=390,y=270)
		CB45=tk.BooleanVar()
		CB45.set(False)
		cb45=ttk.Checkbutton(self, text="Derrumbe",variable=CB45)
		cb45.place(x=390,y=290)
		CB46=tk.BooleanVar()
		CB46.set(False)
		cb46=ttk.Checkbutton(self, text="Escape de Gas",variable=CB46)
		cb46.place(x=390,y=310)
		CB47=tk.BooleanVar()
		CB47.set(False)
		cb47=ttk.Checkbutton(self, text="Mat-Pel",variable=CB47)
		cb47.place(x=390,y=330)
		CB48=tk.BooleanVar()
		CB48.set(False)
		cb48=ttk.Checkbutton(self, text="Abejas/Avispas",variable=CB48)
		cb48.place(x=390,y=350)
		CB49=tk.BooleanVar()
		CB49.set(False)
		cb49=ttk.Checkbutton(self, text="Derrame de Combustible",variable=CB49)
		cb49.place(x=390,y=370)
		CB411=tk.BooleanVar()
		CB411.set(False)
		cb411=ttk.Checkbutton(self, text="Otros",variable=CB411)
		cb411.place(x=390,y=390)
		
		##########################################################
		#FIN CHECKBOX SECUNDARIO
		##########################################################
		self.mainloop()
Conexion.close()

ventanaPrincipal=ventanas()






