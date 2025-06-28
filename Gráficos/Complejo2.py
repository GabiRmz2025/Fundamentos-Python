#2do. Ejercicio de Turtle, Esfera Multicolor
#Uso de ciclos, colores, tamaño de pincel

import turtle as tt
import time

tt.bgcolor('black')
tt.pensize(2)
tt.speed(6)

for i in range(6):
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow', 'pink', 'orange'):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()
