'''
1 - Faça um Programa que peça dois números e imprima o maior deles
'''

#variáveis
num_1 = float(input('Informe o primeiro número: '))
num_2 = float(input('Qual o segundo número: '))

#comparando o 1ª e o 2ª números e informando o maior
if num_1 > num_2:
    print(f'Você informou "{num_1:.0f} e {num_2:.0f}" e o maior entre os dois é {num_1:.0f}')
elif num_1 == num_2:
    print(f'Você informou "{num_1:.0f} e {num_2:.0f}" os números são iguais não exite maior!')
else:
    print(f'Você informou "{num_1:.0f} e {num_2:.0f}" e o maior número entre os dois é {num_2:.0f}')
