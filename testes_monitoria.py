# inputs

nome = input()
quantidade_de_musicas = int(input())
numero_maior_de_streams = 0
numero_menor_de_streams = 0

# comandos
if quantidade_de_musicas == 0:
    print(f'{nome} é team Taylor e não ouviu Kanye West')

elif quantidade_de_musicas == 1:
    musica = input()
    qs = int(input())

    print(f'A única música que {nome} ouviu foi {musica} com {qs} streams')

elif quantidade_de_musicas != 0 and not quantidade_de_musicas == 1:
    for qm in range(quantidade_de_musicas, 0, -1):
        musica = input()
        quantidade_de_streams = int(input())

        if quantidade_de_streams > numero_maior_de_streams:
            numero_maior_de_streams = quantidade_de_streams
            musica_mais_escutada = musica

        elif quantidade_de_streams < numero_menor_de_streams or numero_menor_de_streams == 0:
      # if quantidade_de_streams < numero_menor_de_streams or numero_menor_de_streams == 0:   [SOLUÇÃO]
            numero_menor_de_streams = quantidade_de_streams
            musica_menos_escutada = musica

    if numero_maior_de_streams > numero_menor_de_streams:
        print(
            f'A música que {nome} mais ouviu foi {musica_mais_escutada} com {numero_maior_de_streams} streams\nA música que {nome} menos ouviu foi {musica_menos_escutada} com {numero_menor_de_streams} streams')
    elif numero_menor_de_streams == quantidade_de_streams:

        print(f'A música que {nome} mais ouviu foi {musica_mais_escutada} com {numero_maior_de_streams} streams')
