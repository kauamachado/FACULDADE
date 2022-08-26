print('Bem vindo a loja do Kauã Daniel Lopes Machado')

valor_produto = float(input('Digite o valor do produto: '))

qtd_produto = int(input('Digite a quantidade: '))

valor_total = valor_produto * qtd_produto

if 4 >= qtd_produto > 0:
    print(f'Valor total sem desconto: R$ {valor_total:.2f}')
    print(f'Valor total com desconto: R${valor_total:.2f} (0% de desconto)')

elif 5 <= qtd_produto <= 19:
    valor_desc = valor_total - (valor_total * 3 / 100)
    print(f'Valor total sem desconto: R$ {valor_total:.2f}')
    print(f'Valor total com desconto: R${valor_desc:.2f} (3% de desconto)')

elif 20 <= qtd_produto <= 99:
    valor_desc = valor_total - (valor_total * 6 / 100)
    print(f'Valor total sem desconto: R$ {valor_total:.2f}')
    print(f'Valor total com desconto: R${valor_desc:.2f} (6% de desconto)')

elif qtd_produto >= 100:
    valor_desc = valor_total - (valor_total * 10 / 100)
    print(f'Valor total sem desconto: R$ {valor_total:.2f}')
    print(f'Valor total com desconto: R${valor_desc:.2f} (10% de desconto)')

else:
    print('Digite um número válido')