'''

5 -Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:

a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve 
fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o 
programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import os

def roots(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    if D >0:
        print("A equação não possui raizes reais")
    elif D == 0:
        print("Delta possui apenas uma raiz real")
        print(f'Valor de x1: {x1}')
    else:
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')

while True:
    try:
        # Capitura as entradas do usuário
        valueA = float(input("Insira o valor de A: "))
        if  valueA == 0:
            print("O valor de A não pode ser nulo")
        valueB = float(input("Insira o valor de B: "))
        valueC = float(input("Insira o valor de C: "))

        roots(valueA,valueB,valueC)
        
        # Canselar o loop
        break
    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: Erro: só é permitido números e pontos {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

