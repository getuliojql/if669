contador = musica = tentativas = 0
print('PLAYLIST DO PAPAI NOEL')

while musica != 'FIM' and tentativas < 3:
    musica = input()

    if musica != 'FIM':
        entrada = musica.replace(' ', '')

        if len(entrada) >= 15 and entrada.isalpha():
            contador += 1
            ultima_musica = musica
            print(f'{musica} foi adicionada à playlist!')

        elif entrada.isnumeric():
            contador = 0
            tentativas += 1

            if tentativas < 3:
                print('ABORTAR! OS VILÕES OBTIVERAM ACESSO, TEREMOS QUE RECOMEÇAR.\nPLAYLIST DO PAPAI NOEL')

        else:
            print(f'{musica} não pôde ser adicionada à playlist! A última música adicionada foi {ultima_musica}.')

if tentativas == 3:
    print('NAAÃO! Já está na hora do Papai Noel sair e não conseguimos construir sua playlist perfeita.')

else:
    print(f'Ufa! Conseguimos criar a playlist perfeita, tomara que o Papai Noel goste das {contador} músicas.')
