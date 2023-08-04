def analisar(nome, baralho, culpado):
    global relogio
    idx_nome = idx_baralho = contador = 0

    if len(nome) == 0:
        return True

    elif contador < len(baralho):

        if nome[idx_nome] == baralho[idx_baralho]:
            relogio += 1
            contador += 1

            return analisar(nome[culpado:], baralho[culpado:], 1)

        else:
            while culpado > 0:
                culpado -= culpado
                return analisar(nome_suspeito.lower(), string_concatenada.lower()[relogio:], 0)

            relogio += 1
            contador += 1

            return analisar(nome_suspeito.lower(), baralho[contador:], 0)

    else:
        return False


relogio = -1

nome_suspeito = str(input())
string_concatenada = str(input())

if analisar(nome_suspeito.lower(), string_concatenada.lower(), 0):
    print(f'Encontrei, o culpado é o {nome_suspeito}!')

else:
    print(f'Não era o {nome_suspeito}, tenho que continuar procurando.')
