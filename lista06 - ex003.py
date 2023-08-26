# definindo função que avalia se há possibilidade de formar filas
def avaliar(lista):
    possivel = 'YES'

    lista = [int(n) for n in lista]

    for numeral in lista:
        if numeral != 0 and numeral - 1 not in lista:
            possivel = 'NO'

        if lista.count(numeral) < lista.count(numeral + 1):
            possivel = 'NO'

    return possivel


# registrando todas as possíveis frases em um dicionário
frases = {"Oooh look at him": '0',
          "Baseball bat": '1',
          "Aesthetic": '2',
          "Fake Natty": '3',
          "Chris Bumbstead, o CBUM": '4',
          "Pope Francis": '5',
          "O suco vicia": '6',
          "I don't know you tell me": '7',
          "Não é mesmo?": '8',
          "Rodrigo Goes out": '9'}

# criando uma lista para guardar os números e recebendo quantas pessoas "falarão"
numeros = []
concatenar = 0
qtd_pessoas = int(input())

# recebendo as frases e guardando os respectivos números na lista
for _ in range(qtd_pessoas):
    entrada = str(input()).split('+')

    for idx_frase, frase in enumerate(entrada):
        if idx_frase == 0:
            numeros.append(frases[frase])

        else:
            numeros.append(f'+{frases[frase]}')

# unindo os números se houverem frases concatenadas
while concatenar < len(numeros):
    concatenar = 0

    for idx_numero, numero in enumerate(numeros):
        if '+' in numero:
            numeros.insert(idx_numero, numeros[idx_numero - 1] + numero[1:])

            numeros.pop(idx_numero + 1)
            numeros.pop(idx_numero - 1)

    for numero in numeros:
        if '+' not in numero:
            concatenar += 1

# imprimindo se é possível formar filas com os números informados
print(avaliar(numeros))
