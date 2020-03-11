'''
Atividade 1

Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) 
e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de 
combustível o usuário obterá com esses valores.
'''

#Capitura as entradas do usuário
ask_liter = float(input("Insira o valor do litro da gasolina: "))
ask_for_value = float(input("Insira o valor de quanto deseja abasticer: "))

#calcular a quantidades de litros
cal = ask_for_value/ask_liter

#Mostra na tela o resutado
print(f"Com R${ask_liter} o veículo receber {cal:.2f} litros ")
