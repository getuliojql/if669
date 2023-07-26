from math import floor


def decodificar(cadeia):
    tres = True
    vogais = consoantes = primeiro_natural = liberado = 0

    for idx_caractere, caractere in enumerate(cadeia):
        if caractere.isalpha():
            if caractere.lower() in 'aeiou':
                vogais += 1
            else:
                consoantes += 1

        if caractere.isnumeric():
            if liberado == 0:
                if idx_caractere < len(cadeia) - 1 or idx_caractere < len(cadeia) - 2:
                    if idx_caractere < len(cadeia) - 2:
                        if cadeia[idx_caractere + 1].isnumeric() and cadeia[idx_caractere + 2].isnumeric():
                            caractere = (int(caractere) * 100) + (int(cadeia[idx_caractere + 1]) * 10) + \
                                        int(cadeia[idx_caractere + 2])
                            liberado = 2

                    if liberado < 2:
                        if cadeia[idx_caractere + 1].isnumeric():
                            caractere = (int(caractere) * 10) + int(cadeia[idx_caractere + 1])
                            liberado = 1

                if primeiro_natural == 0:
                    primeiro_natural = int(caractere)

                else:
                    if int(caractere) % primeiro_natural != 0:
                        tres = False
            else:
                liberado -= 1

    if tres and primeiro_natural != 0:
        return 3

    else:
        if consoantes == 0:
            return 0
        else:
            return (floor(vogais / consoantes)) % 7


# recebendo as entradas e armazenando-as já decodificadas
coordenada_x = decodificar(str(input()))
coordenada_y = decodificar(str(input()))

# construindo a matriz
matriz = []

for c in range(7):
    matriz.append([])

    for i in range(7):
        matriz[c].append('.')

matriz[coordenada_x].pop(coordenada_y)
matriz[coordenada_x].insert(coordenada_y, '☆')

# imprimindo a "foto"
for linha in matriz:
    for idx_coluna, coluna in enumerate(linha):
        if idx_coluna == len(linha) - 1:
            print(coluna)
        else:
            print(coluna, end=' ')

# imprimindo frases com base na posição da estrela
if coordenada_x == coordenada_y == 3:
    print('Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!')

elif coordenada_x == 0 or coordenada_x == 6 or coordenada_y == 0 or coordenada_y == 6:
    print('Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente '
          'demora um pouco para criar outro código...')

else:
    print('Ok, agora é só enviar a matriz!')

# imprimindo as "considerações finais"
if coordenada_x == 0 or coordenada_x == 6 or coordenada_y == 0 or coordenada_y == 6:
    print('Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.')

else:
    print('Obrigado pela ajuda! A foto ficou ótima!')
