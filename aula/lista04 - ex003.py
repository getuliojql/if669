def identificador_de_palindromos(verificacao):
    is_palindromo = True

    for idx_c, c in enumerate(verificacao):
        if verificacao[idx_c] != verificacao[(-1) - idx_c] and is_palindromo:
            is_palindromo = False

    if is_palindromo:
        return True
    else:
        return False


def contador_de_diferencas(cadeia):
    conjunto = []

    for c in cadeia:
        if c not in conjunto:
            conjunto.append(c)

    return len(conjunto)


qtd_entradas = int(input())

for i in range(qtd_entradas):
    entrada = str(input())
    frase_ou_numero = entrada.lower().replace(' ', '')

    numero = False

    for caractere in frase_ou_numero:
        if caractere in '1234567890':
            numero = True

    palindromo = identificador_de_palindromos(frase_ou_numero)
    distintos = contador_de_diferencas(frase_ou_numero)

    if numero and palindromo:
        print(f'O número "{int(frase_ou_numero)}" é um palíndromo!')
        print(f'Há {distintos} número(s) distinto(s) na sequência de números.')

    elif not numero and palindromo:
        print(f'A frase "{entrada}" é um palíndromo!')
        print(f'Há {distintos} letra(s) distinta(s) na frase.')

    else:
        print('A frase ou o número não é um palíndromo.')
