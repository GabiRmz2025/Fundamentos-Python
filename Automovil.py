#Ejemplo para crear CLASE
class Automovil:
    def __init__(self, marca, color):
        #Definir los atributos de la clase
        #Son los que empiezan con self
        self.marca = marca
        self.color = color
    def avanzar(self):
        print(f"El coche avanza y es un {self.marca}")
    def retroceder(self):
        print(f"El coche retrocede y es de color {self.color}")

if __name__ == "__main__":
    auto = Automovil("BMW", "Azul") #Este es nuestro objeto auto
    auto.avanzar()
    auto.retroceder()

    auto1 =  Automovil("Honda", "Gris")
    auto1.retroceder()
    auto1.avanzar()
