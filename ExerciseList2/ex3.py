'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

#variáveis
sexo = str(input('Informe seu sexo ditando "M" para masculido e "F" para feminino: ')).strip().upper()

#comparando se o sexo informado foi masculino ou feminino
if sexo == 'M':
    print('O sexo informado foi Masculino')
elif sexo == 'F':
    print('O sexo informado foi Feminino')
else:
    print('O sexo informado inválido digite novamente')