def formatar(entrada, lista):
    algarismos = entrada.replace('-', '').split(' : ')

    if int(algarismos[0]) == 0:
        variavel = f'{algarismos[1]}'
    elif int(algarismos[0]) == 1:
        variavel = f'{algarismos[1]}x'
    else:
        variavel = f'{algarismos[1]}x^{algarismos[0]}'

    lista.insert(int(algarismos[0]), variavel)
    lista.pop(int(algarismos[0]) + 1)


def derivar(expressao, ordem):
    if expressao.isnumeric():
        return 0

    else:
        if ordem == 0:
            return expressao

        else:
            if '^' not in expressao:
                if 'x' not in expressao:
                    return derivar(0, ordem - 1)

                else:
                    return derivar(expressao[:-1], ordem - 1)

            else:
                expressao = (f'{int(expressao[:expressao.find("x")]) * int(expressao[expressao.find("^") + 1:])}x^'
                             f'{int(expressao[expressao.find("^") + 1:]) - 1}')
                return derivar(expressao, ordem - 1)


grau_polinomio = int(input())
ordem_derivada = int(input())
coeficientes_nao_nulos = int(input())

grau_dos_monomios = [str(num) for num in range(grau_polinomio + 1)]

for i in range(coeficientes_nao_nulos):
    formatar(str(input())[15:], grau_dos_monomios)

derivacao = []
negativos = []

for idx_monomio, monomio in enumerate(grau_dos_monomios):
    if '-' in monomio:
        monomio.replace('-', '')
        negativos.append(idx_monomio)

    derivacao.append(derivar(monomio, ordem_derivada))

print(f'A derivada {ordem_derivada} do polinômio', end=' ')
for idx_monomio, monomio in enumerate(grau_dos_monomios):
    if idx_monomio == len(grau_dos_monomios) - 1:
        if idx_monomio in negativos:
            print(f'-{monomio} é')

        else:
            print(f'{monomio} é')

    else:
        if idx_monomio in negativos:
            print(f'-{monomio}', end=' ')

        else:
            print(monomio, end=' ')
