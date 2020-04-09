'''
1 - Faça um Programa que peça dois números e imprima o maior deles
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        num_1 = float(input('Informe o primeiro número: '))
        num_2 = float(input('Qual o segundo número: '))

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

    # comparando o 1ª e o 2ª números e informando o maior
    if num_1 > num_2:
        print(
            f'Você informou "{num_1:.0f} e {num_2:.0f}" e o maior entre os dois é {num_1:.0f}')

        # Canselar o loop
        break
    elif num_1 == num_2:
        print(
            f'Você informou "{num_1:.0f} e {num_2:.0f}" os números são iguais não exite maior!')

        # Canselar o loop
        break
    else:
        print(
            f'Você informou "{num_1:.0f} e {num_2:.0f}" e o maior número entre os dois é {num_2:.0f}')

        # Canselar o loop
        break
