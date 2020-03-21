'''
4- Receba do usuário o ano em que estamos, e o ano que ele nasceu, e calcule sua idade
'''

# Capitura as entradas do usuário
year = float(input("Em qual ano estamos: "))
was_born = float(input("Em qual você nasceu: "))

# Calcula idade
call = year-was_born

# Mostra na tela o resutado
print(f"sua idade é {call}")
