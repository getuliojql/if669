# variaveis iniciais
qtd_colecoes = int(input())

# recebendo as colecoes e suas notas
for num_colecao in range(qtd_colecoes):
    nova_colecao = str(input()).split(', ')
    nota_colecao = str(input()).split(', ')

    # mais algumas variaveis
    media_nota = 0
    controle_peca = True

    # checando se está apta
    while controle_peca:

        #laço para parar de percorrer imediatamente se algo estiver errado
        while True:

            # vendo se contém alguma das peças proibidas
            for peca in nova_colecao:
                if peca == 'colete preto' or peca == 'coturno' or peca == 'vestido com babados' or peca == 'blusa bufante':
                    if peca == 'colete preto' or peca == 'coturno':
                        print(f'{peca} é uma peça muito gótica, não faz o estilo da Glimmer.')
                        controle_peca = False

                    elif peca == 'vestido com babados' or peca == 'blusa bufante':
                        print(f'{peca} é uma peça muito antiquada, infelizmente essa coleção não vai servir...')
                        controle_peca = False
                    break
            break

        # calculando a média
        if controle_peca:
            for nota in nota_colecao:
                media_nota += int(nota)
            media_nota /= int(len(nota_colecao))

            # vendo se a média é menor que 6
            if media_nota < 6:
                print('Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.')
                controle_peca = False

        # se nada estiver errado
        if controle_peca:
            print('Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.')
            controle_peca = False
