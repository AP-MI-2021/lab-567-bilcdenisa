from Domain.carte import get_str_carte, create_book, get_titlu, get_gen, get_pret, get_tip_reducere
from Logic.afisare_titluri_distincte import titluri_distincte
from Logic.crud import create, delete, update, read
from Logic.determinare_pret_minim import determinare_pret_minim
from Logic.lista_noua import lista_noua
from Logic.modificare_gen import modificare_gen
from Logic.ordonare import ordonare
from Logic.redo import redo
from Logic.reducere import discount
from Logic.undo import undo


def show_menu():
    print('1. CRUD')
    print('2. Aplicare discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold')
    print('3. Modificarea genului pentru un titlu dat')
    print('4. Determinarea prețului minim pentru fiecare gen')
    print('5. Ordonarea vânzărilor crescător după preț ')
    print('6. Afișarea numărului de titluri distincte pentru fiecare gen ')
    print('u. Undo')
    print('r. Redo')
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


def handle_crud(lista_carti, lista_versiuni, versiune_curenta):

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
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '2':
            lista_carti = handle_update(lista_carti)
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '3':
            lista_carti = handle_delete(lista_carti)
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '4':
            handle_detalii(lista_carti)
        elif optiune == 'a':
            handle_show_all(lista_carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')

    return lista_carti, lista_versiuni, versiune_curenta


def handle_discount(lista_carti):

    try:
        lista_carti = discount(lista_carti)
        print('Lista actualizata in urma aplicarii reducerii este: ')

        for carte in lista_carti:
            print(get_str_carte(carte))
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista_carti


def handle_pret_min(lista_carti):

    try:
        lista_pret_min = determinare_pret_minim(lista_carti)

        for pret in lista_pret_min:
            print(f'Pretul minim pentru genul {pret[0]} este {pret[1]}')
        return lista_carti

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_modificare_gen(lista_carti):

    try:
        id_carte = int(input('Dati id-ul cartii al carui gen doriti sa il modificati '))
        titlu = input('Dati titlul cartii ')
        gen = input('Dati genul cartii in care doriti sa il modificati ')
        lista_carti = modificare_gen(lista_carti, id_carte, gen, titlu)
        for carte in lista_carti:
            print(get_str_carte(carte))

    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_ordonare(lista_carti):
    try:
        lista_carti = ordonare(lista_carti)
        handle_show_all(lista_carti)
    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti):
    return lista_noua(lista_versiuni, versiune_curenta, lista_carti)


def handle_undo(lista_versiuni, versiune_curenta):
    return undo(lista_versiuni, versiune_curenta)

def handle_redo(lista_versiuni, versiune_curenta):
    return redo(lista_versiuni, versiune_curenta)

def handle_afisare_nr_titluri_distincte(lista_carti):
    try:
        lista = titluri_distincte(lista_carti)
        for tuplu in lista:
            print(f'Numarul de titluri distincte pentru genul {tuplu[0]} este {tuplu[1]}')
    except ValueError as ve:
        print('Eroare: ', ve)

    return lista_carti


def run_ui(lista_carti):

    lista_versiuni = [lista_carti]
    versiune_curenta = 0

    while True:
        show_menu()
        optiune = input('Dati optiune ')
        if optiune == '1':
            lista_carti, lista_versiuni, versiune_curenta = handle_crud(lista_carti, lista_versiuni, versiune_curenta)
        elif optiune == '2':
            lista_carti = handle_discount(lista_carti)
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '3':
            lista_carti = handle_modificare_gen(lista_carti)
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '4':
            handle_pret_min(lista_carti)
        elif optiune == '5':
            lista_carti = handle_ordonare(lista_carti)
            lista_versiuni, versiune_curenta = handle_lista_noua(lista_versiuni, versiune_curenta, lista_carti)
        elif optiune == '6':
            handle_afisare_nr_titluri_distincte(lista_carti)
        elif optiune == 'x':
            break
        elif optiune == 'u':
            if versiune_curenta < 1:
                print('Nu se mai poate face undo')
            else:
                lista_carti, versiune_curenta = handle_undo(lista_versiuni, versiune_curenta)
                if lista_carti == []:
                    print(f'Lista este goala {lista_carti}')
        elif optiune == 'r':
            if versiune_curenta == len(lista_versiuni) - 1:
                print('Nu se mai poate face redo')
            else:
                lista_carti, versiune_curenta = handle_redo(lista_versiuni, versiune_curenta)
        else:
            print('Optiune invalida')
    return lista_carti
