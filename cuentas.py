import tkinter as tk

datos = {
    "Activos": "Son los recursos económicos de una empresa que tienen un valor y se esperan obtener beneficios futuros de ellos.",
    "Activos circulantes": "Son los activos que se espera que se conviertan en efectivo o se consuman en el corto plazo, generalmente dentro de un año. Ejemplos incluyen caja, bancos, clientes, almacenes y papelería y útiles.",
    "Activos no circulantes": "Son los activos que no se espera que se conviertan en efectivo en el corto plazo. Incluyen activos fijos, como mobiliario y equipo, y activos intangibles, como marcas registradas.",
    "Pasivos": "Representan las obligaciones financieras o deudas que una empresa tiene con terceros.",
    "Pasivos a corto plazo": "Son las deudas u obligaciones que deben pagarse en el corto plazo, generalmente dentro de un año. Ejemplos incluyen proveedores y acreedores diversos.",
    "Pasivos a largo plazo": "Son las deudas u obligaciones que deben pagarse en un plazo mayor a un año. Ejemplos incluyen acreedores bancarios y acreedores hipotecarios.",
    "Capital contable": "Es la diferencia entre los activos y los pasivos de una empresa y representa el valor residual que pertenece a los dueños o accionistas.",
    "Capital contribuido": "Es el monto de dinero o recursos aportados por los dueños o accionistas para financiar la empresa.",
    "Capital social": "Es la parte del capital contable que representa el valor nominal de las acciones emitidas por la empresa a sus accionistas.",
    "Capital ganado": "Es la acumulación de los beneficios generados por la empresa a lo largo del tiempo, que no han sido distribuidos entre los accionistas.",
    "Utilidad del ejercicio": "Es el beneficio neto obtenido por la empresa durante un período contable determinado.",
    "Cuentas de resultados acreedoras": "Son las cuentas que representan ingresos o ganancias para la empresa, como las ventas.",
    "Cuentas de resultados deudoras": "Son las cuentas que representan costos o gastos para la empresa, como el costo de ventas, gastos de ventas y gastos de administración."
}

def lista(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        key = listbox.get(index)
        definition = datos[key]
        text.delete("1.0", tk.END)
        text.insert(tk.END, definition)

ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(False, False)
ventana.title("LISTA DE CUENTAS")

listbox = tk.Listbox(ventana, width=60)
for key in datos:
    listbox.insert(tk.END, key)
listbox.pack(pady=10)

text = tk.Text(ventana, width=60, height=10)
text.pack()

listbox.bind("<<ListboxSelect>>", lista)

ventana.mainloop()
