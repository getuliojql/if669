


























'''def tela_informacoes(nome, propulsores, vel_inicio, vel_fim):
    print(f'--- Participante: {nome} ---')
    print(f'Qtd de propulsores Final: {propulsores}')
    print(f'Velocidade Inicial: {vel_inicio} km/h')
    print(f'Velocidade Final: {vel_fim} km/h')


acabou = False
proximo = True
participantes = 0
desclassificados = 0

frase_pitstop = 'Pit-Stop Espacial'
frase_bateu = 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.'
frase_desclassificado = 'Opa esse participante não está inscrito, desclassificando em 3, 2, 1...'

while not acabou:

    if proximo:
        informacoes_participante = str(input()).split(' ')

        if informacoes_participante != ['Próximo'] and informacoes_participante != ['FIM']:

            informacoes_participante[1] = int(informacoes_participante[1])
            informacoes_participante[2] = int(informacoes_participante[2])
            velocidade_inicial = informacoes_participante[1] * informacoes_participante[2]
            proximo = False

    if informacoes_participante == ['Próximo']:
        situacao = 'Próximo'

    elif informacoes_participante == ['FIM']:
        situacao = 'FIM'
        break

    else:
        situacao = str(input())

    if situacao == frase_pitstop:
        informacoes_participante[1] += 1

    elif situacao == frase_bateu:
        informacoes_participante[1] -= 1

    if informacoes_participante[1] < 1:
        desclassificados += 1
        print(f'BUUMM!! Infelizmente, {informacoes_participante[0]} está fora da corrida.')
        proximo = True

    else:

        if situacao == frase_desclassificado:
            desclassificados += 1
            print(f'O {informacoes_participante[0]} achou que não descobriríamos, '
                  f'tirem {informacoes_participante[0]} imediatamente da pista.')
            proximo = True

        elif situacao == 'Próximo' or situacao == 'FIM':
            velocidade_final = informacoes_participante[1] * informacoes_participante[2]
            tela_informacoes(informacoes_participante[0], informacoes_participante[1], velocidade_inicial, velocidade_final)
            participantes += 1

            if situacao == 'Próximo':
                proximo = True

            elif situacao == 'FIM':
                acabou = True

if desclassificados < participantes:
    print(f'Relatório da CIn Pod Race: {participantes} participantes terminaram a corrida '
          f'e {desclassificados} foram desclassificados.')

else:
    print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')
'''



























'''
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
acabou = pegou_pipoca = rodada_parado = pipoca_destruida = voltar_para_casa = False

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

    # vendo se o cambista passou por cima da pipoca
    if not pegou_pipoca and 'P' not in cinema[pipoca_y]:
        pipoca_destruida = True

    # verificando se a pessoa foi pega pelo cambista
    if 'V' not in cinema[voce_y]:
        voltar_para_casa = True

    # caso ela não tenha sido
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

        # se ainda não tiver a pipoca ou ela foi destruída
        if 'P' in cinema[pipoca_y] or pipoca_destruida:
            print('Ainda não achei a pipoca')

        # se já tiver a pipoca
        elif 'P' not in cinema[pipoca_y] and not pipoca_destruida:

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
    print('Ah não, vou passar fome! Não tem graça assistir filme sem uma pipoquinha.')

# caso a pessoa tenha entrado no filme da barbie com pipoca
elif 'B' not in cinema[barbie_y] and pegou_pipoca and not pipoca_destruida:
    print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')

# caso a pessoa tenha entrado no filme do oppenheimer com pipoca
elif 'O' not in cinema[oppenheimer_y] and pegou_pipoca and not pipoca_destruida:
    print('Aí sim, que filmaço! Christopher Nolan nunca erra!')

# caso a pessoa tenha sido pega pelo cambista
elif 'V' not in cinema[voce_y]:
    print('Droga! Agora volto pra casa sem filme e sem dinheiro.')

'''



















'''     cinema[voce_y].remove('V')
        cinema[voce_y].append('-')
        cinema[voce_y - 1].insert(voce_x, 'V')
        voce_y -= 1'''


























'''while not achou and not acabou:
    for idx_numero, numero in enumerate(minutos):
        if int(numero) + somatorio < qtd_ideal_minutos:
            somatorio += int(numero)

        elif int(numero) + somatorio == qtd_ideal_minutos:
            somatorio += int(numero)
            achou = True

        if not achou:
            if len(minutos) > 0:
                minutos.pop(0)
            else:
                acabou = True

if achou:
    print('Conquistamos nossa primeira estrela!')

elif acabou:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')
'''













