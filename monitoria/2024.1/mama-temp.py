equipamentos_disponiveis = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis', 'Adaga Katoptris']

nome_equipamento = ''
nao_deseja = []
lista = []

while nome_equipamento != 'Parar' :
  nome_equipamento = input()
  if nome_equipamento != 'Parar':
      lista.append([nome_equipamento])
print(lista)
