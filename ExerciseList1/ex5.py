'''
5 - Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus  
Celsius e exiba o resultado.
'''

# Capitura as entradas do usuário
fahrenheit = int(input("Insira o valor da temperatura em Fahrenheit:"))

# Convert fahrenheit para Celsius
call = (fahrenheit-32)*5/9

# Mostra na tela o resutado
print(f"{fahrenheit} °F é igual a {call:.2f} °C")
