'''
Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.
'''

# Recebe as entradas do usuário 
num1=int(input("digite um numero: "))
num2=int(input("digite outro numero: "))

# Cria loop
while num1 < num2-1:
    num1 += 1 
    print(num1)
    