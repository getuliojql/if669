personagens_da_serie = ["Jinx", "Vi", "Heimerdinger", "Ekko", "Caitlyn", "Jayce", "Viktor", "Silco", "Claggor",
                        "Vander", "Mylo"]
personagens_chutados = [""] * 11
chutes_final = []


def adicionar(tentativa):
    for i in range(len(personagens_da_serie)):
        if personagens_chutados[i] == "":
            personagens_chutados[i] = tentativa
            print(f'Personagem {tentativa} adicionado')
            break


def remover(tentativa):
    if tentativa in personagens_chutados:
        for i in range(11):
            if tentativa == personagens_chutados[i]:
                personagens_chutados[i] = ""
                break


n_max = int(input())

while n_max > 0:
    chute = input()
    if chute == "Adiciona":
        tentativa = input()
        adicionar(tentativa)
        n_max -= 1
    elif chute == "Remove":
        tentativa = input()
        remover(tentativa)
        n_max += 1

for j in personagens_chutados:
    if j != "":
        chutes_final += [j]

print("Lista final de personagens:")
for i in chutes_final:
    print(i)

contador = 0
for i in range(len(chutes_final)):
    if chutes_final[i] in personagens_da_serie:
        contador += 1

if contador == len(chutes_final):
    print("Parabéns!! Você conseguiu acertar todos os nomes.")
    print("UAUUU! Acho que estamos preparados para ver a segunda temporada.")
else:
    print("Infelizmente você perdeu...")
    print("Eita... Vamos precisar assistir novamente.")
