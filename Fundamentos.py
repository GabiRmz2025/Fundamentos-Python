# En python una función se define con def
# en las siguientes líneas tenemos la creación de una función
# pass sgnifica vacia


#def nuevoTema(tema):
#    print("\n----- ", tema, " -----\n")

def nuevo_tema(tema:str):
    print(f"\n----- {tema} -----\n")



if __name__ == "__main__":

    #Este es un comentario de una sola línea
    '''Es un comentario de varias líneas
    son tres comillas al inicio y final de parrafo'''
    
    nuevo_tema("OPERADORES ARITMÉTICOS")
    #print("----- Operadores aritméticos -----")
    # Ejercicios usando operadores aritméticos
    print("operador suma, 5 + 6 =", 5 + 6)
    print("operador resta, 9 - 8 =", 9 - 8)
    print("operador multiplicación, 9 * 8 =", 9 * 8)
    print("operador división, 440 / 4 =", 440 / 4)
    print("operador división entero, 85 // 3 =", 85 // 3)
    print("operador exponente, 6 ** 3=", 6 ** 3)
    print("operador módulo, 27 % 5 =", 27 % 5)
    print("operador cambio de signo, -( 4 - 6 ) =", -( 4 - 6 ))
    print("varios operadores, ( (4 + 5) * 2 / 3) =", (4 + 5) * 2 / 3)
    print("")
    # Ejercicios usando operadores lógicos
    # not=negación, or=disyunción, and=conjunción
    print("")
    print("----- Tablas de Verdad ----")    
    print("Haciendo uso de los Operadores Lógicos (and, or, not)")
    print("")
    
    nuevo_tema("OPERADOR AND")
    #print("--- Operador And ---")
    print("True and True, resulta =", True and True)
    print("True and False, resulta =", True and False)
    print("False and True, resulta =", False and True)
    print("False and False, resulta =", False and False)
    print("")
    nuevo_tema("OPERADOR OR")
    #print("--- Operador Or ---")
    print("True or True, resulta =", True or True)
    print("True or False, resulta =", True or False)
    print("False or True, resulta =", False or True)
    print("False or False, resulta =", False or False)
    print("Not de True and False, resulta =", True and False)
    print("")
    nuevo_tema("OPERADOR NOT")
    #print("--- Operador Not ---")
    print("Negación de True, resulta =", not True )
    print("Negación de True or False, resulta =", not (True or False))
    print("")
    print("----- Operadores de Comparación -----")
    print("")
    #ejercicios usando operadores de comparación
    print("Respuesta de 37.4 == 37.4: ", 37.4 == 37.4)
    print("48 es != de 48.7, respuesta:", 48 != 48.7)
    print("48.1 es menor que (<) 48, respuesta =", 48.1 < 48)
    print("48.7 mas 0.5 es mayor que 48, respuesta: ", 48.7 > 48)
    print("El resultado de ( 5 + 4 ) es mayor o igual que ( 3 * 3 ):", ( 5 + 4 ) >= ( 3 * 3 ))
    print("Ejemplo completo: (True or (2 == 1 + 2)) == True: ", (True or (2 == 1 + 2)) == True)

#Ejemplo para definir variables
nuevo_tema("Variables")
variable1 = 10
_variable2 =  6.246
Variable3 =  "Pepe"
nombreVariable = 8
nombre_variable = 67.3
print(variable1, _variable2, Variable3, nombreVariable, nombre_variable)

a, b, c, = 5, 88.9, "Prueba de Variable"
print(a)
print(b)
print(c)
#Ejemplo para definir una variable dinámica
nombre_variable = "ADIOS"
print(nombre_variable)

#Ejemplo número enteros
nuevo_tema("ENTEROS")
w =103
x = 9876543210123456
y = -56
z = 0b00110011
h = 0xFF
print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

#Ejemplo de Flotantes
nuevo_tema("FLOTANTES")
x = 1234.67
print(x, type(x))
y = -0.6754
print(y, type(y))

#Ejmeplo de Números Complejos
nuevo_tema("COMPLEJOS")
x =-46j
y = 12 + 45j
z = 2j
c = y + z
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(c, type(c))

#Ejemplo con números boleanos
nuevo_tema("BOLEANOS")
x = True
print(x, type(x))

#Ejemplo de Listas
nuevo_tema("LISTAS")
lista = [10, 29.6, "Lista de Python"]
print(lista)
print(lista[1])
#La lista empieza con 0, por lo tanto 10 es posición 0, 29.6 posición 1
lista[0] = "Hola"
print(lista)
#este es el ejemplo de mutable, cambio 10 por Hola en la posición 0
lista.append("dificil")
print(lista)
#Agregar un elemento al final de la lista
lista.insert(0, 1.1)
print(lista)
#Agregar un elemento en un posición específica
lista.append([3, 4, 5, 6, 7, 8])
print(lista)
#Imprime de la lista sólo la posición 5, esta es una lista o sublista
print(lista[5])
#imprime de la lista la posición 5 que es sublista de esta la posición 4
print(lista[5][4])
#imrpime una lista, el elemento 3 es una cadena esta es iterable, su posición es la a
print(lista[3][4])
#Ejemplo de TUPLAS
nuevo_tema("TUPLAS")
tupla = (25, "Tupla", 1 + 10j)
print(tupla)
print(tupla[1])
#tupla[0] = 0   es error porque no soporta objetos, operación no valida en tuplas
print(tupla)
tupla = (20, "Tupla", 1 + 10j, "Otro")
print(tupla)
#Ejemplo de Conjuntos
nuevo_tema("CONJUNTOS")
conjunto = {10, 20, 30, 40, 50, 20}
print(conjunto)
#No imprime el segundo "20",
#print(conjunto[1])   es error, porque no es ordenado no es iterable
conjunto.add(80)
print(conjunto)
print(50 in conjunto)

#Ejemplo de los Diccionarios
nuevo_tema("DICCIONARIOS")
diccionario = {"Nombre": "Gabriela",
               "Edad": 42,
               "Teléfono": "442-345-678", 
               90 : 4 + 3j}
print(diccionario)
print(diccionario["Nombre"])
print(diccionario[90])

#Ejemplo con CADENAS
nuevo_tema("CADENAS")
cadena1 = "Esto es una cadena"
cadena2 =  'Esto es otra cadena'
cadena3 =''' Cadena multilinea
se conforma por varias líneas
o puede ser parrafo, con 
    tabuladores'''
print(cadena1, type(cadena1))
print(cadena2, type(cadena2))
print(cadena3, type(cadena3))
cadena4 =  "Hola" * 5
print(cadena4)
print(cadena1[2])
print(cadena1[2:10])
print(cadena1[5:])
print(cadena1[5:])
print(cadena1[:-5])
print(cadena1[5:-5])
print(cadena1[::-1])