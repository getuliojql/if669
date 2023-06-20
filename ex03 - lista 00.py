peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / altura ** 2
if imc <= 18.5:
    print('\033[33mVocê está abaixo do peso!')
elif imc <= 25:
    print('\033[32mSeu peso está normal!')
elif imc <= 30:
    print('\033[33mVocê está acima do peso!')
else:
    print('\033[31mVocê está obeso!')
