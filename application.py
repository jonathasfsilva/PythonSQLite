from dml import db_insert, db_update, db_delete, db_select
from base import createDataBase
from interface import cabecalho, menu, mostraDados
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
        data = input('digite um email:  ')
        res = db_select(data, "email")
        if res != None:
            mostraDados(res)
        else:
            print('nenhum email encontrado')
        input()
    elif opcao == 3:
        cabecalho()
        print('MENU UPDATE')
        data = input('digite um email:  ')
        if db_select(data, 'email') != None:
            nome = input('novo nome: ')
            db_update(nome, data)
            mostraDados(db_select(data, 'email'))
        else:
            print('nenhum email encontrado')
        input()
    elif opcao == 4:
        cabecalho()
        print('MENU DELETE')
        data = input('digite um email:  ')
        if db_select(data, 'email') != None:
            db_delete(data)
            print('deletado com sucesso')
        else:
            print('nenhum email encontrado')
        input()
    elif opcao == 0:
        break
    else:
        print('invalido')
        sleep(1)
