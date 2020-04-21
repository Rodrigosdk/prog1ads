'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
decrescimento iniciais. Valide a entrada e permita repetir a operação.
'''
import os

# Contador de anos
year = 0

while True:
    # Capitura as entradas de dados
    country_a = int(input('população do país A: '))
    country_b = int(input('população de país B: '))

    percentage_country_a = float(input('taxa anual de crescimento do país A: '))
    percentage_country_b = float(input('taxa anual de crescimento do país B: '))

    while country_a < country_b:
        # Calcula taxa de pocertagem da população
        country_growth_rate_a = percentage_country_a/100
        country_growth_rate_b = percentage_country_b/100

        # Calcula taxa de crecimento de uma população
        country_a += country_a * country_growth_rate_a
        country_b += country_b * country_growth_rate_b

        # Adiciona mais um ao contador
        year += 1

    # Limpa tela
    os.system('clear')

    # Mostra resutado
    print(f'Ano {year} - população do país A: {country_a:.0f}')
    print(f'Ano {year} - população do país B: {country_b:.0f}')

    # Zera o contador
    year = 0
