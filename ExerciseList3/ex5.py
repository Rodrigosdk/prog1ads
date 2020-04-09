
'''
5 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        note_1 = float(input('Informe primeira nota: '))
        note_2 = float(input('Informe a segunda nota: '))

        # Calculo da média
        average = (note_1 + note_2) / 2

    # Tratamento de erros com valor de argumento inadequado
    except ValueError:
        # Limpar a tela
        os.system("clear")

        print("="*80)

        # Mostra mensagem de erro em cor vermelha e centralizado
        print("{}Só é permitido números e pontos{}".format(
            '\033[31m', '\033[m').center(80))

        print("="*80)

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # Mensagem de aprovação reprovação e distição
    if average >= 10:
        print(f'Parabéns sua media foi {average} e você está APROVADO!')

        # Canselar o loop
        break

    elif average >= 7 and average < 10:
        print(
            f'Parabéns sua media foi {average} e você foi APROVADO COM DISTINÇÃO!')

        # Canselar o loop
        break

    else:
        print(f'Sua media foi {average} e você está REPROVADO!')

        # Canselar o loop
        break
