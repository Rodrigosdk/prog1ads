'''
6 - Faça um Programa que leia três números e mostre o maior deles.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        number_1 = float(input('Informe o primeiro número? '))
        number_2 = float(input('Qual o segundo número? '))
        number_3 = float(input('Qual o terceiro número? '))

    # Tratamento de erros com valor de argumento inadequado
    except ValueError:
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Só é permitido números e pontos{}".format(
            '\033[31m', '\033[m').center(80))

        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # comparando o 1ª, 2ª e 3ª números e informando o maior
    if number_1 > number_2 and number_1 > number_3:
        print(f'Dos números informados o "{number_1:.0f}" é o maior deles')

        # Canselar o loop
        break

    elif number_2 > number_1 and number_2 > number_3:
        print(f'Dos números informados o "{number_2:.0f}" é o maior deles')

        # Canselar o loop
        break

    else:
        print(f'Dos números informados o "{number_3:.0f}" é o maior deles')

        # Canselar o loop
        break
