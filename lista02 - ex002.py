#variáveis
participantes = int(input())
nome_1 = str(input())
pontuacao_1 = int(input())
penalidade_1 = int(input())
final = pontuacao_1 - penalidade_1

#recebimento dos dados e novo vencedor
for c in range(0, participantes - 1):
    nome_2 = str(input())
    pontuacao_2 = int(input())
    penalidade_2 = int(input())
    if (pontuacao_2 - penalidade_2) > (pontuacao_1 - penalidade_1):
        nome_1 = nome_2
        final = pontuacao_2 - penalidade_2

#resultado
print(f'O grande vencedor do torneio foi {nome_1} com um total de {final} pontos!')
