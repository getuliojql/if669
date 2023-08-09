def fibonacci(numero):
    if numero == 0:
        return 0

    elif numero == 1 or numero == 2:
        return 1

    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


entrada = str(input()).split(' ')

vidas = int(entrada[0])
casas = int(entrada[1])

while vidas > 0 and casas > 0:
    valor = 0
    contem = False
    tentativa = int(input())

    while fibonacci(valor) <= tentativa and not contem:
        if tentativa == fibonacci(valor):
            contem = True

        else:
            valor += 1

    if contem:
        casas -= 1

    else:
        vidas -= 1
        casas = int(entrada[1])
        print('Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!')

if casas == 0:
    print('Voce Adicionou A Master Sword ao seu inventario')
    print('Link Salve Hyrule!!!')

else:
    print('A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf')
