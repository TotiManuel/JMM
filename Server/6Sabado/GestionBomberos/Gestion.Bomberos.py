"""
Fecha:31/12/2022

Autor: Julian Manuel Mandaio

Lenguaje: Python

Desimantación: Gestion de Emergencias de los Bomberos de Villa Nueva

Función principal: Gestionar la Informacion de las Emergencias Ocurridas

Objetivo: Mejor Gestion de Emergencias
"""

import os
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as BVVN
import datetime

##########################################################
#CONFIGURACION VENTANA
##########################################################

ventana=BVVN.Tk()
ventana.title("Gestion de Emergencias")
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
wventana=1370
hventana=750
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
# ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
#ventana.config(bg="blue")

ventana.resizable(0,0)

ventana.attributes("-fullscreen",True)

##########################################################
#FIN CONFIGURACION VENTANA
##########################################################

##########################################################
#FUNCIONES
##########################################################

hora_actual_completa = datetime.datetime.now()

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

def GuardarEmergencia(event=None):    
	TipoSiniestro=check()
	file = open("Registros de emergencias.txt", "w")
	file.write("Aviso efectuado por: " + Efectuado.get() + "\n") # + os.linesep
	file.write("Telefono de " + Efectuado.get() + ": " + teEfectuado.get()+ "\n")
	file.write("DNI de " + Efectuado.get() + ": " + DnEfectuado.get()+ "\n")
	file.write("Recepcionado por: " + RBAVISO.get()+ "\n")
	file.write("Lugar de Siniestro: " + luSiniestro.get()+ "\n")
	file.write("Entre Calles: " + enCallesSiniestro.get()+ "\n")
	file.write("En la Ciudad de: " + combo.get()+ "\n")   
	file.write(TipoSiniestro)
	file.write("Magnitud: " + RBMAGNITUD.get()+ "\n")
	file.write("Hubo toque de alarma: " + RBALARMA.get()+ "\n")
	file.write("General: " + RBSINO.get()+ "\n") 
	file.write("Resumen del Siniestro: \n" + resumenSiniestro.get(1.0,"end"))
	file.close()
	messagebox.showinfo(title="Emergencia Guardada",message="Emergencia Guardada con Exito!")

def NuevoDocumento(event):
	Efectuado.set("")	
	teEfectuado.set("")
	DnEfectuado.set("")
	luSiniestro.set("")
	enCallesSiniestro.set("")
	combo.set("Villa Nueva")
	resumenSiniestro.delete(1.0,"end")
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

def menu_tema_presionado():
	valor_tema = tema_elegido.get()
	if valor_tema == 1:
		print("Tema claro establecido.")
	elif valor_tema == 2:
		print("Tema oscuro establecido.")
		
def salir(event):
	ventana.destroy()
	
def San():	
	ventanaSaciones=BVVN.Tk() 
	ventanaSaciones.title("Sanciones") 
	wtotal = ventanaSaciones.winfo_screenwidth()
	htotal = ventanaSaciones.winfo_screenheight()
	wventanaSaciones=500
	hventanaSaciones=500
	pwidth = round(wtotal/2-wventanaSaciones/2)
	pheight = round(htotal/2-hventanaSaciones/2)
	ventanaSaciones.geometry(str(wventanaSaciones)+"x"+str(hventanaSaciones)+"+"+str(pwidth)+"+"+str(pheight))
	#ventana.config(bg="blue") 
	ventana.resizable(0,0) 
	ventana.attributes("-fullscreen",False)

#COMBOBOX

combo = ttk.Combobox(values=["Villa Nueva", "Villa Maria", "Cordoba", "Otro"],state="readonly")
combo.set("Villa Nueva")
combo.bind("<<ComboboxSelected>>", GuardarEmergencia)
combo.place(x=725, y=130)

##########################################################
#FIN FUNCIONES
##########################################################

##########################################################
#LABELS
##########################################################

