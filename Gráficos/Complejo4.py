#4to. Ejercicio de Turtle, Estrella Múltiples picos
#Colorear rojo y amarillo

from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

