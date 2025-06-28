#Actividad Turtle 5. Flecha punteada en incremento
import turtle
from turtle import *
import time

#Esta primer forma tiene un tope
#El máximo de "a", inicia con "4", incrementa de dos en dos
'''for a in range(4, 22, 2):
    forward(a)
    time.sleep(1)
    penup()
    forward(5)
    pendown()
    time.sleep(1)
    print (a)
turtle.done()'''

a = int(8)

# Esta forma repite 8 veces el ciclo incrementando de tres en tres donde el valor a inicia en 8
for _ in range(8):
    
    forward(a)
    penup()
    forward(5)
    pendown()
    time.sleep(1)

    a += 3

time.sleep(2)

#turtle.done()
