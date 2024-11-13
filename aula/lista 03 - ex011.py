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
pegou_pipoca = False
rodada_parado = False
pipoca_destruida = False
voltar_para_casa = False

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
    # se não estiver, movimentando-o para esquerda
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

    if not pegou_pipoca and 'P' not in cinema[pipoca_y]:
        pipoca_destruida = True

    if 'V' not in cinema[voce_y]:
        voltar_para_casa = True

    # verificando se a pessoa foi pega pelo cambista
    if not voltar_para_casa:

        # recebendo o movimento da pessoa e executando-o
        movimento = str(input())

        # checando se a pessoa acabou de pegar a pipoca
        if not rodada_parado:

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

            # caso a pessoa tenha encontrado o cambista
            if 'C' not in cinema[cambista_y]:
                cinema[cambista_y].insert(cinema[cambista_y].index('V'), 'C')
                cinema[cambista_y].remove('V')

                for fileira in cinema:
                    for idx_posicao, posicao in enumerate(fileira):
                        if idx_posicao < 7:
                            print(f'{posicao}', end=' ')
                        else:
                            print(f'{posicao}')

                break

    # imprimindo a situação do "cinema" após as movimentações
    for fileira in cinema:
        for idx_posicao, posicao in enumerate(fileira):
            if idx_posicao < 7:
                print(f'{posicao}', end=' ')
            else:
                print(f'{posicao}')

    # verificando se o laço deve ser extinto
    if 'O' not in cinema[oppenheimer_y] or 'B' not in cinema[barbie_y] or 'V' not in cinema[voce_y]:
        acabou = True

    # caso não tenha sido
    if not acabou:

        # se ainda não tiver a pipoca
        if 'P' in cinema[pipoca_y] or pipoca_destruida:
            print('Ainda não achei a pipoca')

        # se já tiver a pipoca
        else:

            # se  acabou de pegar
            if not pegou_pipoca:
                print('Finalmente! Peguei a pipoca')
                pegou_pipoca = True
                rodada_parado = True

            # se pegou em rodadas passadas
            else:
                print('Já peguei a pipoca')
                rodada_parado = False

        # calculando a distância entre a pessoa e o cambista e retornando a mensagem correspondente
        distancia_pessoa_cambista = (((voce_x - cambista_x) ** 2) + ((voce_y - cambista_y) ** 2)) ** .5

        if distancia_pessoa_cambista <= 3:
            print('Preciso acelerar, o cambista tá na minha cola!\n')

        elif 3 < distancia_pessoa_cambista <= 4:
            print('Consigo ver lá longe o cambista, mas é melhor acelerar!\n')

        else:
            print('O cambista está longe, mas não posso ficar parado\n')

# caso a pessoa tenha entrado em uma sala sem pipoca
if (pipoca_destruida or not pegou_pipoca) and 'V' in cinema[voce_y]:
    print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')

# caso a pessoa tenha entrado no filme da barbie com pipoca
elif 'B' not in cinema[barbie_y] and pegou_pipoca and not pipoca_destruida:
    print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')

# caso a pessoa tenha entrado no filme do oppenheimer com pipoca
elif 'O' not in cinema[oppenheimer_y] and pegou_pipoca and not pipoca_destruida:
    print('Aí sim, que filmaço! Christopher Nolan nunca erra!')

elif 'V' not in cinema[voce_y]:
    print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
