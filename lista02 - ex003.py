estoque = 20
controle = 1

# frases
acabou = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
encham = 'Encham o cooler, vai começar um jogo!!!!'
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário'
intercin = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

# começando
while controle != 0:
    frase = str(input())
    if frase == acabou:
        sedentos = int(input())
        if estoque >= sedentos:
            estoque -= sedentos
        else:
            print(f'Não teremos água para todos os jogadores... Temos que garantir {sedentos - estoque} garrafas!!')
            estoque += estoque
            estoque -= sedentos

    if frase == encham:
        estoque += 15
        print('Geladeira cheia!')
    if frase == timeout:
        vol_1 = int(input())
        vol_2 = int(input())
        vol_3 = int(input())
        vol_4 = int(input())
        vol_5 = int(input())
        soma_vol = vol_1 + vol_2 + vol_3 + vol_4 + vol_5
        estoque -= soma_vol
        if estoque < 0:
            estoque = abs(estoque)
            print(f'Prometemos distribuir {estoque} garrafas e zeramos')

    if frase == intercin:
        controle = 0
    if estoque < 0:
        print('Por questões logísticas, teremos que acabar com os jogos...')
        controle = 0

# final
if estoque > 0:
    print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')
elif estoque == 0:
    print('Vendemos todas as águas, fizemos uma contagem certeira!!')
else:
    print(f'Estamos devendo {abs(estoque)} para os alunos')


'''
estoque = 35
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a ca voluntário'
frase = str(input())
if frase == timeout:
    vol_1 = int(input())
    vol_2 = int(input())
    vol_3 = int(input())
    vol_4 = int(input())
    vol_5 = int(input())
    soma_vol = (vol_1 + vol_2 + vol_3 + vol_4 + vol_5)
    estoque -= soma_vol
    print(estoque)



#início
estoque = 20
controle = 1

#frases
acabou = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
encham = 'Encham o cooler, vai começar um jogo!!!!'
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a ca voluntário'
intercin = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

#recebimento dos dados
while controle != 0:
  frase = str(input())
  if frase == acabou:
    sedentos = int(input())
    if estoque < sedentos:
      print(f'Não teremos água para todos os jogadores... Temos que garantir {sedentos - estoque} garrafas!!')
      estoque *= 2
    estoque -= sedentos
  if frase == encham:
    estoque += 15
    print('Geladeira cheia!')
  if frase == timeout:
    vol_1 = int(input())
    vol_2 = int(input())
    vol_3 = int(input())
    vol_4 = int(input())
    vol_5 = int(input())
    vol_total = (vol_1 + vol_2 + vol_3 + vol_4 + vol_5)
    estoque -= vol_total
    if estoque < 0:
      print(f'Prometemos distribuir {abs(estoque)} garrafas e zeramos')
  if frase == intercin:
    controle = 0
  if estoque < 0:
    print('Por questões logísticas, teremos que acabar com os jogos...')
    controle = 0

#resultado
if estoque > 0:
  print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')
elif estoque == 0:
  print('Vendemos todas as águas, fizemos uma contagem certeira!!')
else:
  print(f'Estamos devendo {abs(estoque)} garrafas para os alunos...')










'''




















'''
estoque = 20

#frases
acabou = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
encham = 'Encham o cooler, vai começar um jogo!!!!'
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário'
intercin = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

#começando
while True:
    frase = str(input())
    if frase == acabou:
        sedentos = int(input())
        if estoque >= sedentos:
            estoque -= sedentos
        else:
            print(f'Não teremos água para todos os jogadores... Temos que garantir {sedentos - estoque} garrafas!!')
            estoque += estoque
            estoque -= sedentos

    if frase == encham:
        estoque += 15
        print('Geladeira cheia!')
    if frase == timeout:
        vol_1 = int(input())
        vol_2 = int(input())
        vol_3 = int(input())
        vol_4 = int(input())
        vol_5 = int(input())
        soma_vol = vol_1 + vol_2 + vol_3 + vol_4 + vol_5
        estoque -= soma_vol
        if estoque < 0:
            print(f'Prometemos distribuir {estoque} garrafas e zeramos')

    if frase == intercin:
        break
    if estoque < 0:
        print('Por questões logísticas, teremos que acabar com os jogos...')
        break

#final
if estoque > 0:
    print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')
elif estoque == 0:
    print('Vendemos todas as águas, fizemos uma contagem certeira!!')
else:
    print(f'Estamos devendo {abs(estoque)} para os alunos')


estoque = 20
controle = 1

# frases
acabou = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
encham = 'Encham o cooler, vai começar um jogo!!!!'
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário'
intercin = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

# começando
while controle != 0:
    frase = str(input)
    if frase == acabou:
        sedentos = int(input())
        if estoque >= sedentos:
            estoque -= sedentos
        else:
            print(f'Não teremos água para todos os jogadores... Temos que garantir {sedentos - estoque} garrafas!!')
            estoque += estoque
            estoque -= sedentos

    if frase == encham:
        estoque += 15
        print('Geladeira cheia!')
    if frase == timeout:
        vol_1 = int(input())
        vol_2 = int(input())
        vol_3 = int(input())
        vol_4 = int(input())
        vol_5 = int(input())
        soma_vol = vol_1 + vol_2 + vol_3 + vol_4 + vol_5
        estoque -= soma_vol
        if estoque < 0:
            estoque = abs(estoque)
            print(f'Prometemos distribuir {estoque} garrafas e zeramos')

        if frase == intercin:
            controle = 0
        if estoque < 0:
            print('Por questões logísticas, teremos que acabar com os jogos...')
            controle = 0

# final
if estoque > 0:
    print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')
elif estoque == 0:
    print('Vendemos todas as águas, fizemos uma contagem certeira!!')
else:
    print(f'Estamos devendo {abs(estoque)} para os alunos')

estoque = 20
controle = 1

# frases
acabou = 'Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores'
encham = 'Encham o cooler, vai começar um jogo!!!!'
timeout = 'Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário'
intercin = 'O InterCIn acabou!!! Vamos ver nosso estoque de bebidas'

# começando
while controle != 0:
    frase = str(input)
    if frase == acabou:
        sedentos = int(input())
        if estoque >= sedentos:
            estoque -= sedentos
        else:
            print(f'Não teremos água para todos os jogadores... Temos que garantir {sedentos - estoque} garrafas!!')
            estoque += estoque
            estoque -= sedentos

    if frase == encham:
        estoque += 15
        print('Geladeira cheia!')
    if frase == timeout:
        vol_1 = int(input())
        vol_2 = int(input())
        vol_3 = int(input())
        vol_4 = int(input())
        vol_5 = int(input())
        soma_vol = vol_1 + vol_2 + vol_3 + vol_4 + vol_5
        estoque -= soma_vol
        if estoque < 0:
            estoque = abs(estoque)
            print(f'Prometemos distribuir {estoque} garrafas e zeramos')

    if frase == intercin:
        controle = 0
    if estoque < 0:
        print('Por questões logísticas, teremos que acabar com os jogos...')
        controle = 0

# final
if estoque > 0:
    print(f'Notícia boa: sobraram {estoque} garrafas, vamos guardar na geladeira :D')
elif estoque == 0:
    print('Vendemos todas as águas, fizemos uma contagem certeira!!')
else:
    print(f'Estamos devendo {abs(estoque)} para os alunos')
'''