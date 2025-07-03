#Ejercicio para crear en Tkinter Muestra de Widgets
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import csv
import os #Este se usa para saber si ya existe un archivo

#Función para limpiar el formulario (widget), cuando se presione el botón Limpiar o después de Guardar
def limpiar(*args):
    txtNombre.delete(0, tk.END)
    txtA_Paterno.delete(0, tk.END)
    txtA_Materno.delete(0, tk.END)
    txtCorreo.delete(0, tk.END)
    txtMovil.delete(0, tk.END)
    Persona.set(None)
    Aficion1.set(None)
    Aficion2.set(None)
    Aficion3.set(None)
    Estados.set("")
    #messagebox.showinfo("Borrado","Registros limpios de forma correcta.")

#Función para Guardar los datos, crear o abrir el archivo CSV cuando se presione el botón Guardar
def guardar_datos(*args):
    datos = [txtNombre.get(), txtA_Paterno.get(), txtA_Materno.get(), txtCorreo.get(), txtMovil.get(),
             Persona.get(), Aficion1.get(), Aficion2.get(), Aficion3.get(), Estados.get()]
    archivo_existe = os.path.isfile("Datos_Archivo.csv") #metodo investigado en Libro de Python y youtube

    try:
        with open("Datos_Archivo.csv", mode="a", newline="", encoding="utf-8") as archivo_guardado:
            rotulo = csv.writer(archivo_guardado)
            if not archivo_existe:
                rotulo.writerow(["Nombre", "Apellido_Paterno", "Apellido_Materno",
                                   "Correo", "Telefono_Móvil", "Tipo_Persona",
                                   "Afición_1", "Afición_2", "Aficion_3", "Estado"])
            rotulo.writerow(datos)
        messagebox.showinfo("Guardado","Información almacenada en 'Datos_Archivo.csv' correctamente.")
        limpiar()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron guardar los datos:\n {e}")

#Función para mostrar el contenido de "Datos_Archivo.csv" en la terminal
def consultar():
    consulta_archivo = "Datos_Archivo.csv"

    if not os.path.isfile(consulta_archivo):
        print("Datos_Archivo.csv, NO EXISTE")
        return

    try:
        with open(consulta_archivo, mode="r", encoding="utf-8") as archivo:
            lectura = csv.reader(archivo)
            for fila in lectura:
                print(" | ".join(fila)) #metódo para concatenar strings y poner un separador |
    except Exception as error_leer:
        print(f"Ocurrió un error al leer 'Datos_Archivo.csv':", {error_leer})

#Función para cerrar la ventana principal y sus widgets
def cerrar():
    raiz.destroy()
    
#Inicio con los Marcos
raiz =  Tk() #siempre nuestro objeto principal es Tk(), es raiz. Es la ventana principal
raiz.title("Muestra de Widgets")
raiz.geometry("550x380")

#Creamos el Marco Principal tipo Frame
marcoPrincipal = ttk.Frame()
marcoPrincipal.pack(fill="both", expand=True, padx=10, pady=10)

# MARCO SUPERIOR
marco_superior = ttk.Frame(marcoPrincipal, padding=5) 
marco_superior.pack(fill="both", expand=True)

#Frame Datos Personales
frame_dtPersonal = ttk.Frame(marco_superior, width=70, height=60, padding=2, borderwidth=3, relief="ridge")
frame_dtPersonal.pack(side="left", expand=False, fill="both", padx=5, pady=5)

Nombre = StringVar() 
A_Paterno = StringVar() 
A_Materno = StringVar()
Correo = StringVar()
Movil = StringVar()

tk.Label(frame_dtPersonal, text="Nombre:").grid(column=0, row=0, sticky=W)
tk.Label(frame_dtPersonal, textvariable=Nombre).grid(column=1, row=0, ipady=7, sticky=(W, E))
txtNombre = tk.Entry(frame_dtPersonal, width=40, textvariable=Nombre)
txtNombre.grid(column=1, row=0, sticky=(W, E))

tk.Label(frame_dtPersonal, text="Apellido Paterno:").grid(column=0, row=1, sticky=W)
tk.Label(frame_dtPersonal, textvariable=A_Paterno).grid(column=1, row=1,  ipady=7, sticky=(W,E))
txtA_Paterno = tk.Entry(frame_dtPersonal, width=40, textvariable=A_Paterno)
txtA_Paterno.grid(column=1, row=1, sticky=(W, E))

tk.Label(frame_dtPersonal, text="Apellido Materno:").grid(column=0, row=2, sticky=W)
tk.Label(frame_dtPersonal, textvariable=A_Materno).grid(column=1, row=2, ipady=7, sticky=(W,E))
txtA_Materno = tk.Entry(frame_dtPersonal, width=40, textvariable=A_Materno)
txtA_Materno.grid(column=1, row=2, sticky=(W, E))

