'''
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

#variáveis
letra = str(input('Informe uma letra qualquer: ')).strip().upper()

#comparando se a letra é uma vogal ou uma consoante
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f'A letra digitada foi "{letra}" e ela é uma vogal.')
else:
    print(f'A letra digitada foi "{letra}" e ela é uma consoante.')

