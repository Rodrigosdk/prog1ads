'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        num_1 = int(input('Informe o primeiro número: '))
        num_2 = int(input('Informe o segundo número: '))
        num_3 = int(input('Informe o terceiro número: '))

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

    # mostrando os 1ª, 2ª e 3ª números em ordem decrescente

    if num_1 == num_2 == num_3:
        print(f'{num_1}, {num_2} e {num_3}')
    else:
        if num_1 < num_2 < num_3:
            print(f'{num_3}, {num_2} e {num_1}')

            # Canselar o loop
            break
        
        elif num_1 < num_3 and num_3 > num_2:
            print(f'{num_3}, {num_1} e {num_2}')
        
            # Canselar o loop
            break
        
        elif num_2 > num_1 and num_1 > num_3:
            print(f'{num_2}, {num_1} e {num_3}')
        
            # Canselar o loop
            break
        
        elif num_2 > num_3 and num_3 > num_1:
            print(f'{num_2}, {num_3} e {num_1}')
        
            # Canselar o loop
            break
        
        elif num_1 > num_3 and num_3 < num_2:
            print(f'{num_1}, {num_2} e {num_3}')
        
            # Canselar o loop
            break
        
        elif num_1 > num_2 and num_2 < num_3:
            print(f'{num_1}, {num_3} e {num_2}')
        
            # Canselar o loop
            break
