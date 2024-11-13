#1
'''
produtos_vendidos = ['cpu', 'gpu', 'fonte', 'cooler']
produtos_estoque = ['cpu', 'cpu', 'cpu', 'gpu', 'gpu', 'fonte', 'fonte', 'fonte', 'fonte']

produto_consultado = str(input('Digite o produto que deseja consultar: '))
estoque_consultado = 0

vendido = False

for produto in produtos_vendidos:
    if produto_consultado == produto:
        vendido = True

if vendido:
    for produto in produtos_estoque:
        if produto_consultado == produto:
            estoque_consultado += 1
    if estoque_consultado > 0:
        print(f'Nossa loja vende {produto_consultado} sim! Atualmente temos {estoque_consultado} {produto_consultado}(s) em loja...')
    else:
        print(f'Nossa loja vende {produto_consultado} sim! Mas infelizmente não temos {produto_consultado} no nosso estoque atualmente :(')
else:
    print(f'Infelizmente nós não vendemos {produto_consultado} :(')
'''

#2
'''
produtos_vendidos = ['cpu', 'gpu', 'fonte', 'cooler']
produtos_estoque = ['cpu', 'cpu', 'cpu', 'gpu', 'gpu', 'fonte', 'fonte', 'fonte', 'fonte']
quantidade = 0

for produto in produtos_vendidos:
    for estoque in produtos_estoque:
        if estoque == produto:
            quantidade +=1
    print(f'Existem {quantidade} {produto}(s) em estoque!')
    quantidade = 0
'''

#3
'''
numeros = [8, 3, 9, 1, 2, 3]
metade_numeros = int(len(numeros) / 2)
primeira_metade = numeros[:metade_numeros]
segunda_metade = numeros[metade_numeros:]
numeros_soma = list()

for chave, numero in enumerate(primeira_metade):
    for chave_2, numero_2 in enumerate(segunda_metade):
        if chave == chave_2:
            numeros_soma.append(numero + numero_2)
print(f'Lista principal: {numeros}')
print(f'Primeira metade: {primeira_metade}')
print(f'Segunda metade: {segunda_metade}')
print(f'Lista soma: {numeros_soma}')
'''

#4
texto = 'O comando for & o t*pico de estudo deste projeto. Ele & #til para iterar sobre objetos iter@veis. Muitos problemas podem ser resolvidos com o aux!lio do comando for.'
'''for letra in '@&!*#':
    if letra == '@':
        texto = texto.replace('@', 'á')
    elif letra == '&':
        texto = texto.replace('&', 'é')
    elif letra == '!':
        texto = texto.replace('!', 'í')
    elif letra == '*':
        texto = texto.replace('*', 'ó')
    elif letra == '#':
        texto = texto.replace('#', 'ú')'''
texto = texto.replace('@', 'á')
texto = texto.replace('&', 'é')
texto = texto.replace('!', 'í')
texto = texto.replace('*', 'ó')
texto = texto.replace('#', 'ú')
print(texto)