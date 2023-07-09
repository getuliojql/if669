# recebendo as variáveis iniciais e convertendo-as para inteiros
lista_inicial = str(input()).split(' ; ')
maximo_objetos = int(lista_inicial[0])
maximo_custo = int(lista_inicial[1])

# variáveis de apoio
controle = 0
objetos_atuais = []
custo_atual = 0
custo = 0
historico = []
contagem_objetos = 0

# possíveis frases
adicionar = 'Quero adicionar um item'
remover = 'Quero remover um item'
lembrar = 'Poderia me lembrar os itens que estão até então e de qual filme eles foram recuperados?'
fim = 'Fim! Muito obrigada pela ajuda!!'

# início do laço responsável por checar qual frase será recebida
while controle == 0:
    frase = str(input())
    # primeiro caso da frase
    if frase == adicionar:
        lista_adicionar = str(input()).replace(' - ', ' , ').split(' , ')

        objeto_magico = lista_adicionar[0]
        filme = lista_adicionar[1]
        custo = int(lista_adicionar[2])

        # caso seja possível adicionar
        if contagem_objetos < maximo_objetos and (custo_atual + custo) < maximo_custo:
            historico.append(objeto_magico)

            historico.append(filme)

            historico.append(custo)
            custo_atual += custo

            objetos_atuais.append(objeto_magico)
            objetos_atuais.append(filme)
            ' - '.join(objetos_atuais)

            print(f'Vá em frente, Ken! Você ainda tem {maximo_custo - custo_atual} barbieCoins disponíveis')
            contagem_objetos += 1

        # caso não seja
        else:
            print('Avise a Barbie que isso não será possível.')

    # segundo caso da frase
    elif frase == remover:
        objeto_remover = str(input())

        # caso o item exista na lista
        if objeto_remover in objetos_atuais:
            objetos_atuais.pop(objetos_atuais.index(objeto_remover) + 1)

            custo_objeto_remover = historico[historico.index(objeto_remover) + 2]

            objetos_atuais.remove(objeto_remover)

            custo_atual -= custo_objeto_remover

            print('Ok, Barbie!')
            print(f'Ken, você ainda tem {maximo_custo - custo_atual} barbieCoins disponíveis')
            contagem_objetos -= 1

        # caso não exista
        else:
            print('Barbie, infelizmente não consegui fazer isso.')

    # terceiro caso da frase
    elif frase == lembrar:

        # imprimindo a lista, caso haja itens dentro
        if len(objetos_atuais) > 0:
            print('Claro!')

            for idx_objeto, objeto in enumerate(objetos_atuais):
                if idx_objeto % 2 == 0:
                    print(f'{objetos_atuais[idx_objeto]} - {objetos_atuais[idx_objeto + 1]}')

        # caso não haja
        else:
            print('Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!')

    # quarto caso da frase, resultando no término do programa
    elif frase == fim:
        print('Por nada! Estou sempre à disposição!')
        controle = 1
