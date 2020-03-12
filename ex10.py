'''
Atividade 10

Faça um programa que calcula o novo valor do salário de um funcionário. 
O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
'''
import os

while True:
    try:
        #Capitura as entradas do usuário
        value_salary = float(input("Insira o valor do seu salário: "))
        value_readjustment = float(input("Insira o percentual de reajuste salarial: "))

        #Calcula o novo valor do salário
        cal = value_salary + (value_salary * value_readjustment/100)

        #Mostra na tela o resutado
        print(f"Seu salrio será {cal}")
        
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