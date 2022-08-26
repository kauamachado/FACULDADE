# print('FOR')
# for c in range(3, 13):
#  print(c)

# c = 2

# print('WHILE ')
# while c <13:
#  c +=1
# print(c)

# for c in range(0, 9, 2):
#    print(c)
# EX 2
# c = 0
# while c < 9:
#   print(c)
#   c += 2


print(' + ADIÇÃO'
      '\n - SUBTRAÇÂO'
      '\n * MULTIPLICAÇÃO'
      '\n / DIVISÃO')
op = str(input('Digite o operador que você quer: '))
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('1º valor: '))
    y = int(input('2º valor: '))

while True:
    if op == '+':
        resultado = x + y
        print(f'O número {x} somado por {y} é {resultado}')
    elif op == '-':
        resultado = x - y
        print(f'O número {x} subtraido por {y} é {resultado}')
    elif op == '*':
        resultado = x * y
        print(f'O número {x} multiplicado por {y} é {resultado}')
    elif op == '/':
        resultado = x / y
        print(f'O número {x} dividido por {y} é {resultado}')
    elif op == 's':
        break
    else:
        print('INVÁLIDO')
    op = str(input('Digite o operador que você quer: '))

    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('1º valor: '))
        y = int(input('2º valor: '))


print('Adeus')
