# criando a matriz que representa o cinema
cinema = []

for f in range(8):
    cinema.append([])

for idx_fileira, fileira in enumerate(cinema):
    for f in range(8):
        cinema[idx_fileira].append('-')

# recebendo as coordenadas de cada um e os colocando no "cinema"
voce_y = int(input())
voce_x = int(input())
cinema[voce_y].pop(voce_x)
cinema[voce_y].insert(voce_x, 'V')

cambista_y = int(input())
cambista_x = int(input())
cinema[cambista_y].pop(cambista_x)
cinema[cambista_y].insert(cambista_x, 'C')

pipoca_y = int(input())
pipoca_x = int(input())
cinema[pipoca_y].pop(pipoca_x)
cinema[pipoca_y].insert(pipoca_x, 'P')

barbie_y = int(input())
barbie_x = int(input())
cinema[barbie_y].pop(barbie_x)
cinema[barbie_y].insert(barbie_x, 'B')

oppenheimer_y = int(input())
oppenheimer_x = int(input())
cinema[oppenheimer_y].pop(oppenheimer_x)
cinema[oppenheimer_y].insert(oppenheimer_x, 'O')

# definindo algumas variáveis
acabou = False

# início da jornada
while not acabou:

    # se o cambista estiver na mesma coluna
    if cambista_x == voce_x:

        # movimentando-o para cima
        if cambista_y > voce_y:
            cinema[cambista_y - 1].pop(cambista_x)
            cinema[cambista_y - 1].insert(cambista_x, 'C')
            cinema[cambista_y].insert(cambista_x, '-')
            cinema[cambista_y].remove('C')
            cambista_y -= 1

        # movimentando-o para baixo
        elif cambista_y < voce_y:
            cinema[cambista_y + 1].pop(cambista_x)
            cinema[cambista_y + 1].insert(cambista_x, 'C')
            cinema[cambista_y].insert(cambista_x, '-')
            cinema[cambista_y].remove('C')
            cambista_y += 1
    # movimentando-o para esquerda
    elif cambista_x > voce_x:
        if cinema[cambista_y].index('C') > 0:
            cinema[cambista_y].pop(cinema[cambista_y].index('C') - 1)
            cinema[cambista_y].insert(cinema[cambista_y].index('C') + 1, '-')
            cambista_x -= 1
    # movimentando-o para direita
    elif cambista_x < voce_x:
        if cinema[cambista_y].index('C') < 7:
            cinema[cambista_y].insert(cinema[cambista_y].index('C'), '-')
            cinema[cambista_y].pop(cinema[cambista_y].index('C') + 1)
            cambista_x += 1

    # recebendo o movimento da pessoa e executando-o
    movimento = str(input())

    if movimento == 'cima':
        if voce_y > 0:
            cinema[voce_y - 1].pop(voce_x)
            cinema[voce_y - 1].insert(voce_x, 'V')
            cinema[voce_y].insert(voce_x, '-')
            cinema[voce_y].remove('V')
            voce_y -= 1

    elif movimento == 'baixo':
        if voce_y < 7:
            cinema[voce_y + 1].pop(voce_x)
            cinema[voce_y + 1].insert(voce_x, 'V')
            cinema[voce_y].insert(voce_x, '-')
            cinema[voce_y].remove('V')
            voce_y += 1
    elif movimento == 'esquerda':
        if cinema[voce_y].index('V') > 0:
            cinema[voce_y].pop(cinema[voce_y].index('V') - 1)
            cinema[voce_y].insert(cinema[voce_y].index('V') + 1, '-')
            voce_x -= 1

    elif movimento == 'direita':
        if cinema[voce_y].index('V') < 7:
            cinema[voce_y].insert(cinema[voce_y].index('V'), '-')
            cinema[voce_y].pop(cinema[voce_y].index('V') + 1)
            voce_x += 1

    # imprimindo a situação do "cinema" após as movimentações
    for fileira in cinema:
        for idx_posicao, posicao in enumerate(fileira):
            if idx_posicao < 7:
                print(f'{posicao}', end=' ')
            else:
                print(f'{posicao}')
