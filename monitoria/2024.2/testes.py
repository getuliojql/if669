nome_suspeito1 = str(input())
distancia_suspeito1 = int(input())
nome_suspeito2 = str(input())
distancia_suspeito2 = int(input())
distancia_entre_suspeitos = (distancia_suspeito1**2 + distancia_suspeito2**2)
distancia_entre_suspeitos2 = distancia_entre_suspeitos ** 1/2
distancia_entre_suspeitos = distancia_entre_suspeitos ** 0.5
if distancia_entre_suspeitos % 2 == 0:
    print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
else:
    categoria_suspeito1 = str(input()).capitalize()
    categoria_suspeito2 = str(input()).capitalize()
    if categoria_suspeito1 == categoria_suspeito2 == "Fã":
        if (distancia_suspeito1 % 6 == 0) and (distancia_suspeito2 % 6 == 0):
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        else:
            if distancia_suspeito1 % 2 == 0:
                print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
            elif distancia_suspeito2 % 3 == 0:
                print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
    elif categoria_suspeito1 == categoria_suspeito2 == "Jogador":
        if (distancia_suspeito1 % 10 == 0) and (distancia_suspeito2 % 10 == 0):
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        else:
            if distancia_suspeito1 % 2 == 0:
                print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
            elif distancia_suspeito2 % 5 == 0:
                print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
    elif categoria_suspeito1 == categoria_suspeito2 == "Jornalista":
        if (distancia_suspeito1 % 15 == 0) and (distancia_suspeito2 % 15 == 0):
            print(f"{nome_suspeito1} e {nome_suspeito2} são CÚMPLICES no crime! Se juntaram para confundir a polícia, mas os CIners são mais espertos! A Bola de Ouro será recuperada com sucesso!")
        else:
            if distancia_suspeito1 % 3 == 0:
                print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
            elif distancia_suspeito2 % 5 == 0:
                print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
    else:
        if distancia_suspeito1 > distancia_suspeito2:
            print(f"{nome_suspeito2} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        elif distancia_suspeito1 < distancia_suspeito2:
            print(f"{nome_suspeito1} é o(a) CULPADO(A)! Ele(a) confessou a localização da Bola de Ouro e ela foi retornada com sucesso!")
        else:
            print(f"{nome_suspeito1} e {nome_suspeito2} são INOCENTES! A polícia parisiense não fez um bom trabalho... Vamos continuar procurando!")
