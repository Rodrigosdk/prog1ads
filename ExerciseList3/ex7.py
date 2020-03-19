'''

6 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se 
este ano é ou não bissexto
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        year = int(input("Insira um ano: "))

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
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        print('É um ano bissexto')
        
        # Canselar o loop
        break
    else:
        print('Não é bissexto')

