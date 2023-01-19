nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if len(nome) == 0 or len(idade) == 0:
    print('Desculpa, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1:-(len(nome)+1):-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome não contém espaços!')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]} ')
    print(f'A última letra do seu nome é {nome[-1]} ')