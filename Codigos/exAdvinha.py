import os
import msvcrt
import time

os.system('cls')
time.sleep(2)

print('Adivinhe o Número Secreto')

time.sleep(2)
os.system ('cls')
time.sleep(1)

num = 3

tentativa = 0

while True:
    
    palpite = float(input('Digite o número: '))

    if palpite == num :
        os.system ('cls')
        time.sleep(3)

        print ('o número escolhido esta CORRETO!!')

        time.sleep(2)
        os.system ('cls')
        break

    else :
        os.system ('cls')
        print('Número Esolhido não CONFEREM!!')

        if tentativa == 3:
            print('Fim de Jogo!!. Suas tentativas acabaram')
            time.sleep(2)
    
            if  palpite > num:
                print('Seu número é maior que o número secreto.')

            else:
                print('Seu numero é menor que o número secreto.')


        time.sleep(2)
        os.system ('cls')

        print('Tente novamente!')

        time.sleep(1)
        os.system ('cls')
    tentativa = tentativa + 1
