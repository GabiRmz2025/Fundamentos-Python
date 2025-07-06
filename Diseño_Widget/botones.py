#Ejercicio para crear botones con imagen y texto
from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Button(raiz, text="BOTÓN SÓLO TEXTO")
etqTexto.grid()

imagen = PhotoImage(file="Gabi_rc.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Boton Combinado")
btnCombinada.grid()
btnCombinada["image"] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opción 1")
chkBoton.grid()

raiz.mainloop()