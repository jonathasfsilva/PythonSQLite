from dml import db_insert, db_update, db_delete, db_select
from base import createDataBase
from os import system
from time import sleep

def cabecalho():
    system('clear')
    print(10*'-'+'CRUD EM PYTHON'+10*'-'+'\n')

def menu():
    print('1 - Create\n' +
    '2 - Read\n' +
    '3 - Update\n' +
    '4 - Delete\n\n'+
    '0 - Exit')

createDataBase()

while True:
    cabecalho()
    menu()
    opcao = int(input('\nOpção: '))

    if opcao == 1:
        cabecalho()
        print('MENU CREATE\n')
        nome = input('nome: ')
        fone = input('telefone: ')
        email = input('email: ')
        db_insert(nome, fone, email)
        print('cadastrado com sucesso!')
        sleep(1)
    elif opcao == 2:
        ## TODO: read
        pass
    elif opcao == 3:
        ## TODO: Update
        pass
    elif opcao == 4:
        ## TODO: delete
        pass
    elif opcao == 0:
        break
    else:
        print('invalido')
        sleep(1)
