# determinando algumas variáveis
controle = 0
numero_arara = 0
profissoes_faltantes = []
numero_profissoes_faltantes = 0

#início do programa
while controle == 0:
    oq_fazer = str(input())

    # saindo do programa se a barbie não quiser explorar uma nova arara
    if oq_fazer == 'Meninas, acho que já falei demais. Vamos para o shopping?':
        controle = 1

    # recebendo as variáveis, caso ela queira
    elif oq_fazer == 'Explorar arara':
        print(f'Arara {numero_arara}:')
        numero_arara += 1
        conteudo_arara = str(input()).split(', ')
        profissoes_falar = str(input()).split(', ')

        # checando se as listas contém o mesmo número de profissões
        if len(conteudo_arara) != len(profissoes_falar):
            print('Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!')

        # checando se as listas são iguais
        elif sorted(conteudo_arara) == sorted(profissoes_falar):
            print('Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!')

        # se nennhum dos casos acima for verdade, vendo quais profissões vão faltar
        elif len(conteudo_arara) == len(profissoes_falar):

            for palavra in conteudo_arara:
                if profissoes_falar.count(palavra) == 0:
                    profissoes_faltantes.append(palavra)
                    numero_profissoes_faltantes += 1

            # imprimindo as profissões faltantes
            print(f'Poxa, Barbie! Você acabou desorganizando essa arara, e {numero_profissoes_faltantes} profissões vão'
                  f' ficar de fora da conversa. São elas: ', end='')
            for profissao in profissoes_faltantes:
                if profissao == profissoes_faltantes[-1]:
                    print(f'{profissao}.')
                else:
                    print(f'{profissao}, ', end='')
    profissoes_faltantes.clear()
    numero_profissoes_faltantes = 0
