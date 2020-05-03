'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        gender = str(input(
            'Informe seu sexo ditando "M" para masculido e "F" para feminino: ')).upper()

        gender_dict = {'M': 'O sexo informado foi Masculino',
                       'F': 'O sexo informado foi Feminino'}

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # comparando se o sexo informado foi masculino ou feminino
    if gender in gender_dict:
        print(gender_dict[gender])
    else:
        print('O sexo informado é inválido digite novamente')
