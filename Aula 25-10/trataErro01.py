# Exemplo de Erro Comuns

while True:
    try:
        num1 = int(input('Digite o Primeiro Numero: '))
        num2 = int(input('\nDigite o Segundo Numero: '))

        resultado = num1 / num2

        print(f'\nO Resultado da operação é {resultado}')
        break
    except ZeroDivisionError:
        print('\nOps! o Segundo valor não pode ser ZERO!!!.')
    except ValueError:
        print('\nOps! Digite somente NUMEROS  INTEIROS!!')
    except:
        print('\Ops! Erro Inesperado!!!')
