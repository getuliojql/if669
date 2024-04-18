velocidade_maxima_curva = int(input('velocidade: '))
tempo = str(input('tempo: '))

if velocidade_maxima_curva <= 260:
    print('mônaco')

elif 260 < velocidade_maxima_curva <= 285:
    if tempo == 'neblina':
        print('mônaco')
    else:
        print('ímola')

else:
    if tempo == 'neblina':
        print('ímola')
    else:
        print('spa-francorchamps')
