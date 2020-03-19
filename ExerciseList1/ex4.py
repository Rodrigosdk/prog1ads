'''
Atividade 4

Escreva um programa que leia uma temperatura em graus Fahrenheit, 
transforme-a em graus Celsius e exiba o resultado.
'''
import os


while True:
    try:
        # Capitura as entradas do usuário
        fahrenheit = int(input("Insira o valor da temperatura em Fahrenheit:"))

        # Convert fahrenheit para Celsius
        cal = (fahrenheit-32)*5/9

        # Mostra na tela o resutado
        print(f"{fahrenheit} °F é igual a {cal:.2f} °C")
     
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
