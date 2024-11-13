# recebendo variáveis iniciais
qtd_ideal_minutos = int(input())
qtd_jogadoras = int(input())

posicoes = []
minutos = []


for j in range(qtd_jogadoras):
    posicao_minuto = str(input()).split(' ')

    posicoes.append(posicao_minuto[0])
    minutos.append(posicao_minuto[1])

