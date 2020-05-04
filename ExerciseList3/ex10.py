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
        time = input(
            'Em que turno você estuda, digite "M" matutino ou "V" Vespertino ou "N" Noturno: ').upper()

        time_dict = {'M': 'Bom Dia!', 'V': 'Boa Tarde!', 'N': 'Boa Noite!'}
    
    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # Informando o turo que estuda
    if time in time_dict:
        print(time_dict[time])

        # Canselar o loop
        break
    else:
        print('Valor Inválido!')
