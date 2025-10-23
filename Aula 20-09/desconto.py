compra = float(input('Digite o Valor total da compra: '))

if compra <= 100: 
    desconto = 0

elif compra <=300:
    desconto = compra * 0.1

elif compra <= 400:
    desconto = compra * 0.15

else:
    desconto = compra * 0.2

total = compra - desconto

print (f'Seu desconto foi {desconto}\n Total a Pagar é {total}')