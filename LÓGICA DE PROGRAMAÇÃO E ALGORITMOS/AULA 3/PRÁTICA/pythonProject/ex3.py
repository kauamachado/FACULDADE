x = int(input('Digite um valor: '))

if x >= 100:
    ced100 = x // 100
    x -= ced100 * 100
    print(f'Cedulas de R$100,00: {ced100}')
if x >= 50:
    ced50 = x // 50
    x -= ced50 * 50
    print(f'Cedulas de R$50,00: {ced50}')
if x >= 20:
    ced20 = x // 20
    x -= ced20 * 20
    print(f'Cedulas de R$20,00: {ced20}')
if x >= 10:
    ced10 = x // 10
    x -= ced10 * 10
    print(f'Cedulas de R$10,00: {ced10}')
if x >= 5:
    ced5 = x // 5
    x -= ced5 * 5
    print(f'Cedulas de R$5,00: {ced5}')
if x >= 1:
    ced1 = x // 1
    x -= ced1 * 1
    print(f'Cedulas de R$1,00: {ced1}')

