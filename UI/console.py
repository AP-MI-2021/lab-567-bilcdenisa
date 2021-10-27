from Domain.carte import get_str_carte
from Logic.crud import create


def show_menu():
    print('1. CRUD')
    print('x. Exit')

def handle_add(carte):
    id_carte = int(input('Dati id carte '))
    titlu = input('Dati titlu carte ')
    gen = input('Dati gen carte ')
    pret = int(input('Dati pret carte '))
    tip_reducere = input('Dati tip reducere client ')
    return create(carte, id_carte, titlu, gen, pret, tip_reducere)

def handle_crud(carti):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')
        optiune = input('Dati optiune ')
        if optiune == '1':
            handle_add(carti)
        elif optiune == 'a':

            handle_show_all(carti)

        elif optiune == '2':
            handle_update(carti)

        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return carti



def handle_show_all(carti):
    for carte in carti:
        print(get_str_carte(carte))


def run_ui(carti):
    while True:
        show_menu()
        optiune = input('Dati optiune ')
        if optiune == '1':
            carti = handle_crud(carti)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return carti

