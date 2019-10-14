from dml import db_insert, db_update, db_delete, db_select
from base import createDataBase
from interface import cabecalho, menu
#from os import system
from time import sleep

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
        cabecalho()
        print('MENU READ\n')
        #field = input('qual campo voce quer pesquisar? (id, name, phone, email):')
        data = input('qual dado: ')

        res = db_select(data, "name")
        print(res)
        input()
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
