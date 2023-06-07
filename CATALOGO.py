import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess

# Datos de ejemplo
datos = {
    "1": """ACTIVOS
        Son los recursos económicos de una empresa que 
        tienen un valor y se esperan obtener beneficios 
        futuros de ellos.""",
    "1.1": """ACTIVOS CIRCULANTES
        Son los activos que se espera que se conviertan en 
        efectivo o se consuman en el corto plazo, generalmente 
        dentro de un año. Ejemplos incluyen caja, bancos, 
        clientes, almacenes y papelería y útiles.""",
    "1.1.1": """CAJA
        En la contabilidad de una empresa, la cuenta contable 
        de caja es la que refleja el saldo de dinero en efectivo o 
        en cheques sin cobrar, existente en la empresa en un momento 
        determinado.""",
    "1.1.2": """BANCOS
        Son entidades que se dedican a trabajar con el dinero, 
        obteniendo una ganancia por las operaciones realizadas.""",
    "1.1.3": """CLIENTES
        El término clientes designa a aquellas personas físicas o 
        jurídicas que compran bienes y servicios que habitualmente 
        son objeto de venta o prestación por parte de la empresa.""",
    "1.1.4": """ALMACENES
         Es el lugar o espacio físico destinado para depositar, 
         guardar, preservar y custodiar un importante número de 
         artículos, piezas, herramientas, maquinarias, equipos, 
         productos o mercancías de una empresa.""",
    "1.1.5": """PAPELERÍA Y ÚTILES
         Los materiales útiles que se emplean en labores de la 
         empresa, siendo los principales el papel tamaño carta u 
         oficio, papel carbón, bloques de remisiones, talonarios de 
         facturas o recibos, libros, registros, tarjetas, lápices, 
         borradores, tintas, secantes, etc.""",
    "1.2": """ACTIVOS NO CIRCULANTES
         Son los activos que no se espera que se conviertan 
         en efectivo en el corto plazo. Incluyen activos fijos, 
         como mobiliario y equipo, y activos intangibles, como 
         marcas registradas.""",
    "1.3": """ACTIVOS FIJOS 
            Los activos fijos o activos no corrientes son los 
            activos que corresponden a bienes y derechos que 
            no son convertidos en efectivo por una empresa en 
            el año, y permanecen en ella durante más de un año.""",
    "1.4": """ACTIVOS INTANGIBLES
            Un activo intangible es un activo identificable, 
            de carácter no monetario y sin apariencia física. 
            Son activos monetarios tanto el dinero en efectivo 
            como otros activos, por los que se van a recibir 
            unas cantidades fijas o determinables de dinero.""",
    "2": """PASIVOS
            Representan las obligaciones financieras o deudas 
            que una empresa tiene con terceros.""",
    "2.1": """PASIVOS A CORTO PLAZO
            Son las deudas u obligaciones que deben pagarse en 
            el corto plazo, generalmente dentro de un año. 
            Ejemplos incluyen proveedores y acreedores diversos.""",
    "2.2": """PASIVOS A LARGO PLAZO
            Son las deudas u obligaciones que deben pagarse en 
            un plazo mayor a un año. Ejemplos incluyen acreedores 
            bancarios y acreedores hipotecarios.""",
    "3": """CAPITAL CONTABLE
            Es la diferencia entre los activos y los pasivos de 
            una empresa y representa el valor residual que pertenece 
            a los dueños o accionistas.""",
    "3.1": """CAPITAL CONTRIBUIDO
            Es el monto de dinero o recursos aportados por los 
            dueños o accionistas para financiar la empresa.""",
    "3.2": """CAPITAL GANADO
            Es la acumulación de los beneficios generados por 
            la empresa a lo largo del tiempo, que no han sido 
            distribuidos entre los accionistas.""",
    "4": """CUENTAS DE RESULTADOS ACREEDORAS
            Son las cuentas que representan ingresos o 
            ganancias para la empresa, como las ventas.""",
    "4": """CUENTAS DE RESULTADOS DEUDORAS
            """,
}

# Referencias globales a las imágenes
image_tk = None
image_tk_resultado = None

def buscar():
    # Obtener el ID ingresado en la caja de texto
    id_busqueda = entrada.get()

    # Buscar el ID en los datos
    if id_busqueda in datos:
        mostrar_resultado(datos[id_busqueda])
    else:
        messagebox.showinfo("ID no encontrado", "El ID no fue encontrado.")

def mostrar_resultado(resultado):
        
    ventana.destroy()
    
    ventana_resultado = tk.Tk()
    ventana_resultado.title("Cuenta")
    ancho_ventana = 620
    alto_ventana = 480
    x_ventana = ventana_resultado.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_resultado.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana_resultado.geometry(posicion)
    ventana_resultado.resizable(False, False)
    
    etiqueta_resultado = tk.Label(ventana_resultado, text=resultado, font="Times")
    etiqueta_resultado.pack()
    
    def salir():
        ventana_resultado.destroy()
        
    regresar = tk.Button(ventana_resultado, text="Regresar", font="Times", command=salir, pady=10, padx=10)
    regresar.pack(side=tk.BOTTOM)
    
    def mostrar_lista():
        subprocess.call(["python", "cuentas.py"])
    
    cuentas = tk.Button(ventana_resultado, text="Lista de cuentas", font="Times", command=mostrar_lista)
    cuentas.pack(side=tk.BOTTOM)
    
    image_label_resultado = tk.Label(ventana_resultado, image=image_tk_resultado)
    image_label_resultado.pack()
    
    # Cargar y almacenar la imagen de resultado en una variable global
    image_resultado = Image.open("img.jpg")
    image_resultado = image_resultado.resize((230, 200))
    image_tk_resultado = ImageTk.PhotoImage(image_resultado)

ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(False, False)
ventana.title("CATÁLOGO DE CUENTAS")

# Cargar y almacenar la imagen en una variable global
image = Image.open("cont.png")
image = image.resize((250, 270))
image_tk = ImageTk.PhotoImage(image)

# Mostrar la imagen en la ventana principal
image_label = tk.Label(ventana, image=image_tk)
image_label.pack()

# Crear la etiqueta y la caja de texto para ingresar el ID
etiqueta = tk.Label(ventana, text="Ingrese un ID:", font="Times")
etiqueta.pack()

def letra(char):
    return char in "12345."
validatecommand = ventana.register(letra)
def limitar_entrada(entrada, limit):
    def limitar(event):
        texto = entrada.get()
        if len(texto) >= limit and not event.keysym == 'BackSpace':
            return "break"
    entrada.bind("<Key>", limitar)

entrada = tk.Entry(ventana, font="Times", validate="key", validatecommand=(validatecommand, "%S"))
limitar_entrada(entrada, 7)
entrada.pack()

# Crear el botón de búsqueda
boton = tk.Button(ventana, text="Buscar", font="Times", command=buscar)
boton.pack()

# Ejecutar la ventana principal
ventana.mainloop()

