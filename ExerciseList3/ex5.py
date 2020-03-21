
'''
5 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

#variáveis
nota_1 = float(input('Informe primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

#calculo da média
media = (nota_1 + nota_2) / 2

#mensagemde Aprovação Reprovação e Distição
if media >= 7 and media < 10:
    print(f'Parabéns sua media foi {media} e você está APROVADO!')
elif media >= 10:
    print(f'Parabéns sua media foi {media} e você foi APROVADO COM DISTINÇÃO!')
else:
    print(f'Sua media foi {media} e você está REPROVADO!')
