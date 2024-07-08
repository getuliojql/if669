# uso das funcoes obrigatorias da questao
def calculo_dano(nivel_pokemon_aliado, poder_pokemon_aliado, defesa_pokemon_inimigo, poder_ataque_pokemon_aliado,
                 nivel_pokemon_inimigo, poder_pokemon_inimigo, defesa_pokemon_aliado, poder_ataque_pokemon_inimigo,
                 lista_efetividades):
    lista_danos = []
    dano_aliado = ((((2 * nivel_pokemon_aliado) + 10) / 250) * (
                poder_pokemon_aliado / defesa_pokemon_inimigo * poder_ataque_pokemon_aliado) + 2) * (
                  lista_efetividades[0])
    lista_danos.insert(0, dano_aliado)
    dano_inimigo = ((((2 * nivel_pokemon_inimigo) + 10) / 250) * (
                poder_pokemon_inimigo / defesa_pokemon_aliado * poder_ataque_pokemon_inimigo) + 2) * (
                   lista_efetividades[1])
    lista_danos.insert(1, dano_inimigo)
    return lista_danos


def calculo_efetividades(tipo_pokemon_aliado, tipo_pokemon_inimigo):
    lista_efetividades = []
    if tipo_pokemon_aliado == 'fogo':
        if tipo_pokemon_inimigo == 'agua':
            efetividade_aliada = 0.5
            efetivade_inimiga = 2
        elif tipo_pokemon_inimigo == 'grama':
            efetividade_aliada = 2
            efetivade_inimiga = 0.5
        else:
            efetividade_aliada = 1
            efetivade_inimiga = 1
    elif tipo_pokemon_aliado == 'agua':
        if tipo_pokemon_inimigo == 'fogo':
            efetividade_aliada = 2
            efetivade_inimiga = 0.5
        elif tipo_pokemon_inimigo == 'grama':
            efetividade_aliada = 0.5
            efetivade_inimiga = 2
        else:
            efetividade_aliada = 1
            efetivade_inimiga = 1
    elif tipo_pokemon_aliado == 'grama':
        if tipo_pokemon_inimigo == 'fogo':
            efetividade_aliada = 0.5
            efetivade_inimiga = 2
        elif tipo_pokemon_inimigo == 'agua':
            efetividade_aliada = 2
            efetivade_inimiga = 0.5
        else:
            efetividade_aliada = 1
            efetivade_inimiga = 1
    elif tipo_pokemon_aliado == 'normal':
        efetividade_aliada = 1
        efetivade_inimiga = 1
    lista_efetividades.insert(0, efetividade_aliada)
    lista_efetividades.insert(1, efetivade_inimiga)
    return lista_efetividades


# informaçoes do pokemon aliado
derrotar_equipe_rocket = False
informaçoes = input().split(", ")
pokemon_aliado = informaçoes[0]
tipo_pokemon_aliado = informaçoes[1]
nivel_pokemon_aliado = int(informaçoes[2])
vida_pokemon_aliado = int(informaçoes[3])
poder_pokemon_aliado = int(informaçoes[4])
defesa_pokemon_aliado = int(informaçoes[5])
velocidade_pokemon_aliado = int(informaçoes[6])
nome_ataque_pokemon_aliado = informaçoes[7]
poder_ataque_pokemon_aliado = int(informaçoes[8])
print(f'escolho você {pokemon_aliado}')
lista_vida_aliado = []
lista_vida_aliado.append(vida_pokemon_aliado)

