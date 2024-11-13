def converter(equacao):
    pilha = []
    resultado = 0

    for valor in equacao:
        if valor.isnumeric():
            pilha.append(int(valor))

        else:
            if valor == '+':
                resultado = pilha[-2] + pilha[-1]

            elif valor == '-':
                resultado = pilha[-2] - pilha[-1]

            elif valor == '*':
                resultado = pilha[-2] * pilha[-1]

            elif valor == '/':
                resultado = pilha[-2] / pilha[-1]

            pilha.pop(-1)
            pilha.insert(-1, resultado)
            pilha.pop(-1)

    return int(resultado)


def numero_perfeito(valor):
    divisores = 0

    for i in range(valor - 1, 0, -1):
        if valor % i == 0:
            divisores += i

    if divisores == valor and valor != 0:
        return 1
    else:
        return 0


numero = 1
palavra = ''
conjunto = []
acabou = False

while not acabou:
    entrada = str(input())

    if entrada == 'Todas as expressoes foram enviadas!':
        acabou = True

    elif entrada == '':
        binario = ''

        print(f'O {numero}º conjunto de expressoes resultou no binario ', end='')

        for n in conjunto:
            print(n, end='')
            binario += str(n)

        letra = chr(int(binario, 2))
        palavra += letra

        print(f' que em ASCII eh: {letra}\n')

        numero += 1
        conjunto.clear()

    else:
        linha = entrada.split(' ')
        conjunto.append(numero_perfeito(converter(linha)))

print(f'A decodificacao final resultou em:\n{palavra}')
