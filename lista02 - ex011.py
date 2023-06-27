# top
nome_top = ''
elo_top = ''
controle_top = 0

# jungler
nome_jungler = ''
elo_jungler = ''
controle_jungler = 0

# mid
nome_mid = ''
elo_mid = ''
controle_mid = 0

# adc
nome_adc = ''
elo_adc = ''
controle_adc = 0

# suporte
nome_suporte = ''
elo_suporte = ''
controle_suporte = 0

# variáveis de ajuda
rodada = 0
pontuacao = 0
controle_while = 1
controle_entrada = 0
controle_faltantes = 5

# recebimento dos dados
while controle_while != 0:
    nome = str(input())

    # conferindo se é a bruna
    if nome == 'Bruna':
        print('LOL NÃO!!! TUDO MENOS LOL!!!')
        controle_while = 0

    # recebendo o resto, caso não seja
    else:
        lane = str(input())
        elo = str(input())
        rodada += 1

        # conferindo se o elo existe
        if elo != 'Bronze' and elo != 'Prata' and elo != 'Ouro' and elo != 'Platina' and elo != 'Diamante' and elo != 'Desafiante':
            print('Não conheço esse elo, então vou considerar que é um elo ruim.')

        # top
        if lane == 'Top' and controle_top == 0:
            nome_top = nome
            elo_top = elo
            controle_top = rodada
            controle_entrada = 1
            controle_faltantes -= 1
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print('Ele tá meio enferrujado...')
            elif nome == 'Frej':
                print('Joga muito!')

            # se for o 1°
            if controle_faltantes == 4:
                nome1 = nome_top
                lane1 = 'Top'
                elo1 = elo_top

            # se for o 2°
            elif controle_faltantes == 3:
                nome2 = nome_top
                lane2 = 'Top'
                elo2 = elo_top

            # se for o 3°
            elif controle_faltantes == 2:
                nome3 = nome_top
                lane3 = 'Top'
                elo3 = elo_top

            # se for o 4°
            elif controle_faltantes == 1:
                nome4 = nome_top
                lane4 = 'Top'
                elo4 = elo_top

            # se for o 5°
            elif controle_faltantes == 0:
                nome5 = nome_top
                lane5 = 'Top'
                elo5 = elo_top

        elif lane == 'Top' and controle_top != 0:
            print(f'{nome} não foi aceito, que pena.')

        # jungler
        elif lane == 'Jungler' and controle_jungler == 0:
            nome_jungler = nome
            elo_jungler = elo
            controle_jungler = rodada
            controle_entrada = 1
            controle_faltantes -= 1
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print('Ele tá meio enferrujado...')
            elif nome == 'Frej':
                print('Joga muito!')

            # se for o 1°
            if controle_faltantes == 4:
                nome1 = nome_jungler
                lane1 = 'Jungler'
                elo1 = elo_jungler

            # se for o 2°
            elif controle_faltantes == 3:
                nome2 = nome_jungler
                lane2 = 'Jungler'
                elo2 = elo_jungler

            # se for o 3°
            elif controle_faltantes == 2:
                nome3 = nome_jungler
                lane3 = 'Jungler'
                elo3 = elo_jungler

            # se for o 4°
            elif controle_faltantes == 1:
                nome4 = nome_jungler
                lane4 = 'Jungler'
                elo4 = elo_jungler

            # se for o 5°
            elif controle_faltantes == 0:
                nome5 = nome_jungler
                lane5 = 'Jungler'
                elo5 = elo_jungler

        elif lane == 'Jungler' and controle_jungler != 0:
            print(f'{nome} não foi aceito, que pena.')

        # mid
        elif lane == 'Mid' and controle_mid == 0:
            nome_mid = nome
            elo_mid = elo
            controle_mid = rodada
            controle_entrada = 1
            controle_faltantes -= 1
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print('Ele tá meio enferrujado...')
            elif nome == 'Frej':
                print('Joga muito!')

            # se for o 1°
            if controle_faltantes == 4:
                nome1 = nome_mid
                lane1 = 'Mid'
                elo1 = elo_mid

            # se for o 2°
            elif controle_faltantes == 3:
                nome2 = nome_mid
                lane2 = 'Mid'
                elo2 = elo_mid

            # se for o 3°
            elif controle_faltantes == 2:
                nome3 = nome_mid
                lane3 = 'Mid'
                elo3 = elo_mid

            # se for o 4°
            elif controle_faltantes == 1:
                nome4 = nome_mid
                lane4 = 'Mid'
                elo4 = elo_mid

            # se for o 5°
            elif controle_faltantes == 0:
                nome5 = nome_mid
                lane5 = 'Mid'
                elo5 = elo_mid

        elif lane == 'Mid' and controle_mid != 0:
            print(f'{nome} não foi aceito, que pena.')

        # adc
        elif lane == 'Adc' and controle_adc == 0:
            nome_adc = nome
            elo_adc = elo
            controle_adc = rodada
            controle_entrada = 1
            controle_faltantes -= 1
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print('Ele tá meio enferrujado...')
            elif nome == 'Frej':
                print('Joga muito!')

            # se for o 1°
            if controle_faltantes == 4:
                nome1 = nome_adc
                lane1 = 'Adc'
                elo1 = elo_adc

            # se for o 2°
            elif controle_faltantes == 3:
                nome2 = nome_adc
                lane2 = 'Adc'
                elo2 = elo_adc

            # se for o 3°
            elif controle_faltantes == 2:
                nome3 = nome_adc
                lane3 = 'Adc'
                elo3 = elo_adc

            # se for o 4°
            elif controle_faltantes == 1:
                nome4 = nome_adc
                lane4 = 'Adc'
                elo4 = elo_adc

            # se for o 5°
            elif controle_faltantes == 0:
                nome5 = nome_adc
                lane5 = 'Adc'
                elo5 = elo_adc

        elif lane == 'Adc' and controle_adc != 0:
            print(f'{nome} não foi aceito, que pena.')

        # suporte
        elif lane == 'Suporte' and controle_suporte == 0:
            nome_suporte = nome
            elo_suporte = elo
            controle_suporte = rodada
            controle_entrada = 1
            controle_faltantes -= 1
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print('Ele tá meio enferrujado...')
            elif nome == 'Frej':
                print('Joga muito!')

            # se for o 1°
            if controle_faltantes == 4:
                nome1 = nome_suporte
                lane1 = 'Suporte'
                elo1 = elo_suporte

            # se for o 2°
            elif controle_faltantes == 3:
                nome2 = nome_suporte
                lane2 = 'Suporte'
                elo2 = elo_suporte

            # se for o 3°
            elif controle_faltantes == 2:
                nome3 = nome_suporte
                lane3 = 'Suporte'
                elo3 = elo_suporte

            # se for o 4°
            elif controle_faltantes == 1:
                nome4 = nome_suporte
                lane4 = 'Suporte'
                elo4 = elo_suporte

            # se for o 5°
            elif controle_faltantes == 0:
                nome5 = nome_suporte
                lane5 = 'Suporte'
                elo5 = elo_suporte

        elif lane == 'Suporte' and controle_suporte != 0:
            print(f'{nome} não foi aceito, que pena.')

        # atribuindo os valores dos elos à pontuação
        if controle_entrada == 1:
            if elo == 'Bronze':
                pontuacao += 1
            elif elo == 'Prata':
                pontuacao += 2
            elif elo == 'Ouro':
                pontuacao += 4
            elif elo == 'Platina':
                pontuacao += 6
            elif elo == 'Diamante':
                pontuacao += 8
            elif elo == 'Desafiante':
                pontuacao += 10
            controle_entrada = 0

        # time completo
        if controle_top > 0 and controle_jungler > 0 and controle_mid > 0 and controle_adc > 0 and controle_suporte > 0:
            print('O time está completo.')

            # time, em ordem
            print(f'{nome1} - {lane1} ({elo1})')
            print(f'{nome2} - {lane2} ({elo2})')
            print(f'{nome3} - {lane3} ({elo3})')
            print(f'{nome4} - {lane4} ({elo4})')
            print(f'{nome5} - {lane5} ({elo5})')

            # pontuacao
            if (
                    nome_top == 'Artur' or nome_jungler == 'Artur' or nome_mid == 'Artur' or nome_adc == 'Artur' or nome_suporte == 'Artur') and (
                    nome_top != 'Frej' and nome_jungler != 'Frej' and nome_mid != 'Frej' and nome_adc != 'Frej' and nome_suporte != 'Frej'):
                print('Vai dar ruim...')
            elif (
                    nome_top == 'Frej' or nome_jungler == 'Frej' or nome_mid == 'Frej' or nome_adc == 'Frej' or nome_suporte == 'Frej') and (
                    nome_top != 'Artur' and nome_jungler != 'Artur' and nome_mid != 'Artur' and nome_adc != 'Artur' and nome_suporte != 'Artur'):
                print('A GENTE VAI GANHAR!!!')
            elif (pontuacao >= 18):
                print('A GENTE VAI GANHAR!!!')
            else:
                print('Vai dar ruim...')

            controle_while = 0