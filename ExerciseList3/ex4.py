'''

4- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de 
um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" 
se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        date = int(input("Insira um numero: "))

        # variáveis
        note_1 = float(input('Informe primeira nota: '))
        note_2 = float(input('Informe a segunda nota: '))

        # calculo da média
        average = (note_1 + note_2) / 2

        # mensagemde Aprovação Reprovação e Distição
        if average >= 9 and average == 10:
            print(f"primeira nota:{note_1}")
            print(f"primeira segunda nota: {note_2}")
            print(f"sua média foi {average}")
            print(f"conceito: A")
            print(f'Parabéns você está APROVADO!')
        elif average >= 7.5 < 9:
            print(f"primeira nota:{note_1}")
            print(f"primeira segunda nota: {note_2}")
            print(f"sua média foi {average}")
            print(f"conceito: B")
            print(f'Parabéns você está APROVADO!')
        elif average >= 6 < 7.5:
            print(f"primeira nota:{note_1}")
            print(f"primeira segunda nota: {note_2}")
            print(f"sua média foi {average}")
            print(f"conceito: D")
            print(f'Parabéns você está APROVADO!')
        elif average >= 4 < 6:
            print(f"primeira nota:{note_1}")
            print(f"primeira segunda nota: {note_2}")
            print(f"sua média foi {average}")
            print(f"conceito: E")
            print(f'você está REPROVADO!')
        elif average > 4:
            print(f"primeira nota:{note_1}")
            print(f"primeira segunda nota: {note_2}")
            print(f"sua média foi {average}")
            print(f"conceito: F")
            print(f'você está REPROVADO!')

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
