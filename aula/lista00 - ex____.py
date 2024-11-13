# mensagem inicial
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

#calorias gastas
basal = int(input("Digite sua taxa metabólica basal: "))
calorias_gastas = int(input("Digite a quantidade média de calorias gastas ao realizer exercício: "))
frequencia_exercicio = int(input("Digite a frequência semanal de seus exercícios físicos: "))
meses_descanso = int(input("Digite o número de meses nos quais você descansa: "))
total_calorias = (basal * 7 * 4 * 12) + (calorias_gastas * frequencia_exercicio * 4 * (12 - meses_descanso))
print(nome + ", você gasta " + str(total_calorias) + " calorias por ano!")

#calorias consumidas
calorias_refeicao = int(input("Digite a média de calorias que você consome por refeição: "))
refeicoes_dia = int(input("Digite quantas vezes você come por dia: "))
calorias_ingeridas = calorias_refeicao * refeicoes_dia * 7 * 4 * 12
total_calorias_final = total_calorias - calorias_ingeridas
print("Mas, já que você consome " + str(calorias_ingeridas) + " calorias todo ano")

# gasto total
print("Seu gasto total é de " + str(total_calorias_final) + " calorias!")

# vai ganhar ou vai perder?
if total_calorias > calorias_ingeridas:
    print(nome + ", você vai perder peso!")
elif total_calorias == calorias_ingeridas:
    print(nome + ", você vai continuar com o mesmo peso que está!")
else:
    print(nome + ", você vai ganhar peso!")
