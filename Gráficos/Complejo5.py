#5to. Ejercicio de Turtle, Espiral de colores
from turtle import *
import time

for steps in range(50):
    for c in ('blue', 'magenta', 'green', 'red'):
        color(c)
        forward(steps)
        right(30)

time.sleep(5)
