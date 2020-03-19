'''

9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        number = input("digite um numero menor que 1000: ")
        number_len = len(number)

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
    if number_len == 3:
        hundred = number[0:1]
        ten = number[1:2]
        unity = number[2:3]

        print(f"{number} = {hundred} centenas, {ten} dezenas e {unity} unidades")

        # Canselar o loop
        break

    elif number_len == 2:
        hundred = number[0:1]
        unity = number[1:2]

        print(f"{number} = {hundred} dezenas e {unity} unidades")

        # Canselar o loop
        break

    elif number_len == 1:
        hundred = number[0:1]

        print(f"{number} = {unity} unidades")

        # Canselar o loop
        break
