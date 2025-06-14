# Ejercicio de calculadora básica
# Se crea módulos y paquetes

from Fundamentos import nuevo_tema # Con esto estamos importando la función del archivo Fundamentos.py
import Calc.operaciones as  c #Importar eñ módulo operaciones de la carpeta Calc y ponle alías "c"

if __name__ == "__main__":
    nuevo_tema("Módulos y Paquetes")

    print(c.resta(4, 1))
    print(c.suma(2, 3, 3))
    print(c.mult(5, 6))
    print(c.div(11, 2.5))