Label(ventana, text="¡Bienvenido!").pack() 
Label(ventana, text="Aviso efectuado por: ").place(x=10,y=40)
Label(ventana, text="Telefono: ").place(x=355,y=40)
Label(ventana, text="DNI: ").place(x=630,y=40)
hola=Label(ventana, text="Hora Actual: " + hora()).place(x=910,y=40)
Label(ventana, text="Recepcionado por: ").place(x=10,y=90)
Label(ventana,text="Lugar de Siniestro: ").place(x=10,y=130)
Label(ventana,text="Entre calles: ").place(x=350,y=130)
Label(ventana,text="Localidad: ").place(x=650,y=130)
Label(ventana, text="Magnitud: ").place(x=760,y=200)
Label(ventana, text="Toque de Alarma: ").place(x=760,y=230)
Label(ventana, text="General: ").place(x=760,y=260)
Label(ventana, text="RESUMEN: ").place(x=20,y=430)


##########################################################
#FIN LABELS
##########################################################

##########################################################
#TEXTS
##########################################################

Efectuado=BVVN.StringVar()
textEfectuado=BVVN.Entry(ventana,textvariable=Efectuado).place(x=150,y=35, width=200, height=30)
teEfectuado=BVVN.StringVar()
telEfectuado=BVVN.Entry(ventana,textvariable=teEfectuado).place(x=425,y=35, width=200, height=30)
DnEfectuado=BVVN.StringVar()
DniEfectuado=BVVN.Entry(ventana,textvariable=DnEfectuado).place(x=670,y=35, width=200, height=30)
luSiniestro=BVVN.StringVar()
lugSiniestro=BVVN.Entry(ventana,textvariable=luSiniestro).place(x=140,y=125,width=200,height=30)
enCallesSiniestro=BVVN.StringVar()
entreCalleSiniestro=BVVN.Entry(ventana,textvariable=enCallesSiniestro).place(x=440,y=125,width=200,height=30)
resumenSiniestro=BVVN.Text(ventana)
resumenSiniestro.place(x=20,y=450, width=1330, height=240)

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

RBAVISO=BVVN.StringVar()
RBAVISO.set(None)
RB100=Radiobutton(ventana, text="100",variable=RBAVISO,value="100").place(x=140,y=90)
RB4913388=Radiobutton(ventana, text="Tel: 4913388",variable=RBAVISO,value="4913388").place(x=200,y=90)
RB4911716=Radiobutton(ventana, text="Tel: 4911716",variable=RBAVISO,value="4911716").place(x=320,y=90)
RB3534138833=Radiobutton(ventana, text="Cel: 353-4138833",variable=RBAVISO,value="353-4138833").place(x=440,y=90)
RBCuartel=Radiobutton(ventana,text="Cuartel",variable=RBAVISO,value="Cuartel").place(x=590,y=90)
RBMAGNITUD=BVVN.StringVar()
RBMAGNITUD.set(None)
RBMagnitud1=Radiobutton(ventana, text="1",variable=RBMAGNITUD,value="1").place(x=830,y=200)
RBMagnitud2=Radiobutton(ventana, text="2",variable=RBMAGNITUD,value="2").place(x=880,y=200)
RBMagnitud3=Radiobutton(ventana, text="3",variable=RBMAGNITUD,value="3").place(x=930,y=200)
RBALARMA=BVVN.StringVar()
RBALARMA.set(None)
RBToqueAlarmaSi=Radiobutton(ventana, text="Si",variable=RBALARMA,value="Si").place(x=880,y=230)
RBToqueAlarmaNo=Radiobutton(ventana, text="No",variable=RBALARMA,value="No").place(x=930,y=230)
RBSINO=BVVN.StringVar()
RBSINO.set(None)
RBToqueAlarmaSi=Radiobutton(ventana, text="Si",variable=RBSINO, value="Si" ).place(x=830,y=260)
RBToqueAlarmaNo=Radiobutton(ventana, text="No",variable=RBSINO, value="No" ).place(x=880,y=260)

