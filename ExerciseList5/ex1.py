'''
1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

# Cria um loop
while True:
    # Recebe a entrada do usuário 
    user = int(input('Insira um numero entre zero e dez: '))

    # Verifica se a nota é maior que 0 e menor que 10
    if user >= 0 and user <= 10:
        
        # Mostra mensagem na tela
        print(user)
        
        # Quebra o loop
        break

    else:

        # Mostra mensagem na tela
        print('Informe um valor válido')
