nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
print('{}, {} anos, pesa {:.2f}kg!'.format(nome, idade, peso))

base = float(input('Informe a medida da base do triângulo: '))
altura = float(input('Informe a medida da altura do triângulo: '))
print('A área do triângulo de base {} e altura {} é {}!'.format(base, altura, (base * altura) / 2))
