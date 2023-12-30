#region Programa
#region Importaciones
import tkinter
import socket
import webbrowser
import subprocess
from tkinter import filedialog
from win10toast import ToastNotifier
try:
    import speech_recognition as sr
    import pyttsx3
except ModuleNotFoundError:
     print("Modulo No Encontrado")
#endregion
#region Acciones
def guardar():
    texto = entrada_texto.get("1.0", "end-1c")  # Obtener el texto del widget de entrada
    if texto:
        try:
            archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
            if archivo:
                archivo.write(texto)  # Escribir el texto en el archivo
                archivo.close()
                print("Archivo guardado correctamente.")
        except Exception as e:
            print("Error al guardar el archivo:", str(e))
    else:
        print("No hay texto para guardar.")
def abrirMinecraft():
    subprocess.Popen("C:/Users/Usuario/Downloads/Instalador/LauncherFenix-Minecraft-v7.exe")
def abrirYoutube():
       webbrowser.open("www.youtube.com")
def abrirGoogle():
     webbrowser.open("https://www.google.com/")
def ip():
    ip=socket.gethostbyname(socket.gethostname())
    return(ip)
def ip_local():
    IP_L=ip()
    toaster = ToastNotifier()
    toaster.show_toast("Ip Local", "IP: " + IP_L, duration=100, threaded=True)
def victor():
    with sr.Microphone() as source:
        toaster = ToastNotifier()
        toaster.show_toast("Victor", "En Escucha.", duration=1)
        audio = recognizer.listen(source)
        query = recognizer.recognize_google(audio, language="es-ES").lower()
        print("Usuario:", query)
        try:
            if "salir" in query:
                root.quit()
            elif "youtube" in query:
                abrirYoutube()
            elif "google" in query:
                abrirGoogle()
            elif "minecraft" in query:
                abrirMinecraft()
            elif "hbo" in query:
                webbrowser.open("")
            elif "star plus" in query:
                print("star")
                webbrowser.open("")
            else:
                 pass
        except sr.UnknownValueError:
            toaster = ToastNotifier()
            toaster.show_toast("Victor", "Victor no escucho.", duration=10)
        except sr.RequestError as e:
            print("Error al solicitar los resultados; {0}".format(e))
#endregion
#region Inicializador
#region InterfazDeVoz
try:
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
except NameError:
     print("No se puede inicializar")
#endregion
#endregion
#region RootSecundarios
#endregion
#region RootPrincipal
root = tkinter.Tk()
root.title("Julian 73")
root.geometry("350x180")
root.resizable(width=False, height=False)
#endregion
#region ObjetoMenu
menu = tkinter.Menu(root)
root.config(menu=menu)
#endregion
#region Menus
####################################################################
# Menu Archivo
####################################################################
menu_archivo = tkinter.Menu(menu, tearoff=False)
menu.add_cascade(label="Archivo", menu=menu_archivo)
####################################################################
# Menu Programacion
####################################################################
menu_programacion = tkinter.Menu(menu, tearoff=False)
menu.add_cascade(label="Programacion", menu=menu_programacion)
####################################################################
# Menu Ocio
####################################################################
menu_ocio = tkinter.Menu(menu, tearoff=False)
menu.add_cascade(label="Ocio", menu=menu_ocio)
####################################################################
# Menu Tareas
####################################################################
menu_tareas = tkinter.Menu(menu, tearoff=False)
menu.add_cascade(label="Tareas", menu=menu_tareas)
####################################################################
# Menu Victor
####################################################################
menu_victor = tkinter.Menu(menu, tearoff=False)
menu.add_command(label="Victor", command=victor)
####################################################################
# Menu Salir
####################################################################
menu_salir = tkinter.Menu(menu, tearoff=False)
menu.add_command(label="Salir", command=root.destroy)
#endregion
#region MenuArchivo
####################################################################
# Menu Archivo
####################################################################
menu_archivo.add_command(label="Abrir", command=root.destroy)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.destroy)
#endregion
#region MenuProgramacion
####################################################################
# Menu Programacion
####################################################################
submenu_hacking = tkinter.Menu(menu, tearoff=False)
menu_programacion.add_cascade(label="Hacking", menu=submenu_hacking)
submenu_hacking.add_command(label="Ip Local", command=ip_local)
submenu_hacking.add_command(label="Iniciar Servidor", command=ip_local)
submenu_programacion = tkinter.Menu(menu, tearoff=False)
menu_programacion.add_cascade(label="Programacion", menu=submenu_programacion)
submenu_programacion.add_command(label="Abrir Visual Studio Code", command=root.destroy)
menu_programacion.add_separator()
menu_programacion.add_command(label="Salir", command=root.destroy)
#endregion
#region MenuOcio
####################################################################
# Menu Ocio
####################################################################
menu_ocio.add_command(label="Videos", command=root.destroy)
menu_ocio.add_command(label="Juegos", command=root.destroy)
menu_ocio.add_separator()
menu_ocio.add_command(label="Salir", command=root.destroy)
#endregion
#region MenuTareas
####################################################################
# Menu Tareas
####################################################################
menu_tareas.add_command(label="tarea1", command=root.destroy)
menu_tareas.add_command(label="tarea2", command=root.destroy)
menu_tareas.add_separator()
menu_tareas.add_command(label="Salir", command=root.destroy)
#endregion
#region pantalla
entrada_texto = tkinter.Text(root, height=9, width=35)
entrada_texto.pack()
#entrada = tkinter.Entry(root)
#entrada.pack()
root.mainloop()
#endregion
#endregion


'''
github
clave:Teclado12369.
'''