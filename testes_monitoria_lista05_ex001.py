def calculo_login(numero, somatorio):
    if numero == 0:
        return somatorio

    else:
        if int(numero) % 2 == 0:
            somatorio += str(numero * 2)

        else:
            somatorio += str(numero * 3)

        return calculo_login(int(numero) - 1, somatorio)


def calculo_senha(numero, somatorio):
    return 0


login = senha = '0'

entrada = input().split(':')

for valor in entrada:
    login += calculo_login(valor, '0')
    # senha += calculo_senha(valor, '0')

print('As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!')
print(f'Login: {login}\nSenha: {senha}')
