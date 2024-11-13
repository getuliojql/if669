# definindo a matriz e recebendo a variável inicial
matriz = []
diagramacao = int(input())

# criando sublistas
for andar in range(diagramacao):
    matriz.append([])

# recebendo as informacoes do tamanho dos cômodos
for idx_andar, andar in enumerate(matriz):
    for comodo in range(diagramacao):
        matriz[idx_andar].append(int(input()))

# imprimindo a matriz
for idx_andar, andar in enumerate(matriz):
    for idx_comodo, comodo in enumerate(matriz[idx_andar]):
        if idx_comodo == len(matriz[idx_andar]) - 1:
            print(f'{comodo}', end='')
        else:
            print(f'{comodo}', end=' ')
    print()
