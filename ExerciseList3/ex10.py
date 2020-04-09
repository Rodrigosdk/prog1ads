'''
10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!"
 ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        shift = str(input(
            'Em que turno você estuda, digite "M" matutino ou "V" Vespertino ou "N" Noturno? ')).upper()

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # Informando o turo que estuda

    if shift == 'M':
        print('Bom Dia!')

        # Canselar o loop
        break

    elif shift == 'V':
        print('Boa Tarde!')

        # Canselar o loop
        break

    elif shift == 'N':
        print('Boa Noite!')

        # Canselar o loop
        break

    else:
        print('Valor Inválido!')
