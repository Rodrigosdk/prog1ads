'''
2- Sabendo que a cotação atual do dólar americano é R$ 4,47, receba um valor em reais do usuário e 
converta para dólares. Exemplo de saída: $ 1.003 - Em um banho de 5 minutos, fechando o registro ao se 
ensaboar, são gastos 45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros, calcule quantos 
banhos de 5 minutos são necessários para consumir 1 metro cúbico de água? 
'''

# Capitura as entradas do usuário
time_bath = int(input("Quanto tempo demora seu banho: "))

# Calcular metros cubicos gastos no banho por minuto
liters_minute = 9
time_all_bath = time_bath * liters_minute
shower = 1000 / time_all_bath

# Mostra na tela o resutado
print("Para um banho de {} minutos, 1m3 permite {} banhos.".format(
    time_bath, int(shower)))
