'''
Atividade 1

Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) 
e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de 
combustível o usuário obterá com esses valores.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        ask_liter = float(input("Insira o valor do litro da gasolina: "))
        ask_value = float(input("Insira o valor de quanto deseja abasticer: "))

        # Calcular a quantidades de litros
        cal = ask_value/ask_liter

        # Mostra na tela o resutado
        print(f"Com R${ask_value} o veículo receber {cal:.2f} litros ")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)
        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: só é permitido números e ponto{}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    except(ZeroDivisionError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: o valor da gasulina não pode ser 0{}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)
