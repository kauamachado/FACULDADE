cont = 1
i3 = 0
i12 = 0
i30 = 0
total = 0
valor = int
while True:
    idade = int(input('Digite sua idade [0 para finalizar]: '))
    if idade == 0:
        print(f'Foram comprado {cont - 1} ingressos')
        break
    cont += 1

    if idade < 3:
        i3 += 1
        valor = 0
    elif idade >= 3 and idade <= 12:
        i12 += 1
        valor = 15
    else:
        i30 += 1
        valor = 30
    total = (i3 * 0) + (15 * i12) + (i30 * 30)
    media = total / (i3 + i12 + i30)
print(f'O total de dinheiro arrecadado foi: {total}. E a média foi: {media}')
