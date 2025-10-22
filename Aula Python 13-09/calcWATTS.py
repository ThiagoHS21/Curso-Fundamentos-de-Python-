print('Calculo de WATTS')

consu = float(input('insira o seu consumo de WATTS:'))

if consu <= 100:
    total = consu *0.65

elif consu <= 150:
    total = consu * 0.7

elif consu <= 200:
    total = consu * 0.75

elif consu > 200:
    total = consu * 0.8

print (f'O valor de sua conta é o total de R${round(total,2)}.')
