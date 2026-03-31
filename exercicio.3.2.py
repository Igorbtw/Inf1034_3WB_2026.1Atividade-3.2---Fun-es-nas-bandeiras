from turtle import *
from time import sleep  

t = Turtle()

t.speed(100)

t.hideturtle()

def desenhar_retangulo(x, y, larg, alt, color):
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

def desenhar_bandeira_japao():
    desenhar_retangulo(-100, -50, 200, 130, "white")


def desenhar_circulo(x, y, color, raio):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()


def desenhar_circulo_japão():
    desenhar_circulo(0, -25, "red", 40)


desenhar_bandeira_japao()

desenhar_circulo_japão()

sleep(2)
t.clear()

#italia
def desenhar_bandeira_italia():
    desenhar_retangulo(-200, 200, 50, 150, "green")
    desenhar_retangulo(-150, 200, 50, 150, "white")
    desenhar_retangulo(-100, 200, 50, 150, "red")

desenhar_bandeira_italia()

sleep(2)
t.clear()

#JORDANIA



def estrela_generica(x, y, larg, alt, pontas, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.right(larg) 
    t.begin_fill()
    angulo = 180 - (180 / pontas)
    for _ in range(pontas):
        t.fd(alt)
        t.right(angulo)
    t.end_fill()
    t.left(larg)

def triangulo_jordania(x, y, color):
    t.pu()
    t.goto(x, y) 
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(-30, 15)      
    t.goto(-100, 80)     
    t.goto(x, y) 
    t.end_fill()


def bandeira_jordania():
    desenhar_retangulo(-100, 36.6, 200, 43.3, "black")
    t.color("black", "white")
    desenhar_retangulo(-100, -6.7, 200, 43.3, "white")
    desenhar_retangulo(-100, -50, 200, 43.3, "green")
    triangulo_jordania(-100, -50, "red")
    estrela_generica(-82, 12, 0, 18, 7, "white")


bandeira_jordania()

sleep(2)
t.clear()


#CHILE

def bandeira_chile():
    desenhar_retangulo(-100, -50, 200, 65, "red")
    desenhar_retangulo(0, 15, 100, 65, "white")
    desenhar_retangulo(-100, 15, 100, 65, "blue")
    estrela_vermelha_iemen(-65, 50, 0, 30, "white")

bandeira_chile()

sleep(2)
t.clear()

#IEMEN DO SUL

def desenhar_triangulo_iemen(x, y, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(-50, 0)
    t.goto(-150, 100)
    t.goto(-150, -100)
    t.end_fill()

def estrela_vermelha_iemen(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.right(larg)
    t.begin_fill()

    for _ in range(5):
        t.fd(alt)
        t.right(144)
    
    t.end_fill()


def bandeira_iemen():
    desenhar_retangulo(-150, 33, 300, 67, "red")
    desenhar_retangulo(-150, -34, 300, 67, "white")
    desenhar_retangulo(-150, -100, 300, 67, "black")
    desenhar_triangulo_iemen(-150, -100, "skyblue")
    estrela_vermelha_iemen(-125, 20, 20, 45, "red")
    
bandeira_iemen()
sleep(2)
t.clear()

#PAQUISTAO

def desenhar_circulo_paquistao(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()

def estrela_paquistao(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.right(larg)
    t.begin_fill()
    for _ in range(5):
        t.forward(alt)
        t.right(144)
    t.end_fill()
    t.left(larg)

def bandeira_paquistao():
    t.color("black", "white")
    desenhar_retangulo(-100, -50, 50, 130, "white")
    t.color("darkgreen", "darkgreen")
    desenhar_retangulo(-50, -50, 150, 130, "darkgreen")
    desenhar_circulo_paquistao(15, -15, 35, "white")
    desenhar_circulo_paquistao(25, -5, 35, "darkgreen")
    estrela_paquistao(35, 50, 30, 20, "white")

bandeira_paquistao()

sleep(2)
t.clear()
sleep(2)

#PANAMA

def bandeira_panama():
    t.color("navy", "white")
    desenhar_retangulo(-100, 15, 100, 65, "white")
    estrela_vermelha_iemen(-65, 50, 0, 30, "navy")
    t.color("red", "red")
    desenhar_retangulo(0, 15, 100, 65, "red")
    t.color("navy", "navy")
    desenhar_retangulo(-100, -50, 100, 65, "navy")
    t.color("navy", "white")
    desenhar_retangulo(0, -50, 100, 65, "white")
    estrela_vermelha_iemen(35, -12, 0, 30, "red")

bandeira_panama()

sleep(2)

t.clear()
t.clear()

# SUDAO

t.left(20)

def bandeira_sudao():
    desenhar_retangulo(-150, 33, 300, 67, "red")
    desenhar_retangulo(-150, -34, 300, 67, "white")
    desenhar_retangulo(-150, -100, 300, 67, "black")
    desenhar_triangulo_iemen(-150, -100, "green")

bandeira_sudao()

sleep(2)
t.clear()

#COREIA DO NORTE

def bandeira_coreia_norte():
    desenhar_retangulo(-150, 50, 300, 30, "navy")
    desenhar_retangulo(-150, 40, 300, 10, "white")
    desenhar_retangulo(-150, -40, 300, 80, "red")
    desenhar_retangulo(-150, -50, 300, 10, "white")
    desenhar_retangulo(-150, -80, 300, 30, "navy")
    desenhar_circulo_paquistao(-50, -30, 30, "white")
    estrela_generica(-75, 10, 0, 50, 5, "red")

bandeira_coreia_norte()

sleep(2)
t.clear()

#ESTADOS UNIDOS

def bandeira_eua():
    desenhar_retangulo(-130, -65, 260, 130, "red")
    desenhar_retangulo(-130, -55, 260, 10, "white")
    desenhar_retangulo(-130, -35, 260, 10, "white")
    desenhar_retangulo(-130, -15, 260, 10, "white")
    desenhar_retangulo(-130, 5, 260, 10, "white")
    desenhar_retangulo(-130, 25, 260, 10, "white")
    desenhar_retangulo(-130, 45, 260, 10, "white")
    desenhar_retangulo(-130, -5, 100, 70, "navy")
    estrela_generica(-120, 50, 0, 5, 5, "white")
    estrela_generica(-100, 50, 0, 5, 5, "white")
    estrela_generica(-80, 50, 0, 5, 5, "white")
    estrela_generica(-60, 50, 0, 5, 5, "white")
    estrela_generica(-40, 50, 0, 5, 5, "white")
    estrela_generica(-110, 35, 0, 5, 5, "white")
    estrela_generica(-90, 35, 0, 5, 5, "white")
    estrela_generica(-70, 35, 0, 5, 5, "white")
    estrela_generica(-50, 35, 0, 5, 5, "white")
    estrela_generica(-30, 35, 0, 5, 5, "white")
    estrela_generica(-120, 20, 0, 5, 5, "white")
    estrela_generica(-100, 20, 0, 5, 5, "white")
    estrela_generica(-80, 20, 0, 5, 5, "white")
    estrela_generica(-60, 20, 0, 5, 5, "white")
    estrela_generica(-40, 20, 0, 5, 5, "white")
    estrela_generica(-110, 5, 0, 5, 5, "white")
    estrela_generica(-90, 5, 0, 5, 5, "white")
    estrela_generica(-70, 5, 0, 5, 5, "white")
    estrela_generica(-50, 5, 0, 5, 5, "white")
    estrela_generica(-30, 5, 0, 5, 5, "white")


bandeira_eua()

sleep(2)
t.clear()

#EXTRA

t.setheading(0)

nome = textinput("Bandeiras", "Digite o nome da bandeira:")

if nome == "japao":
    bandeira_japao()
else:
    if nome == "italia":
        bandeira_italia()
    else:
        if nome == "iemen":
            bandeira_iemen()
        else:
            if nome == "sudao":
                bandeira_sudao()
            else:
                if nome == "chile":
                    bandeira_chile()
                else:
                    if nome == "panama":
                        bandeira_panama()
                    else:
                        if nome == "jordania":
                            bandeira_jordania()
                        else:
                            if nome == "paquistao":
                                bandeira_paquistao()
                            else:
                                if nome == "eua":
                                    bandeira_eua()
                                else:
                                    if nome == "coreia":
                                        bandeira_coreia_norte()
                                    else:
                                        t.write("Nao encontrada")



sleep(2)
t.clear()

mainloop()       
