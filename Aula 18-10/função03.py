def calculadora(peso,altura):
    imc = peso / altura **2
    print(f'o seu IMC é de {imc}')

while True :
    op = input('Quer Calcular o seu IMC? S/N?: ')
    if op == 'n' or op == 'N': 
        print('Obrigado')

    else :
        peso = float(input('Qual o seu peso: '))
        altura = float(input('Qual a sia Altura: '))
        calculadora(peso, altura)