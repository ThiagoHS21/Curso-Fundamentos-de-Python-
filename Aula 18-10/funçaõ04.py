def area():
    lado1 = float(input('Digite o primeiro lado: '))
    lado2 = float(input('Digite o segundo lado: '))
    resultado = lado1 * lado2 
    print(f'A area do retangulo é {resultado:0.2f}')
    
print('Calculadora de area')
print('*' * 20)

area()