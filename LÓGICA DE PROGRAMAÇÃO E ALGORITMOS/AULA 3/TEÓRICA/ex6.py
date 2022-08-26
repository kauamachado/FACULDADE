fruta = int(input('Escolha:'
                  '\n1 - Maçã'
                  '\n2 - Laranja'
                  '\n3 - Banana'))
qtd = int(input('Quantidade: '))
valor = 0
if fruta == 1:
    nome = str('Maçã')
    valor = 2.30 * qtd
elif fruta == 2:
    nome = str('laranjas')
    valor = 3.60 * qtd
elif fruta == 3:
    nome = str('Bananas')
    valor = 1.85 * qtd

print(f'Você comprou {qtd} {nome}. O valor total é: {valor}')
