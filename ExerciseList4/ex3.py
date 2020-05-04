'''

3- Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        date = int(input("Insira um numero: "))
        data_dict = {1: 'Domingo', 2: 'Segunda-feira', 3: 'Terça-feira',
                     4: 'Quarta-feira', 5: 'Quinta-feira', 6: 'Sexta-feira', 
                     7: 'Sábado'}

        if date in data_dict:
            # Mostra na tela o resutado
            print(data_dict[date])

        else:
            print("valor invalido")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: Erro: só é permitido números inteiros{}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
