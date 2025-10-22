print('Verificador de acesso!\n')
print ('1 - Idoso')
print ('2 - Gestante')
print ('3 - Cadeirante')
print ('4 - Nenhuma dessas')

opcao = int(input('Digite a sua opção: '))

if opcao == 1 or opcao == 2 or opcao == 3 :
    print('Você tem direito a vaga especial!. ')

else:
    print('Você não tem direito a vaga!. ')