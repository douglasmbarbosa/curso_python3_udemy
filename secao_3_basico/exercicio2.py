#cálculo de IMC

nome = 'Douglas Barbosa'
altura = 1.70
peso = 80
imc = peso / (altura ** 2)

print('\n' + nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMc é' )
print(imc)

#f-strings

print(f'\n{nome} tem {altura:.2f} de altura,\n'
      f'pesa {peso} quilos e seu IMC é\n' 
      f'{imc:.2f}'    
) 


