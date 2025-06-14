#Ejemplo de serializar´es un archivo binario
import pickle

info = [35, 88, 3.14, 16]

with open("./archivos/ArchivoSerial.txt","wb") as binFile:
    pickle.dump(info, binFile)

print("Archivo binario escrito")

with open("./archivos/ArchivoSerial.txt","rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)

print("Archivo binario leído y resconstuido")