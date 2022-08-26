def valida(pergunta, min, max):
    esc = int(input(pergunta))
    while (esc < min) or (esc > max):
        esc = int(input(pergunta))
    return esc


while True:
    print('1 - CADASTRAR NOVO ITEM'
          '\n2 - LISTAR TODOS OS ITENS '
          '\n3 - SAIR')

    esc = valida('Digite a opção desejada:', 1, 3)

    if esc == 1:
        print('')
    elif esc == 2:
        print('')
    else:
        print('Goodbye')
        break
