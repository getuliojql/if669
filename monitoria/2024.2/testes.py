receber_entradas = True
vilões = []

while receber_entradas:
    entrada = input()

    if entrada == 'Novo vilão - Muito Perigoso':
        vilão = input()
        vilões = [vilão] + vilões
    elif entrada == 'Novo vilão - Meio perigoso':
        vilão = input()
        vilões = vilões + [vilão]
    elif entrada == 'O que ele está fazendo aqui?':
        vilão_a_remover = input()
        for vilão in vilões:
            if vilão == vilão_a_remover:
                vilões.remove(vilão)
    elif entrada == 'Vilão mais perigoso do que pensávamos':
        indice_atual = int(input())
        indice_novo = int(input())
        vilão_antigo = str()
        vilão_antigo = vilões[indice_novo]
        vilões[indice_novo] = vilões[indice_atual]
        vilões[indice_atual] = vilão_antigo
    elif entrada == 'Que estranho, esses dois vilões… troque-os de lugar':
        vilão_1 = input()
        vilão_2 = input()
        index_vilão_1 = vilões.index(vilão_1)
        index_vilão_2 = vilões.index(vilão_2)
        vilões[index_vilão_1] = vilão_2
        vilões[index_vilão_2] = vilão_1
    elif entrada == 'Essa posição não está de acordo, ele nem odeia carecas':
        vilão_a_mover = input()
        for vilão in vilões:
            if vilão == vilão_a_mover:
                vilões.remove(vilão)
        vilões = vilões + [vilão_a_mover]
    elif entrada == 'Como a lista está ficando?':
        for vilão in vilões:
            if vilão == vilões[-1]:
                print(vilão, end='')
            else:
                print(vilão + ', ', end='')
    elif entrada == 'Já temos nossa lista de vilões':
        receber_entradas = False

print('O resultado final ficou assim:')

for vilão in vilões:
    if vilão == vilões[-1]:
        print(vilão, end='')
    else:
        print(vilão + ', ', end='')