'''
8 - Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        prod_1 = float(input('Informe o primeiro preço: '))
        prod_2 = float(input('Qual o segundo preço: '))
        prod_3 = float(input('Qual o terceiro preço: '))

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

    # comparando os preços 1ª, 2ª e 3ª informando o mais barato a ser comprado
    if prod_1 == prod_2 == prod_3:
        print('Todos os preços são iguais!!')
        # Canselar o loop
        break

    else:
        if prod_1 < prod_2 < prod_3:
            print('O produto 1 é os mais baratos!!')

            # Canselar o loop
            break

        elif prod_1 == prod_2 < prod_3:
            print('O produto 1 e 2 são os mais baratos!!')
            
            # Canselar o loop
            break

        elif prod_1 == prod_3 < prod_2:
            print('O produto 1 e 3 são os mais baratos!!')
            
            # Canselar o loop
            break

        if prod_2 < prod_1 < prod_3:
            print('O produto 2 é os mais baratos!!')
            
            # Canselar o loop
            break

        elif prod_2 == prod_3 < prod_1:
            print('O produto 2 e 3 são os mais baratos!!')
            
            # Canselar o loop
            break

        if prod_3 < prod_2 < prod_1:
            print('O produto 3 é os mais baratos!!')
            
            # Canselar o loop
            break
