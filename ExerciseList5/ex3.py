'''
3 - Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

# Cria um loop
while True:
    # Recebe a entrada do usuário 
    name = input('Insira o nome: ')
    age = int(input('Insira a Idade: '))
    Salary = int(input('Insira o Salário: '))
    gender = input('Insira o seu Sexo: ')
    civil_status = input('Insira o seu estado civil: ')

    # Instacia parametros 
    name_len = len(name)
    gender_list = ['masculino', 'm', 'feminino', 'f']
    civil_status_list = ['solteiro', 'casado',
                         'viúvo', 'divorciado', 's', 'c', 'v', 'd']
    # Valida entradas
    if name_len > 3:
        if age > 0  and age < 150:
            if Salary > 0: 
                if gender in gender_list:
                    if civil_status in civil_status_list:
                        print('ok')
                        
    else:
        print('Valor invalido')
