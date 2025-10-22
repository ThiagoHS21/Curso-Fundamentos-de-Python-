nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))

if idade >= 18 and altura >= 1.70:
    print(f'{nome} você está apto para vaga!')

else: 
    print(f'{nome} você não está apto para vaga!')
