print ('''Cardapio Da Pizzaria\n
1 - Calabresa 
2 - Napolitana
3 - Portuguesa
4 - Marguerita\n''')

opçao = int(input('Digite o Numero do sabor da Pizza: '))


if opçao == 1: 
    pizza = 42.50

elif opçao == 2:
    pizza = 32.50

elif opçao == 3:
    pizza = 36.50

else: 
    pizza = 39.80

refri = input('\nGostaria de Refrigerante? Digite "S" ou "N": ')

if refri == "S" or refri == "s":
    total = pizza + 8.9

else:
    total = pizza

print (f'\nO valor Total do pedido é R${total:0.2f}')

