nota_1 = 3.64
nota_2 = 0
nota_3 = 1.75
nota_4 = None

nota_final = 0

print('se eu tirar ˇ vou precisar tirar ˇ')

for i in range(0, 21):
    nota_4 = i / 2

    while ((((nota_1 + nota_2 + nota_3 + nota_4) / 4) + nota_final) / 2) < 5:
        nota_2 += 0.1
        nota_final = nota_2

    if int(nota_4) != 10:
        print(f'           {nota_4}        ->        {nota_final:.1f}')

    else:
        print(f'           {nota_4}       ->        {nota_final:.1f}')

    nota_2 = nota_final = 0