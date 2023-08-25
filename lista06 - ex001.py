# definindo função que cria um dicionário para o famoso informado
def registrar(famoso):
    registro = {'nome': famoso[:famoso.index(' - ')]}

    famoso = famoso[famoso.index(' - ') + 3:].split(' ')

    registro['profissao'] = famoso[0]
    registro['avaliacao'] = famoso[1]
    registro['mes'] = int(famoso[2])

    return registro


# definindo função que verifica se o famoso informado já havia sido informado e atualiza suas informações
def verificar_repeticao(lista, novo_dicionario):
    for idx_dicionario, dicionario in enumerate(lista):
        if dicionario['nome'] == novo_dicionario['nome']:
            lista[idx_dicionario] = novo_dicionario

            return True

    return False


# criando lista que conterá os dicionários dos famosos
registro_geral = []

# recebendo os dados do famoso
for personalidade in range(int(input())):
    novo_registro = registrar(str(input()))

    # verificando se já existia; se já, atualizando suas informações, se não, adicionando-o à lista
    if not verificar_repeticao(registro_geral, novo_registro):
        registro_geral.append(novo_registro)

# criando listas para auxiliar na impressão dos "fake nattys" e recebendo mês desejado
fake_nattys = []
fake_nattys_profissoes = []
consulta_mes = int(input())

# registrando nome e profissão dos "fake nattys"
for individuo in registro_geral:
    if individuo['mes'] == consulta_mes and individuo['avaliacao'] == 'fake':
        fake_nattys.append(individuo['nome'])
        fake_nattys_profissoes.append(individuo['profissao'])

# caso existam, imprimindo uma lista dos "fake nattys"
if len(fake_nattys) > 0:
    print('Os fake nattys do mês são:')

    for nome in sorted(fake_nattys):
        print(f'{nome} - {fake_nattys_profissoes[fake_nattys.index(nome)]}')

# caso não existam, imprimindo mensagem de inexistência
else:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
