'''
8 - Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

#variáveis
prod_1 = float(input('Informe o primeiro preço? R$ '))
prod_2 = float(input('Qual o segundo preço? R$ '))
prod_3 = float(input('Qual o terceiro preço? R$ '))

#comparando os preços 1ª, 2ª e 3ª informando o mais barato a ser comprado

if prod_1 == prod_2 == prod_3:
    print('Todos os preços são iguais!!')
else:
    if prod_1 < prod_2 < prod_3:
        print('O produto 1 é os mais baratos!!')
    elif prod_1 == prod_2 < prod_3:
        print('O produto 1 e 2 são os mais baratos!!')
    elif prod_1 == prod_3 < prod_2:
        print('O produto 1 e 3 são os mais baratos!!')
    if prod_2 < prod_1 < prod_3:
        print('O produto 2 é os mais baratos!!')
    elif prod_2 == prod_3 < prod_1:
        print('O produto 2 e 3 são os mais baratos!!')
    if prod_3 < prod_2 < prod_1:
        print('O produto 3 é os mais baratos!!')
