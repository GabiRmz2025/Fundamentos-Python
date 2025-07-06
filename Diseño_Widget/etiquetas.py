#Ejercicio para crear etiquetas con imagen
from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="ETIQUETA SÓLO TEXTO")
etqTexto.grid()

imagen = PhotoImage(file="Gabi_rc.png")

etqImagen = ttk.Label(raiz)
etqTexto.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text='EtqCombinada', compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()