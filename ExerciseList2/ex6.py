'''
6 - Faça um Programa que leia três números e mostre o maior deles.
'''

#variáveis
num_1 = float(input('Informe o primeiro número? '))
num_2 = float(input('Qual o segundo número? '))
num_3 = float(input('Qual o terceiro número? '))

#comparando o 1ª, 2ª e 3ª números e informando o maior
if num_1 > num_2 and num_1 > num_3:
    print(f'Dos números informados o "{num_1:.0f}" é o maior deles')
elif num_2 > num_1 and num_2 > num_3:
    print(f'Dos números informados o "{num_2:.0f}" é o maior deles')
else:
    print(f'Dos números informados o "{num_3:.0f}" é o maior deles')
