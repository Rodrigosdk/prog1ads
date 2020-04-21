'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
cont =  1

# Cria loop
while cont != 50:
    # Valida entradas 
    if cont%2:
        print(cont, 'é ímpar')
    
    # Adicona mais um ao contador    
    cont += 1
