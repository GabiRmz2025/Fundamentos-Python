#Ejemplo para crear un archivo de texto

file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo.")
file.close()

#Se escribe texto dento del archivo
lista = ["Fresa", "Mango", "Papaya"]

with open("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e + "\n")
print("Lista escrita en el archivo")

# Se escribe texto dentro del archivo
lista2 = ["honda", "Mango", "Papaya"]

with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)
print("Lista escrita con writelines.")

print("Imprimir todo el contenido del archivo.")

with open("EjemploArchivo.txt","r") as file:
    print(file.read())

#me falto ejercico

with open("EjemploArchivo.txt","r") as file:
    print(file.readline())
    print(file.readline(5))
print("Almacenar el contenido en una lista y mostra el contenido del archivo")

with open("EjemploArchivo.txt","r") as file:
    contenido =file.readlines()
    print(contenido[-1])
