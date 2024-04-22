#inputs
vm = (int(input()))
tempo = (str(input()))

#resolução
if ((250 <= vm <= 260) and (tempo == 'ensolarado' or tempo == 'chuvoso')):
    print ('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')

elif ((261 <= vm <= 285) and (tempo == 'ensolarado' or tempo == 'chuvoso')):
    print ('Senna corria em Ímola, onde infelizmente fez sua última corrida.')

elif ((286 == vm <= 310) and (tempo == 'ensolarado' or tempo == 'chuvoso')):
    print ('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')

elif ((vm <= 260) and (tempo == 'neblina')):
    print ('Senna corria em Ímola, onde infelizmente fez sua última corrida.')

elif ((vm <= 285) and (tempo == 'neblina')):
    print ('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')