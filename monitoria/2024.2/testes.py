def registra_conexoes(qtd_estados):
    lista_conexoes = []
    for i in range(qtd_estados):
        conexao = input()
        lista_interna = []
        lista_interna.append(conexao)
        lista_conexoes.append(lista_interna)
    return lista_conexoes

def registra_cadeias(qtd_cadeias_binarias):
    lista_cadeias_binarias = []
    for j in range(qtd_cadeias_binarias):
        cadeia_binaria = input()
        estado_inicial = input()
        lista_interna_cadeias = []
        lista_interna_cadeias.append(cadeia_binaria)
        lista_interna_cadeias.append(estado_inicial)
        lista_cadeias_binarias.append(lista_interna_cadeias)
    return lista_cadeias_binarias

def imprime_conexoes(lista_conexoes):
    contador = 1
    for k in lista_conexoes:
        for l in range(len(k)):
            k[l] = k[l].replace("-", "->")
            print(f"q{contador}: {{{k[l]}}}")
            contador += 1

def processa_cadeia(estado_aceitacao, estado_inicial, cadeia, lista_conexoes):
    if cadeia == "ε" and estado_inicial == estado_aceitacao:
        print("Caramba, essa cadeia é abençoada! Nem precisei trabalhar!")
        return True
    elif cadeia == "ε" and estado_inicial != estado_aceitacao:
        print("Nossa, que maldição! Nem começou e já deu errado…")
        return False
    else:
        estado_atual = estado_inicial[-1]
        qtd_estados = len(lista_conexoes)
        for caractere in cadeia:
            if caractere != "0" and caractere != "1":
                print(f"Só pode estar de brincadeira comigo! Como vou lidar com {caractere} dentro da máquina?")
                return False

            for conexao in lista_conexoes:
                associacoes = conexao[0].split(', ')
                indice_lista_conexoes = lista_conexoes.index(conexao)
                if int(estado_atual) == (indice_lista_conexoes + 1):
                    indice0 = associacoes[0]
                    indice1 = associacoes[1]
                    if caractere == "0":
                        estado_atual = indice0[-1]
                    else:
                        estado_atual = indice1[-1]
                    break

        if estado_atual == estado_aceitacao[-1]:
            print("Beleza! Após suar muito a cadeia foi aceita, o esforço ta sendo compensado!")
            return True
        else:
            print("Que tristeza, todo esse arrudeio pra nada…")
            return False


qtd_estados = int(input())
if qtd_estados != 1:
    estado_aceitacao = input()
    lista_conexoes = registra_conexoes(qtd_estados)
    qtd_cadeias_binarias = int(input())
    lista_cadeias_binarias = registra_cadeias(qtd_cadeias_binarias)
    imprime_conexoes(lista_conexoes)

    for sublista in lista_cadeias_binarias:
        cadeia = sublista[0]
        estado_inicial = sublista[1]
        aceita = processa_cadeia(estado_aceitacao, estado_inicial, cadeia, lista_conexoes)
else:
    print("É… acho que não tem muito o que fazer com apenas uma dimensão, vou ter que me contentar com minha triste realidade :(")
