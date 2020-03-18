'''
2 - Faça um Programa que peça um valor e mostre
na tela se o valor é positivo ou negativo
'''

#variáveis
valor = float(input('Informe o um valor: '))

#comparando se o valor informado é ou não positivo
if valor > 0:
    print(f'O valor informado de "{valor:.0f}" é positivo')
elif valor == 0:
    print(f'O valor informado "{valor:.0f}" é zero e o zero é um valor neutro!')
else:
    print(f'O valor informado de "{valor:.0f}" é negativo')
