produtos = {
    'Batata': 4.90,
    'Cebola': [2.95, 3.80, 5.90],
    'Cenoura': 3.99,
    'Beterraba': 6.99,
}
cont = 1 
for i,j in produtos.items():
    print (f'{cont} - {i} : {j}')
    cont += 1