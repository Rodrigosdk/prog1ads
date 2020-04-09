'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        sex = str(input(
            'Informe seu sexo ditando "M" para masculido e "F" para feminino: ')).upper()

    # Tratamento de erro de interupção
    except(KeyboardInterrupt, EOFError):
        # Limpar a telar
        os.system("clear") or None

        # Canselar o loop
        break

    # comparando se o sexo informado foi masculino ou feminino
    if sex == 'M':
        print('O sexo informado foi Masculino')
    elif sex == 'F':
        print('O sexo informado foi Feminino')
    else:
        print('O sexo informado inválido digite novamente')
