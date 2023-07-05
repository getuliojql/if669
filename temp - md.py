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
#listas

produtos_vendidos = ['cpu', 'gpu', 'fonte', 'cooler']
produtos_estoque = ['cpu', 'cpu', 'cpu', 'gpu', 'gpu', 'fonte', 'fonte', 'fonte', 'fonte', 'cooler']

produto_consultado = str(input('Digite o produto que deseja consultar: '))
estoque_consultado = 0

vendido = False

for produto in produtos_vendidos:
    if produto_consultado == produto:
        vendido = True

if vendido:
    for produto in produtos_estoque:
        if produto_consultado == produto:
            estoque_consultado += 1
    print(f'Nossa loja vende {produto_consultado} sim! Atualmente temos {estoque_consultado} {produto_consultado}(s) em loja...')
else:
    print(f'Infelizmente nós não vendemos {produto_consultado} :(')