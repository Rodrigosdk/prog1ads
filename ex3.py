'''
Atividade 3

Faça um programa que calcule a média de consumo de combustível de um veículo. 
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) 
e quantos litros foram gastos no percurso.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        start_km = float(input("Insira o km inicial: "))
        end_km = float(input("Insira o km final: "))
        ask_liter = float(input("Insira quantos litros foram gastos: "))

        # Calcular a média do usuário
        cal = (end_km - start_km) / ask_liter

        # Mostra na tela o resutado
        print(f"você realizou {cal:.2f}L/km")

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
    except ZeroDivisionError:
        os.system("clear")

        print("="*80)
        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Você não pode dirigir sem gasolina{}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)
