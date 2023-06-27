#definindo número de duplas
duplas = int(input())
controle = 1

#1ª dupla
nome_1 = str(input())
periodo_1 = int(input())
pontuacao_1 = int(input())
final_1 = pontuacao_1 / periodo_1

#dupla vencedora
nome_v = nome_1
final_v = final_1

#dupla perdedora
nome_p = nome_1
final_p = final_1

#cálculo
for c in range(0, duplas - 1):
    nome_2 = str(input())
    periodo_2 = int(input())
    pontuacao_2 = int(input())
    final_2 = pontuacao_2 / periodo_2

#modificando a dupla vencedora
    while final_2 > final_v and controle != 0:
        nome_v = nome_2
        final_v = final_2

#modificando a dupla perdedora
    while final_2 < final_p and final_2 != 0:
        nome_p = nome_2
        final_p = final_2

#resultado
print(f'A dupla vencedora foi {nome_v} com a pontuação final de {final_v:.2f} pontos.')
print(f'A dupla perdedora foi {nome_p} com a pontuação final de {final_p:.2f} pontos.')

'''
#definindo número de duplas
duplas = int(input())

#1ª dupla
nome_1 = str(input())
periodo_1 = int(input())
pontuacao_1 = int(input())
final_1 = pontuacao_1 / periodo_1

#dupla vencedora
nome_v = ''
final_v = 0

#dupla perdedora
nome_p = ''
final_p = 0

#cálculo
for c in range(0, duplas - 1):
    nome_2 = str(input())
    periodo_2 = int(input())
    pontuacao_2 = int(input())
    final_2 = pontuacao_2 / periodo_2

#modificando a dupla vencedora
    while final_2 > final_1 and final_2 != 0:
        nome_v = nome_2
        final_v = final_2
        final_2 = 0
    else:
        nome_v = nome_1
        final_v = final_1

#modificando a dupla perdedora
    while final_2 < final_1 and final_2 != 0:
        nome_p = nome_2
        final_p = final_2
        final_2 = 0
    else:
        nome_p = nome_1
        final_p = final_1

#resultado
print(f'A dupla vencedora foi {nome_v} com a pontuação final de {final_v:.2f} pontos.')
print(f'A dupla perdedora foi {nome_p} com a pontuação final de {final_p:.2f} pontos.')


#definindo número de duplas
duplas = int(input())
controle = 1

#1ª dupla
nome_1 = str(input())
periodo_1 = int(input())
pontuacao_1 = int(input())
final_1 = pontuacao_1 / periodo_1

#dupla vencedora
nome_v = nome_1
final_v = final_1

#dupla perdedora
nome_p = nome_1
final_p = final_1

#cálculo
for c in range(0, duplas - 1):
    nome_2 = str(input())
    periodo_2 = int(input())
    pontuacao_2 = int(input())
    final_2 = pontuacao_2 / periodo_2

#modificando a dupla vencedora
    while final_2 > final_v and controle != 0:
        nome_v = nome_2
        final_v = final_2
        controle = 0
    controle = 1

#modificando a dupla perdedora
    while final_2 < final_p and final_2 != 0:
        nome_p = nome_2
        final_p = final_2
        controle = 0
    controle = 1

#resultado        
print(f'A dupla vencedora foi {nome_v} com a pontuação final de {final_v:.2f} pontos.')
print(f'A dupla perdedora foi {nome_p} com a pontuação final de {final_p:.2f} pontos.')


#definindo número de duplas
duplas = int(input())
controle = 1

#1ª dupla
nome_1 = str(input())
periodo_1 = int(input())
pontuacao_1 = int(input())
final_1 = pontuacao_1 / periodo_1

#dupla vencedora
nome_v = ''
final_v = 0

#dupla perdedora
nome_p = ''
final_p = 0

#cálculo
for c in range(0, duplas - 1):
    nome_2 = str(input())
    periodo_2 = int(input())
    pontuacao_2 = int(input())
    final_2 = pontuacao_2 / periodo_2

#modificando a dupla vencedora
    while final_2 > final_1 and controle != 0:
        nome_v = nome_2
        final_v = final_2
        controle = 0
    if final_1 > final_2:
        nome_v = nome_1
        final_v = final_1
    controle = 1

#modificando a dupla perdedora
    while final_2 < final_1 and final_2 != 0:
        nome_p = nome_2
        final_p = final_2
        controle = 0
    if final_1 < final_2:
        nome_p = nome_1
        final_p = final_1
    controle = 1
#resultado        
print(f'A dupla vencedora foi {nome_v} com a pontuação final de {final_v:.2f} pontos.')
print(f'A dupla perdedora foi {nome_p} com a pontuação final de {final_p:.2f} pontos.')
'''