##########################################################
#FIN RADIOBUTTON
##########################################################

##########################################################
#SEPARADORES
##########################################################

ttk.Separator(ventana,orient="horizontal").place(x=10,y=25,width=9990,height=2)
ttk.Separator(ventana,orient="vertical").place(x=900,y=25,width=1,height=50)
ttk.Separator(ventana,orient="horizontal").place(x=10,y=75,width=9990,height=2)
ttk.Separator(ventana,orient="horizontal").place(x=10,y=170,width=9990,height=2)
ttk.Separator(ventana,orient="vertical").place(x=750,y=170,width=1,height=250)
ttk.Separator(ventana,orient="horizontal").place(x=10,y=420,width=9990,height=2)

##########################################################
#FIN SEPARADORES
##########################################################

##########################################################
#BARRA MENUS
##########################################################

barra_menus = BVVN.Menu()  # Insertarla en la ventana principal.

##########################################################
#MENUS
##########################################################

menu_Menu = BVVN.Menu(barra_menus, tearoff=False)

menu_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=NuevoDocumento,)
ventana.bind_all("<Control-n>", NuevoDocumento)	

menu_Menu.add_command(label="Guardar", accelerator="Ctrl+G", command=GuardarEmergencia,)
ventana.bind_all("<Control-g>", GuardarEmergencia)
menu_Menu.add_separator()

menu_Menu.add_command(label="Salir", accelerator="Ctrl+Z", command=ventana.destroy)
ventana.bind_all("<Control-z>", salir)


menu_opciones = BVVN.Menu(barra_menus, tearoff=False)
iniciar_con_sistema = BVVN.BooleanVar()
menu_opciones.add_checkbutton(label="Iniciar con sistema",command=NuevoDocumento,variable=iniciar_con_sistema)
menu_Sanciones = BVVN.Menu(barra_menus, tearoff=False)
menu_Cursos = BVVN.Menu(barra_menus, tearoff=False)
menu_Inventario = BVVN.Menu(barra_menus, tearoff=False)
menu_Bombero = BVVN.Menu(barra_menus, tearoff=False)
menu_ListadoEmergencia = BVVN.Menu(barra_menus, tearoff=False)
menu_ElementosReparacion = BVVN.Menu(barra_menus, tearoff=False)
menu_Archivo = BVVN.Menu(barra_menus, tearoff=False)

##########################################################
#FIN MENUS
##########################################################

##########################################################
#SUBMENUS
##########################################################

menu_tema = BVVN.Menu(barra_menus, tearoff=False)
tema_elegido = BVVN.IntVar()
tema_elegido.set(1)  # Opción seleccionada por defecto ("Claro").
menu_tema.add_radiobutton(label="Claro",variable=tema_elegido,value=1,command=GuardarEmergencia)
menu_tema.add_radiobutton(label="Oscuro",value=2,variable=tema_elegido, command=menu_tema_presionado)

##########################################################
#SUBMENU EQUIPAMENTO
##########################################################

menu_Equipamento = BVVN.Menu(barra_menus, tearoff=False)
menu_Equipamento.add_command(label="En Uso",command=ventana.destroy)
menu_Equipamento.add_command(label="En Desuso",command=ventana.destroy)
menu_Equipamento.add_command(label="En Reparacion",command=ventana.destroy)

##########################################################
#FIN SUBMENU EQUIPAMENTO
##########################################################

menu_Archivo.add_cascade(menu=menu_tema, label="Tema")
menu_opciones.add_cascade(menu=menu_tema, label="Tema")
menu_Cursos.add_command(label="Primer Nivel", command=ventana.destroy)
menu_Cursos.add_command(label="Segundo Nivel", command=ventana.destroy)
menu_Cursos.add_command(label="Tercer Nivel", command=ventana.destroy)
menu_Inventario.add_cascade(menu=menu_Equipamento, label="Equipamentos")
menu_Inventario.add_cascade(menu=menu_Equipamento, label="Vehiculos")
menu_Inventario.add_cascade(menu=menu_Equipamento, label="Materiales")
menu_Bombero.add_command(label="Listado de Bomberos", command=ventana.destroy)
menu_Bombero.add_command(label="Sanciones", command=San)
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

