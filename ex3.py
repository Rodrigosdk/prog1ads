'''
Atividade 3

Faça um programa que calcule a média de consumo de combustível de um veículo. 
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) 
e quantos litros foram gastos no percurso.
'''

#Capitura as entradas do usuário
start_km = int(input("Insira o km inicial: "))
end_km = int(input("Insira o km final: "))
ask_liter = float(input("Insira quantos litros foram gastos: "))

#calcular a média do usuário
cal = (end_km - start_km)/ ask_liter

#Mostra na tela o resutado
print(f"você realizou {cal:.2f}L/km")
