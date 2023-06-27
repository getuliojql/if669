#criando variáveis para as vitórias
vitorias_1 = 0
vitorias_2 = 0

#lendo os nomes dos times
time_1 = str(input())
time_2 = str(input())

#1° jogo
pontuacao1 = int(input())
pontuacao2 = int(input())
if pontuacao1 > pontuacao2:
    vitorias_1 = 1
    print(f'O vencedor da 1ª rodada foi: {time_1}')
else:
    vitorias_2 = 1
    print(f'O vencedor da 1ª rodada foi: {time_2}')

#2° jogo
pontuacao1 = int(input())
pontuacao2 = int(input())
if pontuacao1 > pontuacao2:
    vitorias_1 += 1
    print(f'O vencedor da 2ª rodada foi: {time_1}')
else:
    vitorias_2 += 1
    print(f'O vencedor da 2ª rodada foi: {time_2}')

#3° jogo
pontuacao1 = int(input())
pontuacao2 = int(input())
if pontuacao1 > pontuacao2:
    vitorias_1 += 1
    print(f'O vencedor da 3ª rodada foi: {time_1}')
else:
    vitorias_2 += 1
    print(f'O vencedor da 3ª rodada foi: {time_2}')

#verificando se já houve vencedor
if vitorias_1 == 3:
    print(f'O time {time_1} ganhou a partida final!')
elif vitorias_2 == 3:
    print(f'O time {time_2} ganhou a partida final!')

#4° jogo
else:
    pontuacao1 = int(input())
    pontuacao2 = int(input())
    if pontuacao1 > pontuacao2:
        vitorias_1 += 1
        print(f'O vencedor da 4ª rodada foi: {time_1}')
    else:
        vitorias_2 += 1
        print(f'O vencedor da 4ª rodada foi: {time_2}')

    #verificando se já houve vencedor
    if vitorias_1 >= 3:
        print(f'O time {time_1} ganhou a partida final!')
    elif vitorias_2 >= 3:
        print(f'O time {time_2} ganhou a partida final!')

    #5° jogo
    else:
        pontuacao1 = int(input())
        pontuacao2 = int(input())
        if pontuacao1 > pontuacao2:
            vitorias_1 += 1
            print(f'O vencedor da 5ª rodada foi: {time_1}')
        else:
            vitorias_2 += 1
            print(f'O vencedor da 5ª rodada foi: {time_2}')

        #declarando o vencedor
        if vitorias_1 > vitorias_2:
            print(f'O time {time_1} ganhou a partida final!')
        else:
            print(f'O time {time_2} ganhou a partida final!')
