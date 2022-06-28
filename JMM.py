import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import webbrowser
from time import sleep
class ventana():
	def __init__(self):
		def Guardar(event=None):
			print("Ja")
		def Nuevo(event=None):
			self.txt.config(state=NORMAL)
			self.txt.delete(1.0,"end")
			self.txt.insert(1.0,'''Bienvenido Julian
Deseas Anotar algo?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
			self.txt.config(state=DISABLED)
		def salir(event):
			self.destroy()
		def Charla(event):
			if(self.Chat.get()!=""):
				if (self.Chat.get()=="Salir"):
					self.destroy()
				elif (self.Chat.get()=="Iniciar Servidor"):
					print(os.system("python3 -m http.server 1998 -d Server &"))
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nServidor Iniciado\nIngresa a 10.20.83.113:1998\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Bomberos"):
					os.system("open /home/toti/Escritorio/Mio/JMM/Server/6Sabado/GestionBomberos &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nCarpeta del Proyecto Bomberos Abierta\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Abrir CV"):
					os.system("open /home/toti/Escritorio/Mio/JMM/Server/1Lunes/CV/Mandaio_Julian.html &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nCV abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Arduino"):
					os.system("cd /home/toti/Programas/arduino-1.8.19 && ./arduino &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nArduino Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Gitkraken"):
					os.system("cd /home/toti/Programas/gitkraken/ && ./gitkraken &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nGitkraken Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Ver Listas"):
					os.system("open /home/toti/Escritorio/Mio/JMM/Server/2Martes/Listas/ &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nListas Abiertas\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Lectura"):
					os.system("open /home/toti/Escritorio/Mio/JMM/Server/4Jueves/Lectura/Paginas.html &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nLecturas Abiertas\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Abrir Bomberos"):
					os.system("cd /home/toti/Escritorio/Mio/JMM/Server/6Sabado/GestionBomberos/ && python self.py &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nPrograma de Bomberos abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Sincronizar"):
					os.system("cd /home/toti/Escritorio/Mio/JMM/ && ./Subir.sh &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nSincronizado Completo\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Apagar PC"):
					os.system("shutdown now")
				elif (self.Chat.get()=="Reiniciar PC"):
					os.system("shutdown -r 0")
				elif (self.Chat.get()=="Detener Servidor"):
					self.txt.config(state=NORMAL)
					self.txt.insert("end","\nEl Servidor se Detendra Reiniciando la PC")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Programar"):
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Ya Podes Programar")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
					Programar=Toplevel()
					Programar.geometry("500x500")
					Programar.resizable(0,0)
					txt=Text(Programar)
					txt.place(x=10,y=10,width=480,height=480)
					barra_menus=tk.Menu()
					menu_Menu=tk.Menu(barra_menus, tearoff=False)
					menu_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=Nuevo)
					Programar.bind_all("<Control-n>", Nuevo)
					menu_Menu.add_command(label="Guardar", accelerator="Ctrl+L", command=Nuevo)
					Programar.bind_all("<Control-l>", Nuevo)
					menu_Menu.add_separator()
					menu_Menu.add_command(label="Salir", accelerator="Ctrl+Z", command=self.destroy)
					Programar.bind_all("<Control-z>", salir)
					barra_menus.add_cascade(menu=menu_Menu, label="Archivos")
					Programar.config(menu=barra_menus)
				elif (self.Chat.get()=="Google"):
					webbrowser.open("www.google.com.ar", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Google Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Facebook"):
					webbrowser.open("www.facebook.com.ar", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Facebook Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Mapa"):
					webbrowser.open("/home/toti/Escritorio/Mio/JMM/Mapa.html", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Mapa Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Abrir Servidor"):
					webbrowser.open("http://0.0.0.0:1998", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Servidor Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Terminal"):
					os.system("exo-open --launch TerminalEmulator &")
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Terminal Abierta\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Try Hack Me"):
					webbrowser.open("https://tryhackme.com/login", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Try Hack Me Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Free Code Camp"):
					webbrowser.open("https://auth.freecodecamp.org/login?state=hKFo2SBEcG9hZ19lWW9QV1VkOFVSd3FzRHhCQi16bTJNTVAwWqFupWxvZ2luo3RpZNkgU3Q0aGRfN2xmZVJhN01iTHNmR3A3amhZWkFNUWE1WFajY2lk2SBhVUR2OWpWcVRmeEJSRTFsNjBOQTVBZjd5VENHRTRjeQ&amp;client=aUDv9jVqTfxBRE1l60NA5Af7yTCGE4cy&amp;protocol=oauth2&amp;response_type=code&amp;redirect_uri=https%3A%2F%2Fapi.freecodecamp.org%2Fauth%2Fauth0%2Fcallback&amp;scope=openid%20profile%20email", new=0, autoraise=True)
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Free Code Camp Abierto\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				elif (self.Chat.get()=="Ayuda"):
					self.txt.config(state=NORMAL)
					self.txt.insert("end","Los Comandos Disponibles Son:\nIniciar Servidor\nAbrir Servidor\nGoogle\nFacebook\nDetener Servidor\nProgramar\nTry Hack Me\nFree Code Camp\nApagar PC\nTerminal\nMapa\nBomberos\nAbrir CV\nVer Listas\nLectura\nArduino\nGitkraken\nReiniciar PC\nAbrir Bomberos\nSalir\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
				else:
					self.Chat.config(fg="black")
					self.txt.config(state=NORMAL)
					msj=self.Chat.get()
					msj=msj
					self.txt.insert("end",msj+"\n")
					self.Chat.delete(0,999)
					self.txt.config(state=DISABLED)
			else:
				self.Chat.insert(0,"")
		def Color(event):
			if (self.Chat.get()=="Salir") or (self.Chat.get()=="Iniciar Servidor") or (self.Chat.get()=="Detener Servidor") or (self.Chat.get()=="Google") or (self.Chat.get()=="Programar") or (self.Chat.get()=="Apagar PC") or (self.Chat.get()=="Facebook") or (self.Chat.get()=="Abrir Servidor") or (self.Chat.get()=="Terminal") or (self.Chat.get()=="Try Hack Me") or (self.Chat.get()=="Free Code Camp") or (self.Chat.get()=="Ayuda") or (self.Chat.get()=="Mapa") or (self.Chat.get()=="Bomberos") or (self.Chat.get()=="Abrir CV") or (self.Chat.get()=="Ver Listas") or (self.Chat.get()=="Lectura") or (self.Chat.get()=="Arduino") or (self.Chat.get()=="Gitkraken") or (self.Chat.get()=="Reiniciar PC") or (self.Chat.get()=="Abrir Bomberos") or (self.Chat.get()=="Sincronizar"):
				self.Chat.config(fg="blue")
			else:
				self.Chat.config(fg="black")

		self=tk.Tk()
		altura=self.winfo_reqheight()
		anchura=self.winfo_reqwidth()
		altura_pantalla=self.winfo_screenheight()
		anchura_pantalla=self.winfo_screenwidth()
		self.geometry(f"{anchura_pantalla}x{altura_pantalla}")
		self.title("JMM")
		self.resizable(0,0)
		self.barra_menus=tk.Menu()
		self.menu_Menu=tk.Menu(self.barra_menus, tearoff=False)
		self.menu_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=Nuevo)
		self.bind_all("<Control-n>", Nuevo)
		self.menu_Menu.add_command(label="Guardar", accelerator="Ctrl+G", command=Nuevo)
		self.bind_all("<Control-g>", Guardar)
		self.menu_Menu.add_separator()
		self.menu_Menu.add_command(label="Salir", accelerator="Ctrl+Z", command=self.destroy)
		self.bind_all("<Control-z>", salir)
		self.barra_menus.add_cascade(menu=self.menu_Menu, label="Archivos")
		self.menu_Menu=tk.Menu(self.barra_menus, tearoff=True)
		self.config(menu=self.barra_menus)
		self.txt=tk.Text()
		self.txt.insert(1.0,'''Bienvenido Julian
Deseas Anotar algo?
----------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
		self.txt.config(state=DISABLED)
		self.txt.place(x=10,y=10,width=anchura_pantalla-30,height=altura_pantalla-110)
		
		self.Chat=tk.Entry()
		self.Chat.insert(0,"")
		self.Chat.focus_set()
		self.Chat.place(x=10,y=altura_pantalla-95,width=anchura_pantalla-30)
		
		self.bind_all("<Return>", Charla)
		self.bind_all("<Key>", Color)
		self.mainloop()
def salir(event=None):
	if(Usuario.get()=="Julian.Mandaio") and (Clave.get()=="41323167"):
		Ingreso.destroy()
		ventana()
	else:
		Ingreso.destroy()
Ingreso=tk.Tk()
Ingreso.geometry("400x75")
Ingreso.title("Ingreso al Sistema")
Ingreso.resizable(0,0)
Ingreso.bind_all("<Control-z>", salir)
labelUsuario=tk.Label(text="Usuario: ")
labelUsuario.place(x=10,y=10)
Usuario=tk.Entry()
Usuario.insert(0,"Julian.Mandaio")
Usuario.config(state=DISABLED)
Usuario.place(x=95,y=10)
labelClave=tk.Label(text="Contraseña: ")
labelClave.place(x=10,y=40)
Clave=tk.Entry(show="*")
Clave.focus_set()
Clave.place(x=95,y=40)
Ingreso.mainloop()
