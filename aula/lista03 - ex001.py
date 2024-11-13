#variaveis iniciais
criaturas = []
qtd_criaturas = int(input())

#lendo novas criaturas e checando se já existem na lista
for c in range(qtd_criaturas):
    nova_criatura = str(input())

    if nova_criatura in criaturas:
        print('Criatura repetida')
    else:
        criaturas.append(nova_criatura)

#imprimindo a lista de criaturas
print('Registradas:')
for criatura in criaturas:
    print(criatura)