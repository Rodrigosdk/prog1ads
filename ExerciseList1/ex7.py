'''
Atividade 7

Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos. 
O usuário deve inserir a largura e comprimento de cada um dos cômodos, 
calcular a área individual de cada um e por fim exibir a área total da casa
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        convenient1_width = float(input("Inserir a largura do cômodos 1: "))
        convenient1_height = float(input("Inserir a altura do cômodos 1: "))

        convenient2_width = float(input("Inserir a largura do cômodos 2: "))
        convenient2_height = float(input("Inserir a altura do cômodos 2: "))

        convenient3_width = float(input("Inserir a largura do cômodos 3: "))
        convenient3_height = float(input("Inserir a altura do cômodos 3: "))

        convenient4_width = float(input("Inserir a largura do cômodos 4: "))
        convenient4_height = float(input("Inserir a altura do cômodos 4: "))

        # Calcula a area dos cômodos
        total_area_convenient1 = convenient1_width*convenient1_height
        total_area_convenient2 = convenient2_width*convenient2_height
        total_area_convenient3 = convenient3_width*convenient3_height
        total_area_convenient4 = convenient4_width*convenient4_height

        # Caucula a área total da casa
        total_area = total_area_convenient1 + total_area_convenient2 + \
            total_area_convenient3 + total_area_convenient4

        # Mostra na tela o resutado
        print(f"Área total da sua casa é de {total_area}m²")

        # Canselar o loop
        break

    # Tratamento de erros com valor de argumento inadequado
    except (ValueError):
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Erro: Erro: só é permitido números e ponto {}".format(
            '\033[31m', '\033[m').center(80))
        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):

        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break
