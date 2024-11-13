def checar_sobrevivencia(coord_sobreviventes, coord_explosao, raio):
    sobreviventes = []

    for idx_c, c in enumerate(coord_sobreviventes):
        sobreviventes.append([])

        for i in c:
            dist = ((coord_explosao[0] - i[0]) ** 2 + (coord_explosao[1] - i[1]) ** 2) ** .5

            if dist > raio:
                sobreviventes[idx_c].append(i)

    return sobreviventes


def pontos_centrais(capsulas_sobreviventes):
    pontos = []

    for idx_c, c in enumerate(capsulas_sobreviventes):
        soma_x = soma_y = 0

        for idx_i, i in enumerate(capsulas_sobreviventes[idx_c]):
            soma_x += capsulas_sobreviventes[idx_c][idx_i][0]
            soma_y += capsulas_sobreviventes[idx_c][idx_i][1]

        if len(capsulas_sobreviventes[idx_c]) != 0:
            soma_x /= len(capsulas_sobreviventes[idx_c])
            soma_y /= len(capsulas_sobreviventes[idx_c])
            pontos.append([soma_x, soma_y])

    return pontos


def resgatar_astronautas(caps, posi, raio):
    num_sobreviventes = 0
    lista_sobreviventes = checar_sobrevivencia(caps, posi, raio)

    for c in lista_sobreviventes:
        num_sobreviventes += len(c)

    return [num_sobreviventes, pontos_centrais(lista_sobreviventes)]


capsulas = eval(str(input()))
posicao_explosao = eval(str(input()))
raio_impacto = int(input())

print(resgatar_astronautas(capsulas, posicao_explosao, raio_impacto))
