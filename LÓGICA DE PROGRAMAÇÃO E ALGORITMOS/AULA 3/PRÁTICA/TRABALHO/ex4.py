listaPecas = []
def cadastrarPeca(codigo):
  print('Você selecionou a opção de Cadastrar Peça')
  print('O código da peça é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome da peça:')
  fabricante = input('Entre com o fabricante da peça:')
  valor = float(input('Entre com o valor R$ da peça:'))
  dicionarioPecas = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaPecas.append(dicionarioPecas.copy())
def consultarPeca():
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Peças')
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas as Peças\n2- Consultar Peças por Código\n3- Consultar Peças por Fabricante\n4- Retornar\n-->'))
      if opConsultar == 1:
        print('-' * 20)
        for pecas in listaPecas:
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 2:
        print('Você Selecionou a Opção Peças por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['codigo'] == entrada):
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 3:
        print('Você Selecionou a Opção Peças por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['fabricante'] == entrada):
            for key, value in pecas.items():
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
def removerPeca():
    print('Você Selecionou o Remover Peça')
    entrada = int(input('Digite o Código da peça que irá remover: '))
    for pecas in listaPecas:
      if(pecas['codigo'] == entrada):
        listaPecas.remove(pecas)
    else:
      print('Você removeu o código.')
print('Bem-vindo ao Controle de Estoque da Mercearia de Kaua Machado')
registroPecas = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar Pecas\n2- Consultar Pecas\n3- Remover Pecas\n4- Sair\n-->'))
      if opcao == 1:
        registroPecas = registroPecas + 1
        cadastrarPeca(registroPecas)
      elif opcao == 2:
        consultarPeca()
      elif opcao == 3:
        removerPeca()
      elif opcao == 4:
        print('Programa finalizado')
        break
      else:
        print('Digite somente uma das opções do MENU')
        continue
    except ValueError:
        print('Pare de digitar números que não existe...')