# variável de controle
barbie_continuar = True

# possíveis decisões da Barbie
decisao_1 = 'Amei!!'
decisao_2 = 'Acho que não combinou muito :/'
decisao_3 = 'Melhor escolher eu mesma'

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

# início da seleção de looks
while barbie_continuar:

    # recebendo dados da roleta e mesclando look
    roleta = str(input()).replace('<', ' esquerda').replace('>', ' direita').split(' ')
    print('Iniciando mesclagem...')

    if roleta[1] == 'esquerda':
        opcao_escolhida_penteado = penteado[(idx_opcao_meio_penteado - int(roleta[0])) % len(penteado)]
    else:
        opcao_escolhida_penteado = penteado[(idx_opcao_meio_penteado + int(roleta[0])) % len(penteado)]

    if roleta[3] == 'esquerda':
        opcao_escolhida_top = top[(idx_opcao_meio_top - int(roleta[2])) % len(top)]
    else:
        opcao_escolhida_top = top[(idx_opcao_meio_top + int(roleta[2])) % len(top)]

    if roleta[5] == 'esquerda':
        opcao_escolhida_bottom = bottom[(idx_opcao_meio_bottom - int(roleta[4])) % len(bottom)]
    else:
        opcao_escolhida_bottom = bottom[(idx_opcao_meio_bottom + int(roleta[4])) % len(bottom)]

    if roleta[7] == 'esquerda':
        opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos - int(roleta[6])) % len(sapatos)]
    else:
        opcao_escolhida_sapatos = sapatos[(idx_opcao_meio_sapatos + int(roleta[6])) % len(sapatos)]

    # imprimindo o look gerado
    print('O look gerado foi:')
    print(f'cabelo {opcao_escolhida_penteado}, {opcao_escolhida_top} com {opcao_escolhida_bottom}'
          f' e {opcao_escolhida_sapatos} nos pés.')

    # recebendo a opinião da Barbie
    decisao_barbie = str(input())

    # caso ela tenha gostado
    if decisao_barbie == decisao_1:

        # caso ela esteja usando a camisa da seleção
        if opcao_escolhida_top == 'camisa da seleção':
            print('Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!')
        else:
            print('Essa Barbie vai arrasar com o look perfeito!')

        barbie_continuar = False

    # caso ela tenha achado que não combinou
    if decisao_barbie == decisao_2:

        # redefinindo o "meio" de cada seção
        opcao_meio_penteado = opcao_escolhida_penteado
        idx_opcao_meio_penteado = penteado.index(opcao_meio_penteado)

        opcao_meio_top = opcao_escolhida_top
        idx_opcao_meio_top = top.index(opcao_meio_top)

        opcao_meio_bottom = opcao_escolhida_bottom
        idx_opcao_meio_bottom = bottom.index(opcao_meio_bottom)

        opcao_meio_sapatos = opcao_escolhida_sapatos
        idx_opcao_meio_sapatos = sapatos.index(opcao_meio_sapatos)

    # caso ela tenha desistido de usar o Armário
    if decisao_barbie == decisao_3:
        print('Acho que estou precisando de ajustes, Ken :(')
        barbie_continuar = False
