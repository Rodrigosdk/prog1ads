'''
Atividade 5

Faça um programa que calcule o valor a ser pago por uma dívida em atraso. 
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade
de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
'''

#Capitura as entradas do usuário
ask_debt = float(input("Valor da divida: "))
ask_day = int(input("Quantidade de dias em atraso: "))
ask_interest = float(input("Valor da multa por dia de atraso: "))

#calcula o valor a ser pago por uma dívida em atraso
cal = (ask_interest*ask_day) + ask_debt 

#Mostra na tela o resutado
print(f"O valor a ser pago é de R$ {cal}")
