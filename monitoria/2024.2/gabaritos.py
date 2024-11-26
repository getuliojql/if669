suspeito_1 = input()
distancia_1 = int(input())
suspeito_2 = input()
distancia_2 = int(input())
suspeito_1_culpado = False
suspeito_2_culpado = False

distancia_entre = (distancia_1 ** 2 + distancia_2 ** 2) ** 0.5

if distancia_entre % 2 == 0:
    print(
        f'{suspeito_1} e {suspeito_2} sao CUMPLICES no crime! Se juntaram para confundir a policia, mas os CIners sao mais espertos! A Bola de Ouro sera recuperada com sucesso!')
else:
    tipo_1 = input()
    tipo_2 = input()

    if tipo_1 != tipo_2:
        # São de tipos diferentes, então se baseia na distância.
        if distancia_1 > distancia_2:
            suspeito_2_culpado = True
        elif distancia_2 > distancia_1:
            # Se as distâncias forem iguais eles são ambos inocentes
            suspeito_1_culpado = True
    else:
        # Se eles forem do mesmo tipo, depende do tipo E da distância.
        if tipo_1 == 'Fã':
            # Se o tipo for fã
            if not (distancia_1 % 6 and distancia_2 % 6):
                suspeito_1_culpado = True
                suspeito_2_culpado = True
            elif not distancia_1 % 2:
                suspeito_2_culpado = True
            elif not distancia_2 % 3:
                suspeito_1_culpado = True

        else:
            # Se o tipo for jogador
            if not (distancia_1 % 10 and distancia_2 % 10):
                suspeito_1_culpado = True
                suspeito_2_culpado = True
            elif not distancia_1 % 2:
                suspeito_2_culpado = True
            elif not distancia_2 % 5:
                suspeito_1_culpado = True

    if not suspeito_1_culpado and not suspeito_2_culpado:
        print(
            f'{suspeito_1} e {suspeito_2} sao INOCENTES! A policia parisiense nao fez um bom trabalho... Vamos continuar procurando!')

    suspeito_culpado = ''

    if suspeito_1_culpado:
        suspeito_culpado = suspeito_1
    elif suspeito_2_culpado:
        suspeito_culpado = suspeito_2

    if suspeito_1_culpado and suspeito_2_culpado:
        print(
            f'{suspeito_1} e {suspeito_2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!')
    elif suspeito_1_culpado or suspeito_2_culpado:
        print(
            f'{suspeito_culpado} e o CULPADO! Ele(a) confessou a localizacao da Bola de Ouro e ela foi retornada com sucesso!')
