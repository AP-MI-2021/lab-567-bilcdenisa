from Domain.carte import get_str_carte, create_book, get_titlu, get_gen, get_pret, get_tip_reducere
from Logic.crud import create, delete, update, read
from Logic.determinare_pret_minim import determinare_pret_minim
from Logic.modificare_gen import modificare_gen
from Logic.reducere import discount


def show_menu():
    print('1. CRUD')
    print('2. Aplicare discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold')
    print('3. Modificarea genului pentru un titlu dat')
    print('4. Determinarea prețului minim pentru fiecare gen')
    print('x. Exit')


def handle_add(lista_carti):

    try:
        id_carte = int(input('Dati id carte '))
        titlu = input('Dati titlu carte ')
        gen = input('Dati gen carte ')
        pret = int(input('Dati pret carte '))
        tip_reducere = input('Dati tip reducere client ')
        return create(lista_carti, id_carte, titlu, gen, pret, tip_reducere)

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_update(lista_carti):

    try:
        id_carte = int(input('Dati id carte '))
        titlu = input('Dati titlu carte ')
        gen = input('Dati gen carte ')
        pret = int(input('Dati pret carte '))
        tip_reducere = input('Dati tip reducere client ')
        carte_noua = create_book(id_carte, titlu, gen, pret, tip_reducere)
        return update(lista_carti, carte_noua)

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_delete(lista_carti):

    try:
        id_carte = int(input('Dati id-ul cartii pe care doriti sa o stergeti '))
        return delete(lista_carti, id_carte)

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_show_all(lista_carti):

    for carte in lista_carti:
        print(get_str_carte(carte))


def handle_detalii(lista_carti):

    try:
        id_carte = int(input('Dati id carte '))
        carte = read(lista_carti, id_carte)
        print(f'Titlul este {get_titlu(carte)}')
        print(f'Genul este {get_gen(carte)}')
        print(f'Pretul este {get_pret(carte)}')
        print(f'Tipul de reducere client este {get_tip_reducere(carte)}')

    except ValueError as ve:
        print('Eroare: ', ve)


def handle_crud(lista_carti):

    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('4. Detalii carte')
        print('a. Afisare')
        print('b. Revenire')
        optiune = input('Dati optiune ')
        if optiune == '1':
            lista_carti = handle_add(lista_carti)
        elif optiune == '2':
            lista_carti = handle_update(lista_carti)
        elif optiune == '3':
            lista_carti = handle_delete(lista_carti)
        elif optiune == '4':
            handle_detalii(lista_carti)
        elif optiune == 'a':
            handle_show_all(lista_carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return lista_carti


def handle_discount(lista_carti):
    lista_noua = discount(lista_carti)
    print('Lista actualizata in urma aplicarii reducerii este: ')

    for carte in lista_noua:
        print(get_str_carte(carte))


def handle_pret_min(lista_carti):

    lista_pret_min = determinare_pret_minim(lista_carti)

    for pret in lista_pret_min:
        print(f'Pretul minim pentru genul {pret[0]} este {pret[1]}')
    return lista_carti


def handle_modificare_gen(lista_carti):

    try:
        id_carte = int(input('Dati id-ul cartii al carui gen doriti sa il modificati '))
        titlu = input('Dati titlul cartii ')
        gen = input('Dati genul cartii in care doriti sa il modificati ')
        lista_noua = modificare_gen(lista_carti, id_carte, gen, titlu)
        for carte in lista_noua:
            print(get_str_carte(carte))

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def run_ui(lista_carti):

    while True:
        show_menu()
        optiune = input('Dati optiune ')
        if optiune == '1':
            carti = handle_crud(lista_carti)
        elif optiune == '2':
            handle_discount(lista_carti)
        elif optiune == '3':
            handle_modificare_gen(lista_carti)
        elif optiune == '4':
            handle_pret_min(lista_carti)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return lista_carti
