velocidade_maxima = int(input())
tempo = str(input())

if velocidade_maxima <= 260:
    print('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')

elif 260 < velocidade_maxima <= 285:
    if tempo == 'neblina':
        print('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')
    else:
        print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')

else:
    if tempo == 'neblina':
        print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
    else:
        print('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
