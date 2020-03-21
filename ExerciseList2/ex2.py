'''
Atividade 2

Em um banho de 5 minutos, fechando o registro ao se ensaboar, 
são gastos 45 litros de água. Sabendo que em 1 m3 de água há 
1.000 litros, calcule quantos banhos de 5 minutos são necessários 
para consumir 1 metro cúbico de água?
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        time_bath = int(input("Quanto tempo demora seu banho: "))

        # Calcular metros cubicos gastos no banho por minuto
        liters_minute = 9
        time_all_bath = time_bath * liters_minute
        shower = 1000 / time_all_bath

        # Mostra na tela o resutado
        print("Para um banho de {} minutos, 1m3 permite {} banhos.".format(
            time_bath, int(shower)))

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)
        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: só é permitido números inteiros{}".format(
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
        print("{}Quanto tempo você demora no banho?{}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)
