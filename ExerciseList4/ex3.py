'''

3- Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        date = int(input("Insira um numero: "))

        if date == 1:
            # Mostra na tela o resutado
            print(f"{date}-Domingo")
        if date == 2:
            # Mostra na tela o resutado
            print(f"{date}-segunda-feira")
        if date == 3:
            # Mostra na tela o resutado
            print(f"{date}-Terça-feira")
        if date == 4:
            # Mostra na tela o resutado
            print(f"{date}-Quarta-feira")
        if date == 5:
            # Mostra na tela o resutado
            print(f"{date}-Quinta-feira")
        if date == 6:
            # Mostra na tela o resutado
            print(f"{date}-Sexta-feira")
        if date == 7:
            # Mostra na tela o resutado
            print(f"{date}-Sábado")
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
        print("{}Erro: Erro: só é permitido números e pontos {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
