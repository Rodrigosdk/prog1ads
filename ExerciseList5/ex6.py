'''
Faça um programa que imprima na tela os números de 1 a 20, 
um abaixo do outro.Depois modique o programa para que ele 
mostre os números um ao lado do outro.
'''


def counter(init, end, type_line=None):
    '''
    init: valor inicial;
    
    end: valor final;

    type_line = como a mensegem deve se apresentar. ex:
    
    counter(1, 21) ==> printa o valor de 1 até 20;
    
    counter(1, 21, ",") ==> printa os valores em uma unica linha segido pelo 
    argumento recebido por type_line: 1,2,3,4...20
    
    '''
    try:
        # Valida as entradas
        while init != end:
            
            #verifica como deve ser inpresa a mensagem
            if type_line == None:
                print(init)

            else: 
                print(init, end=type_line)
            
            init += 1
    except TypeError:
        print('O valor informado deve ser inteiro')

counter(1, 21)
counter(1, 21)