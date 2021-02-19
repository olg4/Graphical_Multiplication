"""
Projet_2 "Les jolies tables"
28_octobre_2016
*Olga Baitemirova*
entrer en paramètre (ligne de commande):
55 500 150 250 1 1 254 130 1
"""

import turtle, math, sys
from sys import argv

turtle.reset()
turtle.colormode(255)
k = int(argv[1])          #table de multiplication
n = int(argv[2])          #modulo
r = int(argv[3])          #rayon du cercle
r1 = int(argv[4])         #("Red1") ; couleurs 1ere composante
g1 = int(argv[5])         #("Green1")
b1 = int(argv[6])         #("Blue1")
r2 = int(argv[7])         #("Red2") ; couleurs 2e composante
g2 = int(argv[8])         #("Green2")
b2 = int(argv[9])         #("Blue2")
turtle.speed(0)
turtle.up()               # démarrer à partir du point 0
turtle.forward(r)         # repère:cercle trigonomètrique
turtle.left(90)
turtle.down()             # division du cercle en n partie pour répartir
turtle.circle(r)          # ...les points uniformément
angle = 360 / n
turtle.colormode(255)
for i in range(n):
    x = r * math.cos(math.radians(angle * i))  # placement des n points
    y = r * math.sin(math.radians(angle * i))  # composantes axe X et Y
    turtle.up()                                # ne pas tracer ces composantes
    turtle.goto(x, y)
    j = (i * k) % n                            # formule qui dirige la tortue
    x = r * math.cos(math.radians(angle * j))
    y = r * math.sin(math.radians(angle * j))
    turtle.down()
    red = int((((r2 - r1)*i // n) + r1))
    green = int((((g2 - g1)*i // n) + g1))
    blue = int((((b2 - b1)*i // n) + b1))
    turtle.pencolor(red,green,blue)
    turtle.goto((x, y))
out=int(input())
