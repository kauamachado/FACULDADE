print(' + ADIÇÃO'
      '\n - SUBTRAÇÂO'
      '\n * MULTIPLICAÇÃO'
      '\n / DIVISÃO')
op = str(input('Digite o operador que você quer: '))

if op == '+':
    v1 = float(input('1º valor:'))
    v2 = float(input('2º valor: '))
    resultado = v1 + v2
    print(f'O número {v1} somado por {v2} é {resultado}')
elif op == '-':
    v1 = float(input('1º valor:'))
    v2 = float(input('2º valor: '))
    resultado = v1 - v2
    print(f'O número {v1} subtraido por {v2} é {resultado}')
elif op == '*':
    v1 = float(input('1º valor:'))
    v2 = float(input('2º valor: '))
    resultado = v1 * v2
    print(f'O número {v1} multiplicado por {v2} é {resultado}')
elif op == '/':
    v1 = float(input('1º valor:'))
    v2 = float(input('2º valor: '))
    resultado = v1 / v2
    print(f'O número {v1} dividido por {v2} é {resultado}')
else:
    print('Digite uma tecla válida! ')
    exit()
