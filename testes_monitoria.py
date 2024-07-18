print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")

artista_1 = input()
artista_2 = input()

print(f"E os artistas de hoje são {artista_1} e {artista_2}!")

# Dicionários "disco-preço" para o artista 1 e o artista 2
album_1 = {}
album_2 = {}


stop = False # Parâmetro de entrada do loop para o artista 1 e 2
while not stop:
    disco = input()
    if disco == "acabou":
        stop = True
    else:
        preco = float(input())

        album_1[disco] = preco
# !!! FAZER UMA FUNÇÃO PARA ESSES LOOPs
stop = False
while not stop:
    disco = input()
    if disco == "acabou":
        stop = True
    else:
        preco = float(input())

        album_2[disco] = preco

print("-----COMEÇO DO EXPEDIENTE!-----")

# discos vendidos e receitas feitos pelo artista 1 e 2
discos_vendidos_1 = 0
discos_vendidos_2 = 0
receita_1 = 0
receita_2 = 0

stop = False
while not stop:
    disco = input()
    if disco == "FIM":
        stop = True
    else:
        if disco in album_1 or disco in album_2:
            print(f"{disco} vendido")
            if disco in album_1:
                discos_vendidos_1 += 1
                receita_1 += album_1[disco]
            else:
                discos_vendidos_2 += 1
                receita_2 += album_2[disco]

            if discos_vendidos_1 > discos_vendidos_2 and (discos_vendidos_1 - discos_vendidos_2) % 3 == 0 and discos_vendidos_1 - discos_vendidos_2 !=0:
                print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista_1.upper()} E ABAIXA R$4 DE {artista_2.upper()}!")

                for i in album_1:
                    album_1[i] += 4
                for j in album_2:
                    if album_2[j] > 3:
                        album_2[j] -= 4
                    else:
                        album_2[j] = 1
            elif discos_vendidos_2 > discos_vendidos_1 and (discos_vendidos_2 - discos_vendidos_1) % 3 == 0 and discos_vendidos_1 - discos_vendidos_2 != 0:
                print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {artista_2.upper()} E ABAIXA R$4 DE {artista_1.upper()}!")

                for i in album_2:
                    album_2[i] += 4
                for j in album_1:
                    if album_1[j] > 3:
                        album_1[j] -= 4
                    else:
                        album_1[j] = 1
        else:
            print("Parece que não temos esse disco...")

print("-----FIM DO EXPEDIENTE!-----")

discos_vendidos_total = discos_vendidos_1 + discos_vendidos_2
receita_total = receita_1 + receita_2

if receita_total == 0:
    print(f"O total de receita gerado foi de {receita_total} e foram vendidos {discos_vendidos_total} discos.")
else:
    print(f"O total de receita gerado foi de {receita_total:.1f} e foram vendidos {discos_vendidos_total} discos.")

if discos_vendidos_1 + discos_vendidos_2 == 0:
    print("Que tristeza! Só artista péssimo...")
elif receita_1 == receita_2:
    print("Difícil de escolher o melhor!")
elif receita_1 > receita_2:
    print(f"O artista que mais gerou dinheiro para a loja foi {artista_1}, acumulando uma receita de {receita_1} e vendendo {discos_vendidos_1} discos.")
elif receita_2 > receita_1:
    print(f"O artista que mais gerou dinheiro para a loja foi {artista_2}, acumulando uma receita de {receita_2} e vendendo {discos_vendidos_2} discos.")