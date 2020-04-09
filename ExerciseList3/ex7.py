'''
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        num_1 = float(input('Informe o primeiro número: '))
        num_2 = float(input('Qual o segundo número: '))
        num_3 = float(input('Qual o terceiro número: '))

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

    # Comparando o 1ª, 2ª e 3ª números e informando o maior e o menor
    if num_1 > num_2 and num_2 > num_3:
        print(f'Dos números informados o "{num_1}" é o maior deles')
        print(f'Dos números informados o "{num_3}" é o menor deles')

        # Canselar o loop
        break

    # Comparando o 1ª, 3ª e 2ª números e informando o maior e o menor
    elif num_1 > num_3 and num_3 > num_2:
        print(f'Dos números informados o "{num_1}" é o maior deles')
        print(f'Dos números informados o "{num_2}" é o menor deles')

        # Canselar o loop
        break

    # Comparando o 2ª, 1ª e 3ª números e informando o maior e o menor
    elif num_2 > num_1 and num_1 > num_3:
        print(f'Dos números informados o "{num_2}" é o maior deles')
        print(f'Dos números informados o "{num_3}" é o menor deles')

        # Canselar o loop
        break

    # Comparando o 2ª, 3ª e 1ª números e informando o maior e o menor
    elif num_2 > num_3 and num_3 > num_1:
        print(f'Dos números informados o "{num_2}" é o maior deles')
        print(f'Dos números informados o "{num_1}" é o menor deles')

        # Canselar o loop
        break

    # Comparando o 3ª, 2ª e 1ª números e informando o maior e o menor
    elif num_3 > num_2 and num_2 > num_1 or num_3 > num_1 and num_1 > num_2:
        print(f'Dos números informados o "{num_3}" é o maior deles')
        print(f'Dos números informados o "{num_1}" é o menor deles')

        # Canselar o loop
        break

    # Comparando o 3ª, 1ª e 2ª números e informando o maior e o menor
    elif num_3 > num_1 and num_1 > num_2:
        print(f'Dos números informados o "{num_3}" é o maior deles')
        print(f'Dos números informados o "{num_2}" é o menor deles')

        # Canselar o loop
        break
    else:
        print(f'Dos números informados dois ou mais números são iguais.')

        # Canselar o loop
        break
