m = 0
y = 0
z = 0

qtd_notas = 85  # ⬅ mudar
minha_nota = 7.1  # ⬅ mudar

for c in range(0, qtd_notas):
    x = float(input())
    if x > minha_nota:
        y += 1
    elif x == minha_nota:
        m += 1
    else:
        z += 1
print(f'Notas maiores: {y}')
print(f'Notas iguais: {m}')
print(f'Notas menores: {z}')
