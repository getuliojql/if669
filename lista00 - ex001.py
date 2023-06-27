x = int(input('Digite o valor x: '))
y = int(input('Digite o valor y: '))
if x == 0:
    if y == 0:
        print('Esse ponto se encontra na origem (0,0).')
    else:
        print('Esse ponto se encontra no eixo Y (0,{}).'.format(y))
elif y == 0:
    print('Esse ponto se encontra no eixo X ({},0).'.format(x))
elif x > 0 and y > 0:
    print('Esse ponto se encontra no 1° quadrante ({},{}).'.format(x, y))
elif x < 0 < y:
    print('Esse ponto se encontra no 2° quadrante ({},{}).'.format(x, y))
elif x < 0 and y < 0:
    print('Esse ponto se encontra no 3° quadrante ({},{}).'.format(x, y))
else:
    print('Esse ponto se encontra no 4° quadrante ({},{}).'.format(x, y))
