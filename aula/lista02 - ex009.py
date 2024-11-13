from math import floor

duracao_playlist = int(input())

meta_diaria = 10
animacao_diaria = 0
nome_maxima = ''
animacao_maxima = 0

for c in range(1, 4):
    print(f'Dia {c} do InterCIn')
    numero_musicas = int(input())

    for c in range(0, numero_musicas):
        nome_musica = str(input())
        duracao_musica = int(input())
        animacao_musica = int(input())
        animacao_diaria += floor((0.8 * animacao_musica))

        if animacao_musica > animacao_maxima:
            nome_maxima = nome_musica
            animacao_maxima = animacao_musica

    print(f'A música mais animada do dia foi {nome_maxima}')

###### ESSA É MINHA QUESTÃO OPCIONAL, LOGO, NÃO FAREI-A ########

# metadiaria = 10
# cadamusica -> animacao += 80%musica (arredondado para baixo)