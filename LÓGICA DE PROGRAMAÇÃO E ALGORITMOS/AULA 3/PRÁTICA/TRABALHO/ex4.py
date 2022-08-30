listaprodutos = []
def cadastrarProduto(codigo):
  print('Você selecionou a opção de Cadastrar produto')
  print('O código da produto é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome da produto:')
  fabricante = input('Entre com o fabricante da produto:')
  valor = float(input('Entre com o valor R$ da produto:'))
  dicionarioprodutos = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaprodutos.append(dicionarioprodutos.copy())
def consultarproduto():
  while True:
    try:
      print('Você Selecionou a Opção de Consultar produtos')
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas as produtos\n2- Consultar produtos por Código\n3- Consultar produtos por Fabricante\n4- Retornar\n-->'))
      if opConsultar == 1:
        print('-' * 20)
        for produtos in listaprodutos:
            for key, value in produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 2:
        print('Você Selecionou a Opção produtos por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for produtos in listaprodutos:
          if(produtos['codigo'] == entrada):
            for key, value in produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 3:
        print('Você Selecionou a Opção produtos por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for produtos in listaprodutos:
          if(produtos['fabricante'] == entrada):
            for key, value in produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 4:
        break
      else:
        print('Por favor digite somente o que pede')
        continue
    except ValueError:
      print('Por Favor pare de digitar números que não existe...')
      continue
def removerproduto():
    print('Você Selecionou o Remover produto')
    entrada = int(input('Digite o Código da produto que irá remover: '))
    for produtos in listaprodutos:
      if(produtos['codigo'] == entrada):
        listaprodutos.remove(produtos)
    else:
      print('Você removeu o código.')
print('Bem-vindo ao Controle de Estoque da mercearia Kauã Machado')
registroprodutos = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar produtos\n2- Consultar produtos\n3- Remover produtos\n4- Sair\n-->'))
      if opcao == 1:
        registroprodutos = registroprodutos + 1
        cadastrarProduto(registroprodutos)
      elif opcao == 2:
        consultarproduto()
      elif opcao == 3:
        removerproduto()
      elif opcao == 4:
        print('Programa finalizado')
        break
      else:
        print('Digite somente uma das opções do MENU')
        continue
    except ValueError:
        print('Pare de digitar números que não existe...')