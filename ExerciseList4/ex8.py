'''

6 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se 
este ano é ou não bissexto
'''
import os

validade = "true"
i = 0

while validade == "true" and i == 0:
    try:
        # Capitura as entradas do usuário
        date = input("Insira uma data: ")
        
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
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
    if (year%4 == 0 and year%100!= 0) or year%400 == 0:
        bissexto = "sim"
    else:
        bissexto = "nao"

    if month < 1 or month > 12:
        validade = "false"

    elif day > 31 or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30):
        validade = "false"

    elif (month == 2 and bissexto == "nao" and day > 28) or ( month == 2 and bissexto == "sim" and day > 29):
        validade = "false"

if validade == "true":
    print("data valida")
else:
    print("data invalida")

