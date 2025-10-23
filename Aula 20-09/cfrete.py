compra = float(input('Digite o Valor da Compra: '))

distancia = float(input('Digite a Distância (km): '))

if compra > 200 :
    frete = 0

elif distancia <= 50:
    frete = distancia * 1

else:
    frete = distancia * 1.5

print(f'Valor do frete é R${frete:0.2f}\n Valor total da entrega é {compra+frete:0.2f}')
