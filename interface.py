from os import system

def cabecalho():
    system('clear')
    print(10*'-'+'CRUD EM PYTHON'+10*'-'+'\n')

def menu():
    print('1 - Create\n' +
    '2 - Read\n' +
    '3 - Update\n' +
    '4 - Delete\n\n'+
    '0 - Exit')
