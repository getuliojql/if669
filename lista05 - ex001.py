def preco(cadeia):
    minusculas = maiusculas = 0

    for caractere in str(cadeia):
        if caractere == caractere.lower():
            minusculas += 1

        else:
            maiusculas += 1

    if minusculas == maiusculas:
        return len(cadeia) ** 2

    elif minusculas > maiusculas:
        return fatorial(minusculas) * len(cadeia)

    else:
        return fatorial(maiusculas) * len(cadeia)


def fatorial(numero):
    if numero == 0:
        return 1

    else:
        return numero * fatorial(numero - 1)


grunhido = str(input())

if preco(grunhido) >= 100:
    print(f'Hum... {preco(grunhido)}? Acho que na volta eu compro')

else:
    print(f'{preco(grunhido)}! Vou comprar todos!')
