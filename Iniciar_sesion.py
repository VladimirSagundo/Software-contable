import tkinter as tk
import subprocess

ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Inicio de sesión")

def __init__(self, master):
   self.master = master

# Crear campos de entrada para el nombre de usuario y la contraseña
primero=tk.Label(ventana, text="- Usuario -", font='Times 20').pack(pady=10)

def letra(char):
    return char in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMáéíóúÁÉÍÓÚ"
validatecommand = ventana.register(letra)
def limitar_entry(entrada, limit):
    def limitar(event):
        texto = entrada.get()
        if len(texto)>=limit and not event.keysym=='BackSpace':
            return "break"
    entrada.bind("<Key>", limitar)
   

nombre_usuario = tk.Entry(ventana, validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(nombre_usuario,30)
nombre_usuario.insert(0, "si")
nombre_usuario.pack(pady=20)
tk.Label(ventana, text="- Contraseña -", font='Times 20').pack(pady=10)
contrasena_usuario = tk.Entry(ventana, show="*", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entry(contrasena_usuario,30)
contrasena_usuario.insert(0, "no")
contrasena_usuario.pack(pady=15)

def abrir_ventana_registros():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "si" and contrasena == "no":
        ventana.destroy()
        subprocess.call(["python", "CATALOGO.py"])
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos", font='Times 20')
#def menú():
    #ventana.destroy()
    #subprocess.call(["python", "Proyecto_menú.py"]) 

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=abrir_ventana_registros, borderwidth=5)
iniciar_sesion.pack(padx=100, pady=10)

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
ventana.resizable(width=0, height=0)
resultado.pack(pady=10)
ventana.mainloop()