import os
import msvcrt
import time

os.system('cls')


while True :
    email = input('Digite Seu Email: ')
    senha = input('Digite Sua Senha: ')

    if email == 'teste@teste' and senha == '12345':
        os.system ('cls')
        time.sleep(3)
        print ('Dados Validado com SUCESSO!!')
        time.sleep(2)
        os.system ('cls')
        break


    else :
        os.system ('cls')
        print('Dados não CONFEREM!!')
        print('Tente novamente!')
        time.sleep(3)
        os.system ('cls')
