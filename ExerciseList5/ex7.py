# Instacia parametros 
larger = -9999999999
cont = 1

# Cria loop
while cont <= 5:
    # Recebe a entrada do usuário 
    number = int(input("Informe um número: "))
    
    # Valida as entradas
    if number > larger:
        larger = number

    # Adiciona mais um ao acontador
    cont += 1
print(larger)
