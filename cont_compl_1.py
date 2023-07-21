import turtle

tela = turtle.Screen()
t = turtle.Turtle()

t.shape('turtle')
t.turtlesize(2, 2, 3)
t.pensize(5)


def poligono(lados, tamanho, cor):
    angulo = 360 / lados
    for c in range(lados):
        t.color(cor)
        t.forward(tamanho)
        t.left(angulo)


t.speed(0)

cores = ['violet', 'purple', 'blue', 'green', 'yellow', 'orange', 'red']

for i in range(3, 13):
    poligono(i, 100, cores[i % len(cores) - 3])

turtle.done()
