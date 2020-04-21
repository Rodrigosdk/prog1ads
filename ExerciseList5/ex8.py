'''
Faça um programa que leia 5 números e informe a soma e a média dos números
'''
# Cria contador
cont = 1
sum_number = 0

# Cria loop 
while cont <= 5:
    # Recebe a entrada do usuário 
    number = int(input("Informe um número: "))
    
    #calcula as entradas
    sum_number += number
    media = sum_number/5
    
    # Adiciona mais um ao contador 
    cont += 1

print(media)
