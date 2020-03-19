number = input("digite um numero menor que 1000: ")
number_len = len(number)

if number_len == 3:
    hundred = number[0:1]
    ten = number[1:2]
    unity = number[2:3]
    
    print(f"{number}+ = {hundred} centenas, {ten} dezenas e {unity} unidades")

elif number_len == 2:
    hundred = number[0:1]
    unity = number[1:2]
    
    print(f"{number} = {hundred} dezenas e {unity} unidades")

elif number_len == 1:
    hundred = number[0:1]
    
    print(f"{number} = {unity} unidades")