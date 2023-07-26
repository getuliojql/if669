import turtle
from time import sleep


def linha(tam, hor):
    for lin in range(hor):
        for q in range(4):
            t.forward(tam)
            t.left(90)
        t.forward(tam)


tela = turtle.Screen()
t = turtle.Turtle()

t.shape('turtle')
t.turtlesize(2, 2, 3)
t.pensize(5)

tamanho_celula = int(input('Informe o tamanho desejado para cada aresta dos quadrados: '))
grid_x = int(input('Informe quantos quadrados deseja imprimir horizontalmente: '))
grid_y = int(input('Informe quantos quadrados deseja imprimir verticalmente: '))

print('PROCESSANDO...')
sleep(2)
print('Tudo pronto! Aqui vai seu padrão quadricular paramétrico:')

for col in range(grid_y):
    linha(tamanho_celula, grid_x)
    t.left(180)
    t.forward(tamanho_celula * grid_x)

    if col < grid_y - 1:
        t.left(90)
        t.forward(tamanho_celula)
        t.left(90)

    else:
        t.right(90)

turtle.done()

# #### AULA 1 ⤵ #### #
'''import turtle

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

turtle.done()'''
