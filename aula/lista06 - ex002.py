# definindo função que cria um dicionário para o famoso informado
def registrar(pessoa):
    registro = {'nome': pessoa[0], 'nota': pessoa[1], 'categoria': pessoa[2]}

    return registro


# definindo função que imprime os dados - em ordem de nota- dos famosos de cada categoria
def ordenar(lista):
    notas = []
    controle = 0

    for tupla in lista:
        notas.append(int(tupla[1]))

    notas.sort(reverse=True)

    while controle < len(lista):
        for tupla in lista:
            if len(notas) > 0:
                if int(tupla[1]) == notas[0]:
                    print(' - '.join(tupla))

                    notas.pop(0)
                    controle += 1


# criando listas que irão armazenar os dados dos famosos
nattys = []
fake_nattys = []
registro_geral = []

# adicionando os dados dos famosos a uma lista geral
for i in range(int(input())):
    registro_geral.append(registrar(str(input()).split(' - ')))

# dividindo-os por categoria
for dicionario in registro_geral:
    if dicionario['categoria'] == 'natty':
        nattys.append(tuple(dicionario.values()))

    else:
        fake_nattys.append(tuple(dicionario.values()))

# imprimindo os dados dos famosos, em ordem decrescente de nota e separados por categoria
ordenar(nattys)
ordenar(fake_nattys)
