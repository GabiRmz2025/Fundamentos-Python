#Ejercicio final para crear una calculadora básica
import tkinter as tk

#Función para mostrar los números y operadores en Pantalla
#Se va ir concatenando los caracteres marcados en las teclas
def mostrar(caracter):
    marcar_caracter.set(marcar_caracter.get() + str(caracter))

#Función para realizar el metódo de calculo
#Se va autilizar la función eval(), evalua que expresa o pide la cadena
def calcular():
    try:
        expresion = marcar_caracter.get()
        resultado = eval(expresion) 
        marcar_caracter.set(str(resultado))
    except Exception as e:
        marcar_caracter.set(f"Error: {e}") #muestra en la pantalla el error 

def limpiar(*args):
    pantalla.delete(0, tk.END)

#Función que decide qué hacer según la tecla presionada
def ejecutar_accion(z):
    if z == '=':
        calcular()
    elif z == 'C':
        limpiar()
    else:
        mostrar(z)

#Función para ejecutar la función calcular() con la tecla enter
def tecla_enter(event):
    calcular()

#Marco Principal
marcoPrincipal = tk.Tk()
marcoPrincipal.title("Calculadora Básica")
marcoPrincipal.geometry("300x400")
marcoPrincipal.resizable(False, False)

#Variable para contener número u operador marcado
marcar_caracter = tk.StringVar()

#Ventana de texto de entrada (Pantalla)
pantalla = tk.Entry(marcoPrincipal, textvariable=marcar_caracter, font=("Arial", 20),
                    bd=4, relief="sunken", justify="right")
pantalla.pack(fill="both", padx=10, pady=10)

#Marco para Teclado
teclado = tk.Frame(marcoPrincipal)
teclado.pack()

#Arreglo del teclado (números y operadores)
teclas = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '.', '+'],
    ['=']
]

#Poner color al texto de las teclas
colores_texto = {
    'C': 'red',
    '=': 'green',
    '/': 'blue',
    '*': 'blue',
    '-': 'blue',
    '+': 'blue',
    '.': 'black',
    '0': 'black',
    '1': 'black',
    '2': 'black',
    '3': 'black',
    '4': 'black',
    '5': 'black',
    '6': 'black',
    '7': 'black',
    '8': 'black',
    '9': 'black',
}

#Crear botones para el teclado
for fila in teclas:
    fila_marco = tk.Frame(teclado)
    fila_marco.pack(expand=True, fill="both")

    for boton in fila:    
        def crear_comando(boton_texto):
            def comando():
                ejecutar_accion(boton_texto)
            return comando
        color = colores_texto.get(boton, "black")

        tecla = tk.Button(
            fila_marco,
            text=boton,
            font=("Arial", 18),
            fg=color,
            width=5,
            height=2,
            command=crear_comando(boton)
        )
        tecla.pack(side="left", expand=True, fill="both")

pantalla.focus()
marcoPrincipal.bind('<Return>', tecla_enter)

marcoPrincipal.mainloop()