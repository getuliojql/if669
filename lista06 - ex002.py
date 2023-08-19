registro_geral = {}
qtd_pessoas = int(input())

for n in range(qtd_pessoas):
    pessoa = str(input()).split(' - ')

    registro_geral['nome'] = pessoa[0]
    registro_geral['nota'] = pessoa[1]
    registro_geral['categoria'] = pessoa[2]