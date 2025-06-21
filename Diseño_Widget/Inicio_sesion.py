#Ejercicio para crear diseño en Tkinter de INICIO DE SESIÓN

from tkinter import * 
from tkinter import ttk

#Con al línea 12 y 13 se crea la ventana, pero aún no le decimos que se vea
raiz =  Tk() #siempre nuestro objeto principal es Tk(), es raiz. Es la ventana
raiz.title("Inicio de Sesión")
#creamos un widget tipo frame, un marco de trabajo
marcoPrincipal = ttk.Frame(raiz, padding="5 5 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

Usuario = StringVar() 
Contrasena = StringVar() 

#la cajas de texto
txtUsuario = ttk.Entry(marcoPrincipal, width=30, textvariable=Usuario)
txtUsuario.grid(column=2, row=3, sticky=(W, E))
txtContrasena = ttk.Entry(marcoPrincipal, width=30, textvariable=Contrasena)
txtContrasena.grid(column=2, row=4, sticky=(W, E))

ttk.Label(marcoPrincipal, textvariable=Usuario).grid(column=1, row=3, sticky=(W,E))
ttk.Label(marcoPrincipal, textvariable=Contrasena).grid(column=1, row=4, sticky=(W,E))
ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2, row=5, sticky=E)

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=1, row=3, sticky=E)
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=1, row=4, sticky=E)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5) #margenes del marco principal
    
txtUsuario.focus() #colocar el cursor

raiz.mainloop()