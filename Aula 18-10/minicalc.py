# Espaço para as finções 
def somar (num1, num2):
    #num1 = float(input('Digite o primeiro numero: '))
    #num2 = float(input('Digite o segundo numero: '))
    result = num1 + num2
    return result

def Sub (num1, num2):
    #num1 = float(input('Digite o primeiro numero: '))
    #num2 = float(input('Digite o segundo numero: '))
    result = num1 - num2
    return result 

def Mult (num1, num2):
    #num1 = float(input('Digite o primeiro numero: '))
    #num2 = float(input('Digite o segundo numero: '))
    while True:
        if num2 == 0:
            print('\nO segundo numero não pode ser 0')
            num2 = float(input('\nO Digite o segundo numero novamente: '))

        else:
            result = num1 * num2
            return result

def Dividir (num1, num2):
    #num1 = float(input('Digite o primeiro numero: '))
    #num2 = float(input('Digite o segundo numero: '))
    while True:
        if num2 == 0:
            print('\nO segundo numero não pode ser 0')
            num2 = float(input('\nO Digite o segundo numero novamente: '))

        else:
            result = num1 / num2 
            return result

# Corpo do Codigos
while True:
    print('\n***MINI CALCULADORA***')
    print('\nQual operação deseja fazer ')
    print('\n1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair')
    op = input ('\ndigite a operação desejada: ')
    num1 = float(input('\nDigite o primeiro numero: '))
    num2 = float(input('\nDigite o segundo numero: '))


    if op == '5' :
        print('\nObrigado')
        break
    
    elif op == '1' : 
        print(f'\nresultado da soma é {somar(num1, num2)}')

    elif op == '2' : 
        print(f'\nresultado da Subtração é {Sub(num1, num2)}')

    elif op == '3' : 
        print(f'\nresultado da Multiplicação é {Mult(num1, num2)}')

    elif op == '4' : 
        print(f'\nresultado da Divisão é {Dividir(num1, num2)}')
    

