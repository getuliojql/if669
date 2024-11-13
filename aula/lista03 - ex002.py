itens_faltantes = 0
indice_item = 1

itens_levar = str(input()).split(', ')
itens_totais = str(input()).split(', ')

for item in itens_levar:
    if item in itens_totais:
        if indice_item == 1:
            print('Esses são os itens que já tenho em casa:')
            print(f'{indice_item}º item: {item}')
            indice_item += 1
        else:
            print(f'{indice_item}º item: {item}')
            indice_item += 1
    else:
        itens_faltantes += 1
if itens_faltantes == len(itens_levar):
    print(f'Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {len(itens_levar)} itens em casa.')
elif itens_faltantes != 0:
    print(f'Irei precisar comprar {itens_faltantes} itens antes do meu encontro!')
else:
    print(f'Que ótimo, consegui encontrar cada um dos {len(itens_levar)} itens!')
print('Isso é tudo! Hora de me preparar!')