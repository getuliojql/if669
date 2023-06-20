x = float(input('Digite o valor do primeiro lado: '))
y = float(input('Digite o valor do segundo lado: '))
z = float(input('Digite o valor do terceiro lado: '))
if x == y == z:
    print('O triângulo é \033[32mEQUILÁTERO\033[m!')
elif x == y or x == z or y == z:
    print('O triângulo é \033[33mISÓSCELES\033[m!')
else:
    print('O triângulo é \033[31mESCALENO\033[m!')
