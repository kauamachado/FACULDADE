print('Bem-vindo ao programa de feijoada de Kauã Daniel. ')
print('Menu: ')
qtd = float(input('Digite a quantidade em ml que deseja: '))
while qtd < 300 or qtd > 5000:
    print('Não aceitamos porções menores que 300ml ou 5l. Tente novamente. ')
    qtd = float(input('Digite a quantidade em ml que deseja: '))