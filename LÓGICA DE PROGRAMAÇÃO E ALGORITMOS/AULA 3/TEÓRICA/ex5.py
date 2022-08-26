escolha = int(input('Qual fruta você quer comprar?'
                    '\n1 - Banana'
                    '\n2 - Maçã'
                    '\n3 - Laranja'
                    '\n'))
if escolha > 3 or escolha < 1:
    print('Produto inexistente')
    exit()
quantidade = int(input('Digite a quantidade: '))

valor = 0


if escolha == 1:
    valor = 1.85 * quantidade
else:
    if escolha == 2:
        valor = 2.30 * quantidade
    else:
        if escolha == 3:
            valor = 3.60 * quantidade
print(f'O valor total a pagar é {valor}')
