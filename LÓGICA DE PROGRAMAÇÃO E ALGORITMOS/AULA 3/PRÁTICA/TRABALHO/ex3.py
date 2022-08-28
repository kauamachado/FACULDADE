def volumeFeijoada():
    global v
    while True:
        try:
            v = 0
            qtd = int(input('Digite a quantidade desejada (ml): '))
            if qtd < 300 or qtd > 5000:
                print('Não aceitamos valores menores que 300 ou maiores que 5000')
                qtd = int(input('Digite a quantidade desejada (ml): '))
            else:
                v = qtd * 0.08
        except ValueError:
            print('Digite um valor numérico. ')
            continue
        return v



def opcaoFeijoada():
    global totalOpc
    v = 1
    print('Entre com a opção desejada:'
          '\nB - Basica (Feijão + paiol + costelinha)'
          '\nP - Premium (Feijão + paiol + costelinha + partes de porco)'
          '\nS - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
    escolha = input('').upper()
    while True:
        if escolha == 'B':
            totalOpc = v * 1
        elif escolha == 'P':
            totalOpc = v * 1.25
        elif escolha == 'S':
            totalOpc = v * 1.5
        else:
            print('Digite um valor válido. ')
            print('Entre com a opção desejada:'
                  '\nB - Basica (Feijão + paiol + costelinha)'
                  '\nP - Premium (Feijão + paiol + costelinha + partes de porco)'
                  '\nS - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
            escolha = input().upper()
            continue
        return totalOpc


def acompanhamentoFeijoada():
    v1 = v2 = v3 = v4 = 0
    valorAc = 0
    global totalAdc
    while True:
        print('0- Não desejo mais acompanhamentos (encerrar pedido)'
              '\n1- 200g de arroz'
              '\n2- 150g de farofa especial'
              '\n3- 100g de couve cozida'
              '\n4- 1 laranja descascada')
        opc = int(input(''))
        if opc == 1:
            v1 = valorAc + 5
            print('200g de arroz foram adicionadas! ')
            continue
        elif opc == 2:
            v2 = valorAc + 6
            print('150g de farofa especial foram adicionadas! ')
            continue
        elif opc == 3:
            v3 = valorAc + 7
            print('100g de couve foram adicionadas! ')
            continue
        elif opc == 4:
            v4 = valorAc + 4
            print('1 (uma) laranja foi adicionada! ')
            continue
        if opc < 0 or opc > 4:
            print('Digite uma opção entre 0 e 4')
            continue
        totalAdc = v1 + v2 + v3 + v4
        return totalAdc


print('BEM VINDO A FEIJOADA DE KAUÃ MACHADO!!')
print('MENU: ')
volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
soma = (v * totalOpc) + totalAdc
print(f'O total a pagar é {soma}. Volume = {v} * opção = {totalOpc} + acompanhamento = {totalAdc} ')
