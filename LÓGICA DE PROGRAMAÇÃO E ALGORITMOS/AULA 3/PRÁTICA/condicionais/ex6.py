l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 > 0 and l2 > 0 and l3 > 0:
    if (l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2):
        if (l1 != l2) and (l2 != l3) and (l1 != l3):
            print('triangulo escaleno. ')
        else:
            if l1 == l2 and l2 == l3:
                print('triangulo equilatero')
            else:
                print('triangulo isoceles')
    else:
        print('Ao menos um dos valores indicados nao servem pra formar um triangulo. ')
else:
    print('Ao menos um dos valores indicados nao servem pra formar um triangulo. ')
