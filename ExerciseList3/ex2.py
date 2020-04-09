'''
2 - Faça um Programa que peça um valor e mostre
na tela se o valor é positivo ou negativo
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        valor = float(input('Informe o um valor: '))

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

    # comparando se o valor informado é ou não positivo
    if valor > 0:
        print(f'O valor informado de "{valor:.0f}" é positivo')

        # Canselar o loop
        break

    elif valor == 0:
        print(
            f'O valor informado "{valor:.0f}" é zero e o zero é um valor neutro!')

        # Canselar o loop
        break

    else:
        print(f'O valor informado de "{valor:.0f}" é negativo')

        # Canselar o loop
        break
