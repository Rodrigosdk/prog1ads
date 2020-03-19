'''
Atividade 9

Escreva um programa que converte valores de polegadas em centímetros utilizando 
a seguinte fórmula para conversão: 1 polegada = 2,54 cm.
'''
import os

while True:
    try:
        #Capitura as entradas do usuário
        value = int(input("Insira um valor das polegadas que deseja converter em cm: "))

        #Mostra na tela o resutado
        print(f"Você dígito {value} polegadas e seu valor em centímetros é {value*2.54}cm")
        
        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: Erro: só é permitido números inteiros {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break