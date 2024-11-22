# artistas
tay = "Taylor Swift"
ye = "Kanye West"

# booleana
descontentamento = False
avaliacao = True
taylor = True
tudo = True

# pontuação
pontoskanye = 0
pontostaylor = 0
pontuacaodesordem = 0
totaltaylor = 0
totallkanye = 0

num_rodadas = int(input())
# input das musicas e das avaliaçôes

for rodada in range(1, num_rodadas + 1, 1):
    print(f"{rodada}° RODADA:")

    musica_kanye = input()
    avaliacao_kanye1 = input()
    if avaliacao_kanye1 == "boa":
        pontoskanye += 2
    elif avaliacao_kanye1 == "média":
        pontoskanye += 1
    elif avaliacao_kanye1 == "ruim":
        pontoskanye -= 3
    elif avaliacao_kanye1 == "péssima":
        # desordem
        descontentamento = True
        while descontentamento == True:
            random_frases = input()
            pontuacaodesordem += 1

            if random_frases == 'ORDEM':
                descontentamento = False
                continue
            if pontuacaodesordem == 5:
                print(f'Os fãs do(a) {ye} causaram tanta desordem que ele(a) perdeu o prêmio!')
                print(f'O(a) vencedor(a) do Cin Awards é {tay}, parabéns!')
                descontentamento = False
                taylor = False
            continue

    avaliacao_kanye2 = input()
    if avaliacao_kanye2 == "boa":
        pontoskanye += 2
    elif avaliacao_kanye2 == "média":
        pontoskanye += 1
    elif avaliacao_kanye2 == "ruim":
        pontoskanye -= 3
    elif avaliacao_kanye2 == "péssima":
        # desordem
        descontentamento = True
        while descontentamento == True:
            random_frases = input()
            pontuacaodesordem += 1

            if random_frases == 'ORDEM':
                descontentamento = False
            if pontuacaodesordem == 5:
                print(f'Os fãs do(a) {ye} causaram tanta desordem que ele(a) perdeu o prêmio!')
                print(f'O(a) vencedor(a) do Cin Awards é {tay}, parabéns!')
                descontentamento = False
                taylor = False
            continue

    avaliacao_kanye3 = input()
    if avaliacao_kanye3 == "boa":
        pontoskanye += 2
    elif avaliacao_kanye3 == "média":
        pontoskanye += 1
    elif avaliacao_kanye3 == "ruim":
        pontoskanye -= 3
    elif avaliacao_kanye3 == "péssima":
        # desordem
        descontentamento = True
        while descontentamento == True:
            random_frases = input()
            pontuacaodesordem += 1

            if random_frases == 'ORDEM':
                descontentamento = False
            if pontuacaodesordem == 5:
                print(f'Os fãs do(a) {ye} causaram tanta desordem que ele(a) perdeu o prêmio!')
                print(f'O(a) vencedor(a) do Cin Awards é {tay}, parabéns!')
                descontentamento = False
                taylor = False
            continue

    while taylor == True:
        musica_taylor = input()
        avaliacao_taylor1 = input()
        if avaliacao_taylor1 == "boa":
            pontostaylor += 2
        elif avaliacao_taylor1 == "média":
            pontostaylor += 1
        elif avaliacao_taylor1 == "ruim":
            pontostaylor -= 3
        elif avaliacao_taylor1 == "péssima":
            # desordem
            descontentamento = True
            while descontentamento == True:
                random_frases = input()
                pontuacaodesordem += 1

                if random_frases == 'ORDEM':
                    descontentamento = False
                if pontuacaodesordem == 5:
                    print(f'Os fãs do(a) {tay} causaram tanta desordem que ele(a) perdeu o prêmio!')
                    print(f'O(a) vencedor(a) do Cin Awards é {ye}, parabéns!')
                    descontentamento = False
                continue
        avaliacao_taylor2 = input()
        if avaliacao_taylor2 == "boa":
            pontostaylor += 2
        elif avaliacao_taylor2 == "média":
            pontostaylor += 1
        elif avaliacao_taylor2 == "ruim":
            pontostaylor -= 3
        elif avaliacao_taylor2 == "péssima":
            # desordem
            descontentamento = True
            while descontentamento:
                random_frases = input()
                pontuacaodesordem += 1

                if random_frases == 'ORDEM':
                    descontentamento = False
                if pontuacaodesordem == 5:
                    print(f'Os fãs do(a) {tay} causaram tanta desordem que ele(a) perdeu o prêmio!')
                    print(f'O(a) vencedor(a) do Cin Awards é {ye}, parabéns!')
                    descontentamento = False
                continue
        avaliacao_taylor3 = input()
        taylor = False
        if avaliacao_taylor3 == "boa":
            pontostaylor += 2
        elif avaliacao_taylor3 == "média":
            pontostaylor += 1
        elif avaliacao_taylor3 == "ruim":
            pontostaylor -= 3
        elif avaliacao_taylor3 == "péssima":
            # desordem
            descontentamento = True
            while descontentamento:
                random_frases = input()
                pontuacaodesordem += 1

                if random_frases == 'ORDEM':
                    descontentamento = False
                if pontuacaodesordem == 5:
                    print(f'Os fãs do(a) {tay} causaram tanta desordem que ele(a) perdeu o prêmio!')
                    print(f'O(a) vencedor(a) do Cin Awards é {ye}, parabéns!')
                    descontentamento = False
                continue
        # pontuação total da rodada
        if pontoskanye > pontostaylor:
            print(f'O(a) vencedor(a) da {rodada}° rodada foi {ye}')
            totallkanye += 1
        elif pontostaylor > pontoskanye:
            print(f'O(a) vencedor(a) da {rodada}° rodada foi {tay}')
            totaltaylor += 1
        elif pontoskanye == pontostaylor:
            print(f"Não houve vencedor na {rodada}° rodada")
