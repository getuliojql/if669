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