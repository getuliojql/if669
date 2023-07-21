def soma(a, b):
    resultado = a + b
    return resultado


def subtracao(a, b):
    resultado = a - b
    return resultado


def produto(a, b):
    resultado = a * b
    return resultado


def divisao(a, b):
    resultado = a / b
    return resultado


def potenciacao(a, b):
    resultado = a ** b
    return resultado


qtd_operacoes = int(input())
numero_final = 0

frase_soma = 'Quero somar esses dois números:'
frase_subtracao = 'Preciso subtrair um pelo outro'
frase_produto = 'Quanto dá o produto disso?'
frase_divisao = 'Vou dividir aqui rapidinho'
frase_potenciacao = 'E se eu elevar um pelo outro?'

if qtd_operacoes != 0:
    for i in range(qtd_operacoes):
        frase_operacao = str(input())
        numero_a = float(input())
        numero_b = float(input())

        if frase_operacao == frase_soma:
            numero_final = soma(numero_a, numero_b)

        elif frase_operacao == frase_subtracao:
            numero_final = subtracao(numero_a, numero_b)

        elif frase_operacao == frase_produto:
            numero_final = produto(numero_a, numero_b)

        elif frase_operacao == frase_divisao:
            numero_final = divisao(numero_a, numero_b)

        elif frase_operacao == frase_potenciacao:
            numero_final = potenciacao(numero_a, numero_b)

        print(f'O resultado da {i + 1}ª operação foi {numero_final:.1f}')

    print('Ufa, já deu de cálculos por hoje!')

else:
    print('Vou relaxar aqui na minha nave')
