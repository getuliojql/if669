# definindo quais itens são necessários para cada profissão
itens_padeira = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
itens_personal_trainer = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']
itens_medica = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta', 'Celular']
itens_economista = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
itens_assistente_de_informatica = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']

# variáveis
controle = True
faltou_item = False

# recebendo o trabalho que a barbie achou que executaria e copiando seus itens
trabalho_achou = str(input())

if trabalho_achou == 'Padeira':
    itens_bolsa = itens_padeira.copy()

elif trabalho_achou == 'Personal Trainer':
    itens_bolsa = itens_personal_trainer.copy()

elif trabalho_achou == 'Medica':
    itens_bolsa = itens_medica.copy()

elif trabalho_achou == 'Economista':
    itens_bolsa = itens_economista.copy()

else:
    itens_bolsa = itens_assistente_de_informatica.copy()

# recebendo o trabalho que a barbie realmente irá executar e copiando seus itens
trabalho_real = str(input())

if trabalho_real == 'Padeira':
    itens_necessarios = itens_padeira.copy()

elif trabalho_real == 'Personal Trainer':
    itens_necessarios = itens_personal_trainer.copy()

elif trabalho_real == 'Medica':
    itens_necessarios = itens_medica.copy()

elif trabalho_real == 'Economista':
    itens_necessarios = itens_economista.copy()

else:
    itens_necessarios = itens_assistente_de_informatica.copy()


while controle:
    acao_barbie = str(input())

    if acao_barbie == 'Adicionar':
        item_adicionar = str(input())

        if item_adicionar in itens_necessarios:

            if item_adicionar in itens_bolsa:
                print(f'Barbie, você já colocou {item_adicionar} na bolsa')

            else:
                print(f'{item_adicionar} adicionado à bolsa')
                itens_bolsa.append(item_adicionar)

        else:
            print(f'Barbie, {item_adicionar} não esta na lista de itens de {trabalho_real}')

    elif acao_barbie == 'Retirar':
        item_retirar = str(input())

        if item_retirar in itens_bolsa:
            if item_retirar in itens_necessarios:
                print(f'Não faca isso Barbie, você precisa de {item_retirar} para trabalhar de {trabalho_real}')

            if item_retirar not in itens_necessarios:
                print(f'{item_retirar} retirado da bolsa')
                itens_bolsa.remove(item_retirar)

        else:
            print('Barbie, como você vai retirar algo que já não esta ai?')

    elif acao_barbie == 'Sair':
        print('Itens na bolsa: ', end='')
        for idx_i, i in enumerate(sorted(itens_bolsa)):
            if idx_i != len(itens_bolsa) - 1:
                print(f'{i}, ', end='')
            else:
                print(f'{i}')

        if sorted(itens_bolsa) == sorted(itens_necessarios):
            print('Boa Barbie, foi na correria mas tudo deu certo!')

        else:
            for i in itens_necessarios:
                if i not in itens_bolsa:
                    item_esquecido = i
                    print(f'Oh não!! Barbie, você esqueceu de pegar {item_esquecido}!!')

            for i in itens_bolsa:
                if i not in itens_necessarios:
                    item_errado = i
                    print(f'Barbie, você esqueceu de tirar {item_errado}, você não usa ele '
                          f'trabalhando de {trabalho_real}')

        controle = False