tk.Label(frame_dtPersonal, text="Correo:").grid(column=0, row=3, sticky=W)
tk.Label(frame_dtPersonal, textvariable=Correo).grid(column=1, row=3, ipady=7, sticky=(W,E))
txtCorreo = tk.Entry(frame_dtPersonal, width=40, textvariable=Correo)
txtCorreo.grid(column=1, row=3, sticky=(W, E))

tk.Label(frame_dtPersonal, text="Móvil:").grid(column=0, row=4, sticky=W)
tk.Label(frame_dtPersonal, textvariable=Movil).grid(column=1, row=4, ipady=7, sticky=(W,E))
txtMovil = tk.Entry(frame_dtPersonal, width=40, textvariable=Movil)
txtMovil.grid(column=1, row=4, sticky=(W, E))

#Frame Rol de Personas
frame_Rol = ttk.Frame(marco_superior, width=30, height=90)
frame_Rol.pack(side="left", expand=True, fill="both", padx=5, pady=5)

Persona =StringVar()

Estudiante = ttk.Radiobutton(frame_Rol, text='Estudiante', variable=Persona, value='Estudiante').place(relx=0.2, rely=0.4, anchor="w")
Empleado = ttk.Radiobutton(frame_Rol, text='Empleado', variable=Persona, value='Empleado').place(relx=0.2, rely=0.5, anchor="w")
Desempleado = ttk.Radiobutton(frame_Rol, text='Desempleado', variable=Persona, value='Desempleado').place(relx=0.2, rely=0.6, anchor="w")

#MARCO MEDIO
marco_medio = ttk.Frame(marcoPrincipal, padding=3)
marco_medio.pack(fill="both", expand=True)

#Frame Aficiones 
frame_Aficion = ttk.Frame(marco_medio, width=140, height=20, padding=2, borderwidth=3, relief="ridge")
frame_Aficion.pack(side="left", expand=True, fill="both", padx=5, pady=5)
TituloA = ttk.Label(marco_medio, text='Aficiones').place(relx=0.1, rely=0.1, anchor="w")

Aficion1 = StringVar()
Aficion2 = StringVar()
Aficion3 = StringVar()

Leer = ttk.Checkbutton(frame_Aficion, text='Leer', variable=Aficion1, onvalue='Leer', offvalue='').place(relx=0.1, rely=0.5, anchor="w")
Musica = ttk.Checkbutton(frame_Aficion, text='Música', variable=Aficion2, onvalue='Música', offvalue='').place(relx=0.4, rely=0.5, anchor="w")
Videojuegos = ttk.Checkbutton(frame_Aficion, text='Videojuegos', variable=Aficion3, onvalue='Video_Juegos', offvalue='').place(relx=0.7, rely=0.5, anchor="w")

#Frame Estados
frame_Estado = ttk.Frame(marco_medio, padding=5)
frame_Estado.pack(side="right", expand=True, fill="both", padx=5, pady=5)

Estados = StringVar()
ListaEdo = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Ciudad de México", "Coahuila", "Colima",
            "Chiapas", "Chihuahua", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo",
            "Jalisco", "Michoacan", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", 
            "Querétaro", "Quintana Roo", "San Luis Potosi", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
            "Veracruz", "Yucatán", "Zacatecas"]

Estados = ttk.Combobox(frame_Estado, textvariable=Estados, value=ListaEdo) 
Estados.place(relx=0.0, rely=0.5, anchor="w")
Estados.set("Selecciona")

#MARCO INFERIOR
marco_inferior = ttk.Frame(marcoPrincipal, padding=2)
marco_inferior.pack(fill="both", padx=5, pady=10)

#Frame Guardar y Cancelar
frame_GC = ttk.Frame(marco_inferior, padding=3)
frame_GC.pack(side="left" , expand=True, fill="both", padx=5, pady=5)

ttk.Button(frame_GC, command=guardar_datos, text="Guardar").place(relx=0.0, rely=0.5, anchor="w")
ttk.Button(frame_GC, command=limpiar, text="Limpiar").place(relx=0.2, rely=0.5, anchor="w")
ttk.Button(frame_GC, command=consultar, text="Mostrar Terminal").place(relx=0.4, rely=0.5, anchor="w")
ttk.Button(frame_GC, command=cerrar, text="Cerrar").place(relx=0.7, rely=0.5, anchor="c")

for child in marcoPrincipal.winfo_children():
    child.pack(fill="both", expand=True)
txtNombre.focus()

raiz.mainloop()