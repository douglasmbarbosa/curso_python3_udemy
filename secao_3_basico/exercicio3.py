# verificar se um número é maior que outro

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')