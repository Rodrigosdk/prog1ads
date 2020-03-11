'''
Atividade 10

Faça um programa que calcula o novo valor do salário de um funcionário. 
O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
'''

#Capitura as entradas do usuário
value_salary = float(input("Insira o valor do seu salário: "))
value_readjustment = float(input("Insira o percentual de reajuste salarial: "))

#Calcula o novo valor do salário
cal = value_salary + (value_salary * value_readjustment/100)

#Mostra na tela o resutado
print(f"Seu salrio será {cal}")