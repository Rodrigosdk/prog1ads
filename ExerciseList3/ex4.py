'''
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        letter = str(input('Informe uma letra qualquer: ')).upper()

        # define as lista com as vogais e consoantes
        vowel = ['A', 'E', 'I', 'O', 'U']
        consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                     'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # comparando se a letra é uma vogal
    if letter in vowel:
        print(f'A letra digitada foi "{letter}" e ela é uma vogal.')

        # Canselar o loop
        break
    
    # comparando se a letra é uma consoante
    elif letter in consonant:
        print(f'A letra digitada foi "{letter}" e ela é uma consoante.')

        # Canselar o loop
        break

    else:
        print(f'"{letter}" não é uma letra.')
