def tela_informacoes(nome, propulsores, vel_inicio, vel_fim):
    print(f'--- Participante: {nome} ---')
    print(f'Qtd de propulsores Final: {propulsores}')
    print(f'Velocidade Inicial: {vel_inicio} km/h')
    print(f'Velocidade Final: {vel_fim} km/h')


acabou = False
proximo = True
participantes = 0
desclassificados = 0

frase_pitstop = 'Pit-Stop Espacial'
frase_bateu = 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.'
frase_desclassificado = 'Opa esse participante não está inscrito, desclassificando em 3, 2, 1...'

while not acabou:

    if proximo:
        informacoes_participante = str(input()).split(' ')
        informacoes_participante[1] = int(informacoes_participante[1])
        informacoes_participante[2] = int(informacoes_participante[2])
        velocidade_inicial = informacoes_participante[1] * informacoes_participante[2]
        proximo = False

    situacao = str(input())

    if situacao == frase_pitstop:
        informacoes_participante[1] += 1

    elif situacao == frase_bateu:
        informacoes_participante[1] -= 1

    if informacoes_participante[1] <= 0:
        desclassificados += 1
        print(f'BUUMM!! Infelizmente, {informacoes_participante[0]} está fora da corrida.')
        proximo = True

    else:

        if situacao == frase_desclassificado:
            desclassificados += 1
            print(f'O {informacoes_participante[0]} achou que não descobriríamos, '
                  f'tirem {informacoes_participante[0]} imediatamente da pista.')
            proximo = True

        elif situacao == 'Próximo' or situacao == 'FIM':
            velocidade_final = informacoes_participante[1] * informacoes_participante[2]
            tela_informacoes(informacoes_participante[0], informacoes_participante[1],
                             velocidade_inicial, velocidade_final)
            participantes += 1

            if situacao == 'Próximo':
                proximo = True

            elif situacao == 'FIM':
                acabou = True

if desclassificados < participantes:
    print(f'Relatório da CIn Pod Race: {participantes} participantes terminaram a corrida '
          f'e {desclassificados} foram desclassificados.')

else:
    print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')