ventana.config(menu=barra_menus)

##########################################################
#FIN CONFIGURACION VENTANA
##########################################################

##########################################################
#CHECKBOX PRINCIPAL
##########################################################

CB1=BVVN.BooleanVar()
CB1.set(False)
cb1=ttk.Checkbutton(ventana, text="INCENDIO",variable=CB1)
cb1.place(x=20,y=190)
CB2=BVVN.BooleanVar()
CB2.set(False)
cb2=ttk.Checkbutton(ventana, text="ACCIDENTES",variable=CB2)
cb2.place(x=140,y=190)
CB3=BVVN.BooleanVar()
CB3.set(False)
cb3=ttk.Checkbutton(ventana, text="RESCATE",variable=CB3)
cb3.place(x=270,y=190)
CB4=BVVN.BooleanVar()
CB4.set(False)
cb4=ttk.Checkbutton(ventana, text="OTROS SERVICIOS",variable=CB4)
cb4.place(x=380,y=190)
CB5=BVVN.BooleanVar()
CB5.set(False)
cb5=ttk.Checkbutton(ventana, text="FALSA ALARMA",variable=CB5)
cb5.place(x=590,y=190)

##########################################################
#FIN CHECKBOX PRINCIPAL
##########################################################

##########################################################
#CHECKBOX SECUNDARIO
##########################################################

CB11=BVVN.BooleanVar()
CB11.set(False)
cb11=ttk.Checkbutton(ventana, text="Vivienda",variable=CB11)
cb11.place(x=30,y=210)
CB12=BVVN.BooleanVar()
CB12.set(False)
cb12=ttk.Checkbutton(ventana, text="Comercio",variable=CB12)
cb12.place(x=30,y=230)
CB13=BVVN.BooleanVar()
CB13.set(False)
cb13=ttk.Checkbutton(ventana, text="Industria",variable=CB13)
cb13.place(x=30,y=250)
CB14=BVVN.BooleanVar()
CB14.set(False)
cb14=ttk.Checkbutton(ventana, text="Vehiculo",variable=CB14)
cb14.place(x=30,y=270)
CB15=BVVN.BooleanVar()
CB15.set(False)
cb15=ttk.Checkbutton(ventana, text="Campos",variable=CB15)
cb15.place(x=30,y=290)
CB16=BVVN.BooleanVar()
CB16.set(False)
cb16=ttk.Checkbutton(ventana, text="Rollos",variable=CB16)
cb16.place(x=30,y=310)
CB17=BVVN.BooleanVar()
CB17.set(False)
cb17=ttk.Checkbutton(ventana, text="Otros",variable=CB17)
cb17.place(x=30,y=330)

CB21=BVVN.BooleanVar()
CB21.set(False)
cb21=ttk.Checkbutton(ventana, text="Urbano",variable=CB21)
cb21.place(x=150,y=210)
CB22=BVVN.BooleanVar()
CB22.set(False)
cb22=ttk.Checkbutton(ventana, text="Rural",variable=CB22)
cb22.place(x=150,y=230)
CB23=BVVN.BooleanVar()
CB23.set(False)
cb23=ttk.Checkbutton(ventana, text="Automovil",variable=CB23)
cb23.place(x=150,y=250)
CB24=BVVN.BooleanVar()
CB24.set(False)
cb24=ttk.Checkbutton(ventana, text="Colectivo",variable=CB24)
cb24.place(x=150,y=270)
CB25=BVVN.BooleanVar()
CB25.set(False)
cb25=ttk.Checkbutton(ventana, text="Moto",variable=CB25)
cb25.place(x=150,y=290)
CB26=BVVN.BooleanVar()
CB26.set(False)
cb26=ttk.Checkbutton(ventana, text="Tren",variable=CB26)
cb26.place(x=150,y=310)
CB27=BVVN.BooleanVar()
CB27.set(False)
cb27=ttk.Checkbutton(ventana, text="Animal",variable=CB27)
cb27.place(x=150,y=330)
CB28=BVVN.BooleanVar()
CB28.set(False)
cb28=ttk.Checkbutton(ventana, text="Otros",variable=CB28)
cb28.place(x=150,y=350)