while not derrotar_equipe_rocket:  # qnd ocorrer a batalha contra a equipe rocket, por isso uso do while
    inimigo = input()  # informaçoes inimigo
    if inimigo == 'um pokemon selvagem aparece!':
        print('vamo botar pra quebrar!')
        print()
        info_inimigo = input().split(", ")  # informaçoes pokemon inimigo
        pokemon_inimigo = info_inimigo[0]
        tipo_pokemon_inimigo = info_inimigo[1]
        nivel_pokemon_inimigo = int(info_inimigo[2])
        vida_pokemon_inimigo = int(info_inimigo[3])
        poder_pokemon_inimigo = int(info_inimigo[4])
        defesa_pokemon_inimigo = int(info_inimigo[5])
        velocidade_pokemon_inimigo = int(info_inimigo[6])
        nome_ataque_pokemon_inimigo = info_inimigo[7]
        poder_ataque_pokemon_inimigo = int(info_inimigo[8])
        lista_vida_inimigo = []
        lista_vida_inimigo.insert(0, vida_pokemon_inimigo)
        acao = ''
        lista_efetividades = calculo_efetividades(tipo_pokemon_aliado, tipo_pokemon_inimigo)
        lista_danos = calculo_dano(nivel_pokemon_aliado, poder_pokemon_aliado, defesa_pokemon_inimigo,
                                   poder_ataque_pokemon_aliado, nivel_pokemon_inimigo, poder_pokemon_inimigo,
                                   defesa_pokemon_aliado, poder_ataque_pokemon_inimigo, lista_efetividades)
        while vida_pokemon_inimigo > 0 and vida_pokemon_aliado > 0 and acao != 'correr':  # uso do while para o combate
            acao = input()
            if acao != 'correr':
                if velocidade_pokemon_aliado > velocidade_pokemon_inimigo:
                    print(f'{pokemon_aliado} usou {nome_ataque_pokemon_aliado}')
                    if lista_efetividades[0] == 0.5:
                        print('não foi muito efetivo')
                    elif lista_efetividades[0] == 2:
                        print('foi super efetivo!')
                    vida_pokemon_inimigo -= int(lista_danos[0])
                    if vida_pokemon_inimigo > 0:
                        print(f'{pokemon_inimigo} usou {nome_ataque_pokemon_inimigo}')
                        if lista_efetividades[1] == 0.5:
                            print('não foi muito efetivo')
                        elif lista_efetividades[1] == 2:
                            print('foi super efetivo!')
                        vida_pokemon_aliado -= int(lista_danos[1])
                    if vida_pokemon_aliado > 0 and vida_pokemon_inimigo > 0:
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                    elif vida_pokemon_aliado > 0 and vida_pokemon_inimigo <= 0:
                        vida_pokemon_inimigo = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_inimigo} derrotado!')
                        print()
                    elif vida_pokemon_inimigo > 0 and vida_pokemon_aliado <= 0:
                        vida_pokemon_aliado = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_aliado} derrotado!')
                        print()
                        print('Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                        derrotar_equipe_rocket = True
                else:
                    print(f'{pokemon_inimigo} usou {nome_ataque_pokemon_inimigo}')
                    if lista_efetividades[1] == 0.5:
                        print('não foi muito efetivo')
                    elif lista_efetividades[1] == 2:
                        print('foi super efetivo!')
                    vida_pokemon_aliado -= int(lista_danos[1])
                    if vida_pokemon_aliado > 0:
                        print(f'{pokemon_aliado} usou {nome_ataque_pokemon_aliado}')
                        if lista_efetividades[0] == 0.5:
                            print('não foi muito efetivo')
                        elif lista_efetividades[0] == 2:
                            print('foi super efetivo!')
                        vida_pokemon_inimigo -= int(lista_danos[0])
                    if vida_pokemon_aliado > 0 and vida_pokemon_inimigo > 0:
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                    elif vida_pokemon_aliado > 0 and vida_pokemon_inimigo <= 0:
                        vida_pokemon_inimigo = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_inimigo} derrotado!')
                        print()
                    elif vida_pokemon_inimigo > 0 and vida_pokemon_aliado <= 0:
                        vida_pokemon_aliado = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_aliado} derrotado!')
                        print()
                        print('Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                        derrotar_equipe_rocket = True
            else:
                print('ufa, consegui meter o pé!')
    else:  # combate contra a equipe rocket, acabar o while inicial
        print(f'{pokemon_aliado}, bora acabar com a raça desses bandidos e salvar o professor!')
        print()
        info_inimigo = input().split(", ")
        pokemon_inimigo = info_inimigo[0]
        tipo_pokemon_inimigo = info_inimigo[1]
        nivel_pokemon_inimigo = int(info_inimigo[2])
        vida_pokemon_inimigo = int(info_inimigo[3])
        poder_pokemon_inimigo = int(info_inimigo[4])
        defesa_pokemon_inimigo = int(info_inimigo[5])
        velocidade_pokemon_inimigo = int(info_inimigo[6])
        nome_ataque_pokemon_inimigo = info_inimigo[7]
        poder_ataque_pokemon_inimigo = int(info_inimigo[8])
        lista_vida_inimigo = []
        lista_vida_inimigo.insert(0, vida_pokemon_inimigo)
        acao = ''
        lista_efetividades = calculo_efetividades(tipo_pokemon_aliado, tipo_pokemon_inimigo)
        lista_danos = calculo_dano(nivel_pokemon_aliado, poder_pokemon_aliado, defesa_pokemon_inimigo,
                                   poder_ataque_pokemon_aliado, nivel_pokemon_inimigo, poder_pokemon_inimigo,
                                   defesa_pokemon_aliado, poder_ataque_pokemon_inimigo, lista_efetividades)
        while vida_pokemon_inimigo > 0 and vida_pokemon_aliado > 0:
            acao = input()
            if acao != 'correr':
                if velocidade_pokemon_aliado > velocidade_pokemon_inimigo:
                    print(f'{pokemon_aliado} usou {nome_ataque_pokemon_aliado}')
                    if lista_efetividades[0] == 0.5:
                        print('não foi muito efetivo')
                    elif lista_efetividades[0] == 2:
                        print('foi super efetivo!')
                    vida_pokemon_inimigo -= int(lista_danos[0])
                    if vida_pokemon_inimigo > 0:
                        print(f'{pokemon_inimigo} usou {nome_ataque_pokemon_inimigo}')
                        if lista_efetividades[1] == 0.5:
                            print('não foi muito efetivo')
                        elif lista_efetividades[1] == 2:
                            print('foi super efetivo!')
                        vida_pokemon_aliado -= int(lista_danos[1])
                    if vida_pokemon_aliado > 0 and vida_pokemon_inimigo > 0:
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                    elif vida_pokemon_aliado > 0 and vida_pokemon_inimigo <= 0:
                        vida_pokemon_inimigo = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_inimigo} derrotado!')
                        print()
                        print(
                            f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {pokemon_aliado}?')
                        derrotar_equipe_rocket = True
                    elif vida_pokemon_inimigo > 0 and vida_pokemon_aliado <= 0:
                        vida_pokemon_aliado = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_aliado} derrotado!')
                        print()
                        print('Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                        derrotar_equipe_rocket = True
                else:
                    print(f'{pokemon_inimigo} usou {nome_ataque_pokemon_inimigo}')
                    if lista_efetividades[1] == 0.5:
                        print('não foi muito efetivo')
                    elif lista_efetividades[1] == 2:
                        print('foi super efetivo!')
                    vida_pokemon_aliado -= int(lista_danos[1])
                    if vida_pokemon_aliado > 0:
                        print(f'{pokemon_aliado} usou {nome_ataque_pokemon_aliado}')
                        if lista_efetividades[0] == 0.5:
                            print('não foi muito efetivo')
                        elif lista_efetividades[0] == 2:
                            print('foi super efetivo!')
                        vida_pokemon_inimigo -= int(lista_danos[0])
                    if vida_pokemon_aliado > 0 and vida_pokemon_inimigo > 0:
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')

                    elif vida_pokemon_aliado > 0 and vida_pokemon_inimigo <= 0:
                        vida_pokemon_inimigo = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_inimigo} derrotado!')
                        print()
                        print(
                            f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {pokemon_aliado}?')
                        derrotar_equipe_rocket = True
                    elif vida_pokemon_inimigo > 0 and vida_pokemon_aliado <= 0:
                        vida_pokemon_aliado = 0
                        print(
                            f'HP: {vida_pokemon_aliado}/{lista_vida_aliado[0]} | HP inimigo: {vida_pokemon_inimigo}/{lista_vida_inimigo[0]}')
                        print(f'{pokemon_aliado} derrotado!')
                        print()
                        print('Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                        derrotar_equipe_rocket = True
            else:  # nao da p correr
                print('lascou, eles não largam do meu pé!')










