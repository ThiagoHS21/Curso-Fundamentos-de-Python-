nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) /4

print(f'A média das suas notas é {media}')

if media < 4:
    print('\nVocê foi REPROVADO!!')

elif media < 6:
    print ('Você está de RECUPERAÇÃO!!')

else:
    print('\nParabéns! Você está APROVADO!!')