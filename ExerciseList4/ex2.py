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
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
import os

while True:
    try:
        # Capitura as entradas do usuário
        value_time = float(input("Insira quanto custa sua hora: "))
        time = float(input("Insira quantas horas você trabalha no mês: "))
        
        cal_fgts = cal = (value_time*time) * 11/100
        cal_syndicate =  (value_time*time) * 3/100

        gross_salary = (value_time*time)

        if gross_salary <= 900:
            cal_inss = gross_salary*10/100
            # Mostra na tela o resutado
            print(f"Salário Bruto \t: R${gross_salary}")
            print(f"(-) IR \t: Isento")
            print(f"(-) INSS ( 10%) \t: R${cal_inss}")
            print(f"FGTS (11%) \t: R${cal_fgts}")
            print(f"Total de descontos \t: {cal_syndicate+cal_fgts}")
            print(f"Salário Liquido: {gross_salary-(cal_syndicate+cal_fgts)}")

        elif gross_salary > 900 and gross_salary <= 1500:
            cal_inss = gross_salary*10/100

            print(f"Salário Bruto \t: R${gross_salary}")
            print(f"(-) IR 5% \t: {gross_salary*5/1000}")
            print(f"(-) INSS ( 10%) \t: R${cal_inss}")
            print(f"FGTS (11%) \t: R${cal_fgts}")
            print(f"Total de descontos \t: {cal_syndicate+cal_fgts}")
            print(f"Salário Liquido: {gross_salary-(cal_syndicate+cal_fgts)}")

        elif gross_salary > 1500 and gross_salary <= 2500:
            cal_inss = gross_salary*10/100

            print(f"Salário Bruto \t: R${gross_salary}")
            print(f"(-) IR 10% \t: {gross_salary*10/1000}")
            print(f"(-) INSS ( 10%) \t: R${cal_inss}")
            print(f"FGTS (11%) \t: R${cal_fgts}")
            print(f"Total de descontos \t: {cal_syndicate+cal_fgts}")
            print(f"Salário Liquido: {gross_salary-(cal_syndicate+cal_fgts)}")

        elif gross_salary < 2500:
            cal_inss = gross_salary*10/100

            print(f"Salário Bruto \t: R${gross_salary}")
            print(f"(-) IR (20%) \t: {gross_salary*10/1000}")
            print(f"(-) INSS ( 0%) \t: R${cal_inss}")
            print(f"FGTS (11%) \t: R${cal_fgts}")
            print(f"Total de descontos \t: {cal_syndicate+cal_fgts}")
            print(f"Salário Liquido: {gross_salary-(cal_syndicate+cal_fgts)}")

        # Canselar o loop
        break

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