# recebendo as opções de cada seção do look e definindo o meio
penteado = str(input()).split(' - ')
opcao_meio_penteado = penteado[(len(penteado) // 2)]
idx_opcao_meio_penteado = penteado.index(opcao_meio_penteado)

top = str(input()).split(' - ')
opcao_meio_top = top[(len(top) // 2)]
idx_opcao_meio_top = top.index(opcao_meio_top)

bottom = str(input()).split(' - ')
opcao_meio_bottom = bottom[(len(bottom) // 2)]
idx_opcao_meio_bottom = bottom.index(opcao_meio_bottom)

sapatos = str(input()).split(' - ')
opcao_meio_sapatos = sapatos[(len(sapatos) // 2)]
idx_opcao_meio_sapatos = sapatos.index(opcao_meio_sapatos)

print('Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!')

# recebendo dados da roleta e mesclando look
roleta = str(input()).replace('<', ' esquerda').replace('>', ' direita').split(' ')
print('Iniciando mesclagem...')

if roleta[1] == 'esquerda':
    opcao_escolhida_penteado = penteado[(idx_opcao_meio_penteado - (int(roleta[0])) % len(penteado)) % len(penteado)]
else:
    opcao_escolhida_penteado = penteado[(idx_opcao_meio_penteado + (int(roleta[0])) % len(penteado)) % len(penteado)]


if roleta[3] == 'esquerda':
    opcao_escolhida_top = top[(idx_opcao_meio_top - (int(roleta[2])) % len(top)) % len(top)]
else:
    opcao_escolhida_top = top[(idx_opcao_meio_top + (int(roleta[2])) % len(top)) % len(top)]


if roleta[5] == 'esquerda':
    opcao_escolhida_bottom = bottom[(idx_opcao_meio_bottom - (int(roleta[4])) % len(bottom)) % len(bottom)]
else:
    opcao_escolhida_bottom = bottom[(idx_opcao_meio_bottom + (int(roleta[4])) % len(bottom)) % len(bottom)]


if roleta[7] == 'esquerda':
    opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos - (int(roleta[6])) % len(sapatos)) % len(sapatos)]
else:
    opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos + (int(roleta[6])) % len(sapatos)) % len(sapatos)]

print('O look gerado foi:')
print(f'cabelo {opcao_escolhida_penteado}, {opcao_escolhida_top} com {opcao_escolhida_bottom} e {opcao_escolhida_sapatos} nos pés.')


























'''sapatos = str(input()).split(' - ')
opcao_meio_sapatos = sapatos[(len(sapatos) // 2)]
idx_opcao_meio_sapatos = sapatos.index(opcao_meio_sapatos)

# recebendo dados da roleta e mesclando look
roleta = str(input()).replace('<', ' esquerda').replace('>', ' direita').split(' ')

if roleta[7] == 'esquerda':
    if int(roleta[6]) + idx_opcao_meio_sapatos > len(sapatos):
        opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos - (int(roleta[6])) % len(sapatos)) % len(sapatos)]
    else:
        opcao_escolhida_sapatos = sapatos[idx_opcao_meio_sapatos - int(roleta[6])]
else:
    if int(roleta[6]) + idx_opcao_meio_sapatos > len(sapatos):
        opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos + (int(roleta[6])) % len(sapatos)) % len(sapatos)]
    else:
        opcao_escolhida_sapatos = sapatos[idx_opcao_meio_sapatos + int(roleta[6])]
print('O look gerado foi:')
print(f'{opcao_escolhida_sapatos} nos pés.')
'''
















'''if roleta[3] == 'esquerda':
    opcao_escolhida_top = top[idx_opcao_meio_top - (int(roleta[2])) % len(top)]

else:
    opcao_escolhida_top = top[idx_opcao_meio_top + (int(roleta[2])) % len(top)]

if roleta[5] == 'esquerda':
    opcao_escolhida_bottom = bottom[idx_opcao_meio_bottom - (int(roleta[6])) % len(bottom)]

else:
    opcao_escolhida_bottom = bottom[idx_opcao_meio_bottom + (int(roleta[6])) % len(bottom)]


if roleta[7] == 'esquerda':
    opcao_escolhida_sapatos = sapatos[idx_opcao_meio_sapatos - (int(roleta[6])) % len(sapatos)]

else:
    opcao_escolhida_sapatos = sapatos[idx_opcao_meio_sapatos + (int(roleta[6])) % len(sapatos)]

print(opcao_escolhida_penteado)
print(opcao_escolhida_top)
print(opcao_escolhida_bottom)
print(opcao_escolhida_sapatos)'''


























#l03 - e04
'''a = ['chibata', 'carro', 'caminhao', 'caminhonete', 'trailer']
b = ['carro', 'chibata', 'chinelo', 'trailer', 'caminhonete']

for idx, palavra in enumerate(a):
    print(b.count(palavra))









nao_encontradas = 0
lista_inexistentes = []
a.sort()
b.sort()
for idx, profissao in enumerate(a):
    if a[idx] != b[idx]:
        nao_encontradas += 1
        lista_inexistentes.append(profissao)'''