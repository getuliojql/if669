# início
partidas = int(input())
partidas_cont = 0
controle = 1
vit_rod_jogador = 0
vit_rod_adversario = 0
vit_part_jogador = 0
vit_part_adversario = 0

# cálculo
while partidas > 0 and controle != 0:
    partidas -= 1
    partidas_cont += 1
    rodadas = int(input())

    if partidas != 0:
        print(f'Vai começar a {partidas_cont}º partida. Esse jogo terá {rodadas} rodada(s).')
    else:
        print(f'Tá na hora da grande final! Esse jogo terá {rodadas} rodada(s)')

    for c in range(0, rodadas):
        hab_jogador = int(input())
        hab_adversario = int(input())

        if hab_jogador >= hab_adversario:
            vit_rod_jogador += 1
        else:
            vit_rod_adversario += 1
        if c == (rodadas - 1):
            if partidas != 0:
                print(f'Fim de jogo! O placar foi {vit_rod_jogador}x{vit_rod_adversario}')

                if vit_rod_jogador > vit_rod_adversario and (
                        vit_rod_jogador - vit_rod_adversario) >= 5 and partidas != 1:
                    print(
                        'QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!')
                    controle = 0
                elif vit_rod_jogador > vit_rod_adversario:
                    print('Vamos para próxima fase!')
                elif vit_rod_jogador <= vit_rod_adversario:
                    print('Não foi dessa vez! Treinar pro ano que vem!')
                    controle = 0
                vit_rod_jogador = 0
                vit_rod_adversario = 0

            else:
                if vit_rod_jogador <= vit_rod_adversario:
                    print('Ah não!! Chegaram tão longe mas não foi dessa vez. :(')
                else:
                    print('É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!')