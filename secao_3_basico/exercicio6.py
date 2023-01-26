# iterando strings com while

nome = "Douglas Barbosa"

TAMANHO_NOME = len(nome)
iterador = 0
nova_string = ''
while iterador < TAMANHO_NOME:
    nova_string += f"*{nome[iterador]}"
    iterador +=1
print(f'{nova_string}')