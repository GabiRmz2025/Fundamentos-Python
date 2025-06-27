#Ejercicio para crear en Tkinter Muestra de Widgets
from tkinter import * 
from tkinter import ttk

raiz =  Tk() #siempre nuestro objeto principal es Tk(), es raiz. Es la ventana principal
raiz.title("Muestra de Widgets")
raiz.geometry("550x350")

#Creamos el Marco Principal tipo Frame
marcoPrincipal = ttk.Frame()
marcoPrincipal.pack(fill="both", expand=True, padx=10, pady=10)

# Marco superior
marco_superior = ttk.Frame(marcoPrincipal, padding=5) 
marco_superior.pack(fill="both", expand=True)

#Frame Datos Personales
frame_dtPersonal = ttk.Frame(marco_superior, width=95, height=100, padding=2, borderwidth=3, relief="ridge")
frame_dtPersonal.pack(side="left", expand=False, fill="both", padx=5, pady=5)

Nombre = StringVar() 
A_Paterno = StringVar() 
A_Materno = StringVar()
Correo = StringVar()
Movil = StringVar()

ttk.Label(frame_dtPersonal, text="Nombre:").grid(column=0, row=0, sticky=W)
ttk.Label(frame_dtPersonal, textvariable=Nombre).grid(column=1, row=0, ipady=7, sticky=(W, E))
txtNombre = ttk.Entry(frame_dtPersonal, width=40, textvariable=Nombre).grid(column=1, row=0, sticky=(W, E))

ttk.Label(frame_dtPersonal, text="A. Paterno:").grid(column=0, row=1, sticky=W)
ttk.Label(frame_dtPersonal, textvariable=A_Paterno).grid(column=1, row=1,  ipady=7, sticky=(W,E))
txtA_Paterno = ttk.Entry(frame_dtPersonal, width=40, textvariable=A_Paterno).grid(column=1, row=1, sticky=(W, E))

ttk.Label(frame_dtPersonal, text="A. Materno:").grid(column=0, row=2, sticky=W)
ttk.Label(frame_dtPersonal, textvariable=A_Materno).grid(column=1, row=2, ipady=7, sticky=(W,E))
txtA_Materno = ttk.Entry(frame_dtPersonal, width=40, textvariable=A_Materno).grid(column=1, row=2, sticky=(W, E))

ttk.Label(frame_dtPersonal, text="Correo:").grid(column=0, row=3, sticky=W)
ttk.Label(frame_dtPersonal, textvariable=Correo).grid(column=1, row=3, ipady=7, sticky=(W,E))
txtCorreo = ttk.Entry(frame_dtPersonal, width=40, textvariable=Correo).grid(column=1, row=3, sticky=(W, E))

ttk.Label(frame_dtPersonal, text="Móvil:").grid(column=0, row=4, sticky=W)
ttk.Label(frame_dtPersonal, textvariable=Movil).grid(column=1, row=4, ipady=7, sticky=(W,E))
txtMovil = ttk.Entry(frame_dtPersonal, width=40, textvariable=Movil).grid(column=1, row=4, sticky=(W, E))

#Frame Tipo Personas
frame_Personas = ttk.Frame(marco_superior)
frame_Personas.pack(side="left", expand=True, fill="both", padx=5, pady=5)

Persona =StringVar()

estudiante = ttk.Radiobutton(frame_Personas, text='Estudiante', variable=Persona, value='estudiante').place(relx=0.2, rely=0.4, anchor="w")
empleado = ttk.Radiobutton(frame_Personas, text='Empleado', variable=Persona, value='empleado').place(relx=0.2, rely=0.5, anchor="w")
desempleado = ttk.Radiobutton(frame_Personas, text='Desempleado', variable=Persona, value='Desempleado').place(relx=0.2, rely=0.6, anchor="w")

# Marco medio
marco_medio = ttk.Frame(marcoPrincipal, padding=3)
marco_medio.pack(fill="both", expand=True)

#Frame Aficiones 
frame_Aficion = ttk.Frame(marco_medio, width=140, height=20, padding=2, borderwidth=3, relief="ridge")
frame_Aficion.pack(side="left", expand=True, fill="both", padx=5, pady=5)
TituloA = ttk.Label(marco_medio, text='Aficiones').place(relx=0.1, rely=0.1, anchor="w")

Aficion1 = StringVar()
Aficion2 = StringVar()
Aficion3 = StringVar()

Leer = ttk.Checkbutton(frame_Aficion, text='Leer', variable=Aficion1, onvalue='si', offvalue='no').place(relx=0.1, rely=0.5, anchor="w")
Musica = ttk.Checkbutton(frame_Aficion, text='Música', variable=Aficion2, onvalue='si', offvalue='no').place(relx=0.4, rely=0.5, anchor="w")
Videojuegos = ttk.Checkbutton(frame_Aficion, text='Videojuegos', variable=Aficion3, onvalue='si', offvalue='no').place(relx=0.7, rely=0.5, anchor="w")

#Frame Estados
frame_Estado = ttk.Frame(marco_medio, padding=5)
frame_Estado.pack(side="right", expand=True, fill="both", padx=5, pady=5)

Estados = StringVar()

Estados = ttk.Combobox(frame_Estado, textvariable=Estados, value=["Querétaro", "Guanajuato", "Yucatán", "Tamaulipas", "Jalisco"])
Estados.place(relx=0.0, rely=0.5, anchor="w")
Estados.set("Estados (32)")

# Marco Inferior
marco_inferior = ttk.Frame(marcoPrincipal, padding=2)
marco_inferior.pack(fill="x", padx=5, pady=10)

#Frame Guardar y Cancelar
frame_GC = ttk.Frame(marco_inferior, padding=3)
frame_GC.pack(side="left", expand=True, fill="both", padx=5, pady=5)

ttk.Button(frame_GC, text="Guardar").place(relx=0.0, rely=0.5, anchor="w")
ttk.Button(frame_GC, text="Cancelar").place(relx=0.2, rely=0.5, anchor="w")

for child in marcoPrincipal.winfo_children():
    child.pack(fill="both", expand=True)

raiz.mainloop()