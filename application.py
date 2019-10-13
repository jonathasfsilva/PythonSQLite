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
    '4 - Delete')

createDataBase()

while True:
    cabecalho()
    menu()
    opcao = input('\nOpção: ')

    if opcao == 1:
        ## TODO: create
        pass
    elif opcao == 2:
        ## TODO: read
        pass
    elif opcao == 3:
        ## TODO: Update
        pass
    elif opcao == 4:
        ## TODO: delete
        pass
    else:
        print('invalido')
