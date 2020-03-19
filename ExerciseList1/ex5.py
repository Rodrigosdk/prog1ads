'''
Atividade 5

Faça um programa que calcule o valor a ser pago por uma dívida em atraso. 
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade
de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
'''
import os


def Error(msg):
    # Limpar a tela
    os.system("clear")

    print("="*80)

    # Mostra mensagem de erro em cor vermelha e centralizado
    print("{}Erro: {} {}".format(
        '\033[31m', msg, '\033[m').center(80))
    print("="*80)


while True:
    try:
        # Capitura as entradas do usuário
        ask_debt = float(input("Valor da divida: "))

        try:
            # Capitura as entradas do usuário
            ask_day = int(input("Quantidade de dias em atraso: "))

        # Tratamento de erros com valor de argumento inadequado
        except(ValueError):
            Error("só é permitido números inteiros")

        # Capitura as entradas do usuário
        ask_interest = float(input("Valor da multa por dia de atraso: "))

        # Calcula o valor a ser pago por uma dívida em atraso
        cal = (ask_interest*ask_day) + ask_debt

        # Mostra na tela o resutado
        print(f"O valor a ser pago é de R$ {cal}")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Mostra mensagem de erro
        Error("só é permitido números e ponto.")

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
