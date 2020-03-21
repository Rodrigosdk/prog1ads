'''
8 -Escreva um programa que converte valores de polegadas em centímetros utilizando a seguinte fórmula:
1 polegada = 2,54cm;
'''

# Capitura as entradas do usuário
value = int(input("insira um valor: "))

# Calcula a converção de polegadas para centímetros
call = value**2.54

# Mostra na tela o resutado
print(f"Você dígito {value} polegadas e seu valor em centímetros é {call}cm")
