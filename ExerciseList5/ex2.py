'''
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

# Cria um loop
while True:
    # Recebe a entrada do usuário 
    user = input('Insira o usuário: ')
    password = input('Insira a sua senha: ')

    # Verifica se a senha é diferente do usuário
    if user != password:
        # Mostra mensagem na tela
        print('ok')
        
        # Quebra o loop
        break
    
    else:
        # Mostra mensagem na tela
        print('Nome e senha não pode ser igual!')