def pontuar(avaliacao):
    nota = 0
    desordem_local = 0

    if avaliacao == 'boa':
        nota = 2

    elif avaliacao == 'média':
        nota = 1

    elif avaliacao == 'ruim':
        nota = -3

    else:
        frase_aleatoria = ''

        while frase_aleatoria != 'ORDEM':
            frase_aleatoria = str(input())

            if frase_aleatoria != 'ORDEM':
                desordem_local += 1

    return nota, desordem_local


desordem_kanye = 0
vitorias_kanye = 0

desordem_taylor = 0
vitorias_taylor = 0

perdedor = ''
desordem = False

numero_rodadas = int(input())

for rodada in range(numero_rodadas):
    if vitorias_kanye < 3 and vitorias_taylor < 3 and not desordem:
        print(f'{rodada + 1}° RODADA:')

        pontuacao_kanye = 0
        pontuacao_taylor = 0

        if not desordem:
            musica_kanye = str(input())

            for _ in range(3):
                avaliacao_kanye = str(input())
                pontuacao_atual_kanye, desordem_atual_kanye = pontuar(avaliacao_kanye)
                pontuacao_kanye += pontuacao_atual_kanye
                desordem_kanye += desordem_atual_kanye

            if desordem_kanye >= 5 and perdedor == '':
                perdedor = 'Kanye West'
                desordem = True

        if not desordem:
            musica_taylor = str(input())
            for _ in range(3):
                avaliacao_taylor = str(input())
                pontuacao_atual_taylor, desordem_atual_taylor = pontuar(avaliacao_taylor)
                pontuacao_taylor += pontuacao_atual_taylor
                desordem_taylor += desordem_atual_taylor

            if desordem_taylor >= 5 and perdedor == '':
                perdedor = 'Taylor Swift'
                desordem = True

        if not desordem:
            if pontuacao_kanye > pontuacao_taylor:
                vitorias_kanye += 1
                vencedor_rodada = 'Kanye West'
                print(f'O(a) vencedor(a) da {rodada + 1}° rodada foi Kanye West')

            elif pontuacao_taylor > pontuacao_kanye:
                vitorias_taylor += 1
                vencedor_rodada = 'Taylor Swift'
                print(f'O(a) vencedor(a) da {rodada + 1}° rodada foi Taylor Swift')

            else:
                print(f'Não houve vencedor na {rodada + 1}° rodada')

if desordem:
    if perdedor == 'Kanye West':
        print(f'Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!\nO(a) vencedor(a) do Cin '
              f'Awards é Taylor Swift, parabéns!')

    else:
        print(f'Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!\nO(a) vencedor(a) do Cin '
              f'Awards é Kanye West, parabéns!')

else:
    if vitorias_kanye > vitorias_taylor:
        print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitorias_kanye} vitórias, é Kanye West, parabéns!')

    elif vitorias_taylor > vitorias_kanye:
        print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitorias_taylor} vitórias, é Taylor Swift, parabéns!')

    else:
        print('Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!')
