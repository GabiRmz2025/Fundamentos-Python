#Ejercicio para crear diseño en Tkinter
from tkinter import * # sirven para importar paquete Tkinter
from tkinter import ttk

def calcular(*args):
    try:  #para el manejo de excepciones
        valor = float(pies.get())
        metros.set((0.3048 * valor * 10000.0 + 0.5) / 10000.0)
    except ValvueError: #si es un valor invalido, no debe hacer nada
        pass
#Con al línea 12 y 13 se crea la ventana, pero aún no le decimos que se vea
raiz =  Tk() #siempre nuestro objeto principal es Tk(), es raiz. Es la ventana
raiz.title("Pies a metros")
#creamos un widget tipo frame, un marco de trabajo
marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

pies = StringVar()
metros = StringVar()
#la caja de texto donde va escribir
txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies)
txtPies.grid(column=2, row=1, sticky=(W, E))

ttk.Label(marcoPrincipal, textvariable=metros).grid(column=2, row=2, sticky=(W,E))
ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W)

ttk.Label(marcoPrincipal, text="pies").grid(column=3, row=1, sticky=W)
ttk.Label(marcoPrincipal, text="es equivalente a:").grid(column=1, row=2, sticky=E)
ttk.Label(marcoPrincipal, text="metros").grid(column=3, row=2, sticky=W)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5) #margenes del marco principal
    
txtPies.focus() #colcoar el cursor
raiz.bind('<Return>', calcular) #'<Return>' es igual a enter

raiz.mainloop()