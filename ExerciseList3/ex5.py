'''

5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        side1 = float(input("Insira o valor um lado 1: "))
        side2 = float(input("Insira o valor um lado 2: "))
        side3 = float(input("Insira o valor um lado 3: "))

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
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Lados nulos ou negativos nao sao aceitos.")

        # Canselar o loop
        break

    if side1 >= side2+side3 or side2 >= side3+side1 or side3 >= side1+side2:
        print("Triangulo inexistente.")

        # Canselar o loop
        break

    if side1 == side2 and side2 == side3:
        print("Triangulo equilatero.")

        # Canselar o loop
        break

    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Triangulo isosceles.")

        # Canselar o loop
        break
    else:
        print("Triangulo escaleno.")

        # Canselar o loop
        break
