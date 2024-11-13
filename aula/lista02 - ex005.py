# início
jogos = int(input())
total_manchester = 0
total_spicin = 0
controle = 1
partidas = 0

# recebimento das variáveis e cálculo
while controle != 0:
    for c in range(0, jogos):
        nome = str(input())
        gols = int(input())
        chutes = int(input())
        amarelos = int(input())
        vermelhos = int(input())
        partidas += 1

        if nome == 'Manchester CIn':
            total_manchester += (gols * 10) + (chutes * 3) + (amarelos * -2) + (vermelhos * -4)
            if gols >= (0.3 * chutes):
                total_manchester += 3
            if vermelhos >= amarelos:
                total_manchester -= 3

        elif nome == 'SpiCIn Girls':
            total_spicin += (gols * 10) + (chutes * 3) + (amarelos * -2) + (vermelhos * -4)
            if gols >= (0.3 * chutes):
                total_spicin += 3
            if vermelhos >= amarelos:
                total_spicin -= 3

        if total_manchester < 0 or total_spicin < 0:
            if total_manchester < 0:
                perdedor = 'Manchester CIn'
            elif total_spicin < 0:
                perdedor = 'SpiCIn Girls'
            print(
                f'O time {perdedor} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.')
            controle = 0
        if partidas == 5:
            controle = 0

# resultado
if total_manchester > total_spicin:
    vencedor = 'Manchester CIn'
    porcentagem = (total_manchester / (total_manchester + total_spicin)) * 100

elif total_spicin > total_manchester:
    vencedor = 'SpiCIn Girls'
    porcentagem = (total_spicin / (total_manchester + total_spicin)) * 100

print(
    f'Com {porcentagem:.2f}% dos pontos, o time {vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')