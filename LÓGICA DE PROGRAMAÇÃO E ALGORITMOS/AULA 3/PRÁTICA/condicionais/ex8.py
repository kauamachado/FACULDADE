kw = int(input('Digite a quantidade de kwh: '))
print('R - RESIDENCIAL'
      '\nC - COMERCIAL'
      '\nI - INDUSTRIAL')
valor = 0
tipo = str(input('Tipo:'))
if tipo == 'r' or tipo == 'R':
    if kw < 500:
        valor = kw * 0.40
        print(f'A quantidade de kWh gastos foram {kw}, do tipo residencial e o valor total foi {valor}')
    else:
        valor = kw * 0.65
        print(f'A quantidade de kWh gastos foram {kw}, do tipo residencial e o valor total foi {valor}')
elif tipo == 'C' or tipo == 'c':
    if kw <= 1000:
        valor = kw * 0.55
        print(f'A quantidade de kWh gastos foram {kw}, do tipo comercial e o valor total foi {valor}')
    else:
        valor = kw * 0.60
        print(f'A quantidade de kWh gastos foram {kw}, do tipo comercial e o valor total foi {valor}')
elif tipo == 'I' or tipo == 'i':
    if kw <= 5000:
        valor = kw * 0.55
        print(f'A quantidade de kWh gastos foram {kw}, do tipo industrial e o valor total foi {valor}')
    else:
        valor = kw * 0.60
        print(f'A quantidade de kWh gastos foram {kw}, do tipo industrial e o valor total foi {valor}')
else:
    print('Digito invalido')
exit()
