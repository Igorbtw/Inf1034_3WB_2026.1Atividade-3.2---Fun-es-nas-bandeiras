from turtle import *
from time import sleep  

t = Turtle()

t.speed(100)

t.hideturtle()

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(larg)
        t.left(90)
        t.forward(alt)
        t.left(90)
    t.end_fill()

def desenha_bandeira_japao():
    desenha_retangulo(-100, -50, 200, 130, "white")


def desenha_circulo(x, y, color, raio):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()


def desenha_circulo_japão():
    desenha_circulo(0, -25, "red", 40)


desenha_bandeira_japao()

desenha_circulo_japão()

sleep(2)
t.clear()

#italia
def desenha_bandeira_italia():
    desenha_retangulo(-200, 200, 50, 150, "green")
    desenha_retangulo(-150, 200, 50, 150, "white")
    desenha_retangulo(-100, 200, 50, 150, "red")

desenha_bandeira_italia()

sleep(2)
t.clear()

#jordania
def desenha_bandeira_jordania():
    desenha_retangulo(-100, 36.6, 150, 50, "black")
    desenha_retangulo(-100, -6.7, 150, 50, "white")
    desenha_retangulo(-100, -50, 150, 50, "red")

def desenhar_triangulo(x, y, alt, color):
    









desenha_bandeira_jordania()




mainloop()       