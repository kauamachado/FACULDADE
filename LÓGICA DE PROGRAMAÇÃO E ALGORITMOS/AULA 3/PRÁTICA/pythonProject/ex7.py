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


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo! ')
    else:
        a.write(f'{nomeJogo}; {nomeVideoGame}\n')
    finally:
        a.close()


def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao listar arquivos')
    else:
        print(a.read())
    finally:
        a.close()


while True:
    print('1 - CADASTRAR NOVO ITEM'
          '\n2 - LISTAR TODOS OS ITENS '
          '\n3 - SAIR')

    esc = valida('Digite a opção desejada:', 1, 3)

    if esc == 1:
        print('CADASTRO: ')
        nomeJogo = input('Nome do jogo: ')
        nomeVideoGame = input('Nome do video game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)

    elif esc == 2:
        print('CADASTRADOS')
        listarArquivo(arquivo)
    else:
        print('Goodbye')
        break
