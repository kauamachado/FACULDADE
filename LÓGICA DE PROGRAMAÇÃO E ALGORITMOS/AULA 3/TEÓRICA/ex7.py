nome = str(input('Nome: '))
idade = int(input('Idade: '))

if nome == 'vinicius':
    print(f'O nome é {nome}')
elif idade < 18:
        print(f'Você não é Vinicius e é menor de idade.')
elif idade > 100:
        print('Essa pessoa provavelmente não existe.')
