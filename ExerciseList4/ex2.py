'''

2- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
 Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
 e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
 O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
 o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o
exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220): R$ 1100,00
        (-) IR (5%): R$55,00
        (-) INSS ( 10%): R$110,00
        FGTS (11%): R$121,00
        Total de descontos: R$165,00
        Salário Liquido: R$935,00
'''
import os


def printoutput(gross_salary, time, value_time, percentage_ir=None):
    '''
    gross_salary: valor do salário bruto;
    time: horas trabalhada
    value_time: custo da hora
    percentage_ir: desconto do imposto de renda
    '''
    fgts = (value_time*time) * 11/100
    syndicate = (value_time*time) * 3/100
    inss = gross_salary*10/100

    if percentage_ir == None:
        print(f"Salário Bruto: R${gross_salary}")
        print(f"(-) IR: Isento")
        print(f"(-) INSS (10): R${inss}")
        print(f"FGTS (11%): R${fgts}")
        print(f"Total de descontos: {syndicate+fgts}")
        print(f"Salário Liquido: {gross_salary-(syndicate+fgts)}")
    else:
        
        ir = gross_salary*5/1000
        print(f"Salário Bruto: R${gross_salary}")
        print(f"(-) IR ({percentage_ir}): {ir}")
        print(f"(-) INSS (10): R${inss}")
        print(f"FGTS (11%): R${fgts}")
        print(f"Total de descontos: {syndicate+fgts}")
        print(f"Salário Liquido: {gross_salary-(syndicate+fgts)}")


while True:
    try:
        # Capitura as entradas do usuário
        value_time = int(input("Insira quanto custa sua hora: "))
        time = float(input("Insira quantas horas você trabalha no mês: "))

        gross_salary = (value_time*time)

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

    if gross_salary <= 900:
        # Mostra na tela o resutado
        printoutput(gross_salary, time, value_time)

        # Canselar o loop
        break

    elif gross_salary > 900 and gross_salary <= 1500:
        # Mostra na tela o resutado
        printoutput(gross_salary, time, value_time, 5)

        # Canselar o loop
        break

    elif gross_salary > 1500 and gross_salary <= 2500:
        # Mostra na tela o resutado
        printoutput(gross_salary, time, value_time, 10)

        # Canselar o loop
        break

    elif gross_salary < 2500:
        # Mostra na tela o resutado
        printoutput(gross_salary, time, value_time)

        # Canselar o loop
        break
