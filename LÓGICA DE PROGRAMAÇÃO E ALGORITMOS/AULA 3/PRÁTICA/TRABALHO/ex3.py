def volumeFeijoada():
    while True:
        try:
            v = 0
            qtd = int(input('Digite a quantidade desejada (ml): '))
            if qtd < 300 or qtd > 5000:
                qtd = int(input('Digite a quantidade desejada (ml): '))
            else:
                v = qtd * 0.08
                return v
        except ValueError:
            print('Digite um valor válido. ')


def opcaoFeijoada():
    print('Entre com a opção desejada:'
          '\nB - Basica (Feijão + paiol + costelinha)'
          '\nP - Premium (Feijão + paiol + costelinha + partes de porco)'
          '\nS - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
    escolha = input('').upper()
    while True:
        if escolha == 'B':
            return escolha
        elif escolha == 'P':
            return escolha
        elif escolha == 'S':
            return escolha
        else:
            print('Digite um valor válido. ')
            print('Entre com a opção desejada:'
                  '\nB - Basica (Feijão + paiol + costelinha)'
                  '\nP - Premium (Feijão + paiol + costelinha + partes de porco)'
                  '\nS - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
            escolha = input().upper()


def acompanhamentoFeijoada():
    valorAc = 0
    print('0- Não desejo mais acompanhamentos (encerrar pedido)'
          '\n1- 200g de arroz'
          '\n2- 150g de farofa especial'
          '\n3- 100g de couve cozida'
          '\n4- 1 laranja descascada')
    opc = int(input(''))

    while opc != 0:
        print('0- Não desejo mais acompanhamentos (encerrar pedido)'
              '\n1- 200g de arroz'
              '\n2- 150g de farofa especial'
              '\n3- 100g de couve cozida'
              '\n4- 1 laranja descascada')
        opc = int(input(''))
        if opc == 1:
            total = valorAc + 5
        elif opc == 2:
            total = valorAc + 6
        elif opc == 3:
            total = valorAc + 7
        elif opc == 4:
            total = valorAc + 3
        return total


# print('BEM VINDO A FEIJOADA DE KAUÃ MACHADO!!')
# print('MENU: ')
# volumeFeijoada()
# opcaoFeijoada()
acompanhamentoFeijoada()
