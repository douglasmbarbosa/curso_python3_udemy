"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = (input("Digite um número inteiro: "))
validacao_numero = numero.isdigit()

if validacao_numero:
    numero = int(numero)
    numero_par = (numero % 2 == 0)
    if numero_par:
        print("Esse número é par!")
    else:
        print("Esse número é ímpar!") 
else:
    print("Você não digitou um número inteiro!")
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = int(input("Digite o horário atual: "))

if horario >= 0 and horario <=11:
    print("Bom dia!")
elif horario > 11 and horario <=17:
    print("Boa tarde!")
elif horario > 17 and horario < 24:
    print("Boa noite!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite o seu primeiro nome: ")

if len(nome) < 5:
    print("Seu nome é curto")
elif len(nome) < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")