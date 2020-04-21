'''
4 - Suponha que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual 
de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxade crescimento 
de 1.5%. Faça um programa que calcule e escreva o número de anosnecessários para que a população 
do país A ultrapasse ou iguale a população do país B,mantidas as taxas de crescimento.
'''
# Instacia parametros 
nation_a = 80000
nation_b = 200000

# Cria contador
year = 0

# Valida as entradas
while nation_a <= nation_b :

    # Calcuala o crecimento 
    nation_a += nation_a * 0.03
    nation_b += nation_b * 0.015
    
    # Adiciona mais um ao acontador
    year += 1


print(f'Ano {year} - população do país A: {int(nation_a)}')
print(f'Ano {year} - população do país B: {int(nation_b)}')
    
