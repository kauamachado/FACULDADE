def valida(pergunta, min, max):
    esc = int(input(pergunta))
    while (esc < min) or (esc > max):
        esc = int(input(pergunta))
    return esc


def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo. ')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso')


def existeArquivos(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


arquivo = 'games.txt'
if existeArquivos(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente. ')
    criaArquivo(arquivo)
while True:
    print('1 - CADASTRAR NOVO ITEM'
          '\n2 - LISTAR TODOS OS ITENS '
          '\n3 - SAIR')

    esc = valida('Digite a opção desejada:', 1, 3)

    if esc == 1:
        print('Opçãod de cadastrar novo item.')
    elif esc == 2:
        print('Opção de listar os itens')
    else:
        print('Goodbye')
        break
