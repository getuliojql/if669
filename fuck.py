# TENTATIVA FRUSTRADA DO EXERCÍCIO F DA LISTA 1 #

nome = str(input())
pessoas = int(input())
coef = float(input())
bordao = 'fuma não pow, cuide da sua saúde'
if pessoas % 2 == 0:
  fumantes = coef * (pessoas - 1) + 1
else:
  fumantes = coef * (pessoas - 1) / 2
if coef != 0:
  fumantes_str = str(fumantes)
  fumantes_str = fumantes_str[0:int(fumantes_str.find('.') + 2)]
  fumantes_int = int(len(fumantes_str))
  fumantes_aaa = int(fumantes_str[fumantes_int - 1])
  if 1 <= fumantes_aaa <= 5:
    fumantes -= (fumantes_aaa / 10)
  else:
    fumantes += (10 - fumantes_aaa) / 10
proporcao = (int(fumantes) / pessoas) * 100
print('Vamos verificar se {} vai fumar singaro!'.format(nome))
print('{:.0f}% dos seus amigos fumam singaro'.format(proporcao))
if proporcao < 25:
  print('Você tem poucas chances de fumar singaro, {}'.format(bordao))
elif 25 < proporcao < 50:
  print('Cuidado pra não fumar ein, {}'.format(bordao))
elif proporcao > 50:
  print('TIRA ESSE SINGARO DA BOCA. {}!'.format(bordao.upper()))



'''coef = float(input('valor de coef: '))
coef_str = str(coef)
coef_int = int(len(str(coef)))
print(coef_str[coef_int - 1])'''

coef = float(input('valor de coef: '))
coef_str = str(coef)
coef_int = int(len(coef_str))
print(coef)
print(coef_str)
print(coef_int)


'''
coef_aaa = int(coef_str[coef_int - 1])
if 1 <= coef_aaa <= 5:
  coef -= coef_aaa'''

coef_str = str(coef)
coef_int = int(len(coef_str))
coef_aaa = int(coef_str[coef_int - 1])
if 1 <= coef_aaa <= 5:
  coef -= (coef_aaa / 10)
else:
  coef += (10 - coef_aaa) / 10
print(coef)

'''nome = str(input())
pessoas = int(input())
coef = float(input())
bordao = 'fuma não pow, cuide da sua saúde'
if pessoas % 2 == 0:
  fumantes = coef * (pessoas - 1) + 1
else:
  fumantes = coef * (pessoas - 1) / 2
ffumantes = fumantes - int(fumantes)
if 0.1 <= ffumantes <= 0.5:
  fumantes -= ffumantes
elif ffumantes > 0.5:
  fumantes += (1 - ffumantes)
proporcao = (fumantes / pessoas) * 100
print('Vamos verificar se {} vai fumar singaro!'.format(nome))
print('{:.0f}% dos seus amigos fumam singaro'.format(proporcao))
if proporcao < 25:
  print('Você tem poucas chances de fumar singaro, {}'.format(bordao))
elif 25 < proporcao < 50:
  print('Cuidado pra não fumar ein, {}'.format(bordao))
elif proporcao > 50:
  print('TIRA ESSE SINGARO DA BOCA. {}!'.format(bordao.upper()))'''
