print ('***BEM VINDO***')

lista = []

while True :
    nome = input('Digite um nome para inserir ou a letra "Q" para sair: ')
    
    if nome == 'Q' or nome == 'q':
        print ('Aqui está sua lista\n')
        break

    else :
        lista.append(nome)

cont = 1
for i in lista:
    print(f'{cont} : {i}')
    cont += 1

    