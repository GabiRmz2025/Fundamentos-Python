#Actividad Turtle 4. Flecha punteada

from turtle import *
import time

for _ in range(8):
    forward(10)
    penup()
    forward(6)
    pendown()
    time.sleep(1)

turtle.done()
