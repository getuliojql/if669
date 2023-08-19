


























'''# função que cria o dicionário de dado famoso
def registrar_famoso():
    famoso = {}
    informacoes = str(input())

    famoso['nome'] = informacoes[0:informacoes.index('-')].rstrip()

    informacoes = informacoes[informacoes.index('-') + 2:].split(' ')

    famoso['profissao'] = informacoes[0]
    famoso['avaliacao'] = informacoes[1]
    famoso['mes'] = int(informacoes[2])

    return famoso


# definindo a lista que irá conter todos os famosos e recebendo quantos serão
registro_geral = []
qtd_famosos = int(input())

# somando os dicionários de cada um à lista geral
for f in range(qtd_famosos):
    registro_geral.append(registrar_famoso())

# definindo listas para ajudar na hora de imprimir as informações dos fake nattys
fake_nattys = []
fake_nattys_profissoes = []
consulta_mes = int(input())

# indo de dicionário em dicionário, checando se o famoso cumpre os requisitos de "fake natty do mês" e registrando-o
for registro in registro_geral:
    if registro['mes'] == consulta_mes and registro['avaliacao'] == 'fake':
        fake_nattys.append(registro['nome'])
        fake_nattys_profissoes.append(registro['profissao'])

# caso existam fake nattys a serem expostos
if len(fake_nattys) > 0:
    print('Os fake nattys do mês são:')

    # organizando-os por ordem alfabética
    for nome in sorted(fake_nattys):
        print(f'{nome} - {fake_nattys_profissoes[fake_nattys.index(nome)]}')

# caso não existam
else:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
# CRIAR UMA LISTA AO INVES DE UM DICIONARIO
'''