# definindo função responsável por somar
def soma(a, b):
    resultado = a + b
    return resultado


# definindo função responsável por subtrair
def subtracao(a, b):
    resultado = a - b
    return resultado


# definindo função responsável por multiplicar
def produto(a, b):
    resultado = a * b
    return resultado


# definindo função responsável por dividir
def divisao(a, b):
    resultado = a / b
    return resultado


# definindo função responsável por elevar(?)
def potenciacao(a, b):
    resultado = a ** b
    return resultado


# recebendo o número de operações a serem feitas e criando a variável do resultado
qtd_operacoes = int(input())
numero_final = 0

# definindo as frases que ocasionarão cada operação
frase_soma = 'Quero somar esses dois números:'
frase_subtracao = 'Preciso subtrair um pelo outro'
frase_produto = 'Quanto dá o produto disso?'
frase_divisao = 'Vou dividir aqui rapidinho'
frase_potenciacao = 'E se eu elevar um pelo outro?'

# se o usuário quiser realizar alguma operação
if qtd_operacoes != 0:

    # criando o laço de repetição e recebendo as entradas
    for i in range(qtd_operacoes):
        frase_operacao = str(input())
        numero_a = float(input())
        numero_b = float(input())

        # criando condicionais para cada operação e executando a respectiva função
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

        # imprimindo o resultado
        print(f'O resultado da {i + 1}ª operação foi {numero_final:.1f}')

    # quando todas as operações tiverem sido concluídas
    print('Ufa, já deu de cálculos por hoje!')

# se não quiser
else:
    print('Vou relaxar aqui na minha nave')
