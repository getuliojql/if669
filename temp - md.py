'''
y = 0
z = 0
for c in range(0, 67):
    x = float(input())
    if x > 0.35:
        y += 1
    elif x == 0.35:
        print('Mesma nota')
    else:
        z += 1
print(f'Notas maiores: {y}')
print(f'Notas menores: {z}')


x = int(input())
print((2 * abs((x ** 2))) - x)
'''