CB31=BVVN.BooleanVar()
CB31.set(False)
cb31=ttk.Checkbutton(ventana, text="Persona",variable=CB31)
cb31.place(x=280,y=210)
CB32=BVVN.BooleanVar()
CB32.set(False)
cb32=ttk.Checkbutton(ventana, text="Animal",variable=CB32)
cb32.place(x=280,y=230)
CB33=BVVN.BooleanVar()
CB33.set(False)
cb33=ttk.Checkbutton(ventana, text="Vivo",variable=CB33)
cb33.place(x=280,y=250)
CB34=BVVN.BooleanVar()
CB34.set(False)
cb34=ttk.Checkbutton(ventana, text="Muerto",variable=CB34)
cb34.place(x=280,y=270)
CB35=BVVN.BooleanVar()
CB35.set(False)
cb35=ttk.Checkbutton(ventana, text="Libre",variable=CB35)
cb35.place(x=280,y=290)
CB36=BVVN.BooleanVar()
CB36.set(False)
cb36=ttk.Checkbutton(ventana, text="Atrapado",variable=CB36)
cb36.place(x=280,y=310)
CB37=BVVN.BooleanVar()
CB37.set(False)
cb37=ttk.Checkbutton(ventana, text="Ahogado",variable=CB37)
cb37.place(x=280,y=330)

CB41=BVVN.BooleanVar()
CB41.set(False)
cb41=ttk.Checkbutton(ventana, text="Prevencion",variable=CB41)
cb41.place(x=390,y=210)
CB42=BVVN.BooleanVar()
CB42.set(False)
cb42=ttk.Checkbutton(ventana, text="Traslado",variable=CB42)
cb42.place(x=390,y=230)
CB43=BVVN.BooleanVar()
CB43.set(False)
cb43=ttk.Checkbutton(ventana, text="Arbol Caido",variable=CB43)
cb43.place(x=390,y=250)
CB44=BVVN.BooleanVar()
CB44.set(False)
cb44=ttk.Checkbutton(ventana, text="Cable Colgado",variable=CB44)
cb44.place(x=390,y=270)
CB45=BVVN.BooleanVar()
CB45.set(False)
cb45=ttk.Checkbutton(ventana, text="Derrumbe",variable=CB45)
cb45.place(x=390,y=290)
CB46=BVVN.BooleanVar()
CB46.set(False)
cb46=ttk.Checkbutton(ventana, text="Escape de Gas",variable=CB46)
cb46.place(x=390,y=310)
CB47=BVVN.BooleanVar()
CB47.set(False)
cb47=ttk.Checkbutton(ventana, text="Mat-Pel",variable=CB47)
cb47.place(x=390,y=330)
CB48=BVVN.BooleanVar()
CB48.set(False)
cb48=ttk.Checkbutton(ventana, text="Abejas/Avispas",variable=CB48)
cb48.place(x=390,y=350)
CB49=BVVN.BooleanVar()
CB49.set(False)
cb49=ttk.Checkbutton(ventana, text="Derrame de Combustible",variable=CB49)
cb49.place(x=390,y=370)
CB411=BVVN.BooleanVar()
CB411.set(False)
cb411=ttk.Checkbutton(ventana, text="Otros",variable=CB411)
cb411.place(x=390,y=390)

##########################################################
#FIN CHECKBOX SECUNDARIO
##########################################################

ventana.mainloop()    #Creando la ventana en si
