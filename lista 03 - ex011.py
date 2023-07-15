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

    # imprimindo a situação do "cinema" após as movimentações
    for fileira in cinema:
        for idx_posicao, posicao in enumerate(fileira):
            if idx_posicao < 7:
                print(f'{posicao}', end=' ')
            else:
                print(f'{posicao}')