#Lista telefonica
import os
import time

agenda = {}

def inserir_contatos():
    os.system('cls')
    nome = input('\nDigite o nome do Contato: ')
    telefone = input('\nDigite o Numero de telefone do Contato: ')
    agenda[nome] = telefone
    os.system('cls')
    print('Dados Inserido com Sucesso!')
    time.sleep(2)
    os.system('cls')

def exibir_contatos():
    os.system('cls')
    print('Lista de Contatos')
    print('-' * 20)
    cont = 1 
    for i,j in agenda.items():
        print(f'{cont} : {i} - Telefone: {j}')
        cont += 1
    time.sleep(2)
    os.system('cls')
    
    # Menu Agenda

while True:
    print('***AGENDA DE TELEFONE***\n')
    print('Opções:')
    print('1 - Inserir Contato\n2 - Exibir Lista de Contato\n3 - Sair do App')

    op = input('\nDigite a opção desejada:')

    if op == '3':
        os.system('cls')
        print('Obrigado por usar o APP!!')
        time.sleep(2)
        os.system('cls')
        break
    elif op == '1':
        inserir_contatos()
    elif op == '2':
        exibir_contatos()