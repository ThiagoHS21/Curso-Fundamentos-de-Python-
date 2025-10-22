peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura: '))

imc = peso / altura **2

print (f'o seu IMC é {round(imc,2)}. ')

if imc <= 18.5:
    print ('Você está ABAIXO DO PESO!.')

elif imc <= 24.9:
    print ('Você está no PESO IDEAL!.')

elif imc <= 29.9:
    print ('Você está LEVEMENTE ACIMA DO PESO!.')

elif imc <= 34.9:
    print ('Você está com OBESIDADE GRAU I.')

elif imc <= 39.9:
    print('Você está com OBESIDADE GRAU II.')

else: 
    print ('Você está com OBESIDADE GRAU III.')

