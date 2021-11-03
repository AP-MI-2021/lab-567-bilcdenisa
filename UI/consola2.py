from Domain.carte import get_str_carte, get_titlu, get_gen, get_pret, get_tip_reducere, create_book
from Logic.crud import create, delete, update, read
from Logic.determinare_pret_minim import determinare_pret_minim
from Logic.modificare_gen import modificare_gen
from Logic.reducere import discount


def show_menu2():
    print(' Comenzi: ')
    print(' add ')
    print(' delete ')
    print(' showall ')
    print(' update ')
    print(' details ')
    print(' pret minim ')
    print(' modificare gen ')
    print(' discount ')
    print(' quit ')

def handle_details(lista_carti, comanda):
    try:
        comanda[1] = int(comanda[1])
        carte = read(lista_carti, comanda[1])
        print('Detaliile despre carte sunt: ')
        print(f'Titlul este {get_titlu(carte)}')
        print(f'Genul este {get_gen(carte)}')
        print(f'Pretul este {get_pret(carte)}')
        print(f'Tipul de reducere client este {get_tip_reducere(carte)}')

    except ValueError as ve:
        print('Eroare: ', ve)

def prelucrare_input(lista_comenzi):

    comenzi = lista_comenzi.split(sep=";")

    lst_comenzi = []
    for comanda in comenzi:
        comenzi_despartite_prin_spatiu = comanda.split(sep=",")
        lst_comenzi.append(comenzi_despartite_prin_spatiu)

    return lst_comenzi

def handle_showall2(lista_carti):
    for carte in lista_carti:
        print(get_str_carte(carte))

def handle_add2(lista_carti,comanda):
    try:
        comanda[1] = int(comanda[1])
        comanda[4] = int(comanda[4])
        carti = create(lista_carti, comanda[1], comanda[2], comanda[3], comanda[4], comanda[5])
        print('lista in urma adaugarii este ')
        handle_showall2(carti)
    except ValueError as ve:
        print('eroare ', ve)
    return lista_carti

def handle_delete2(lista_carti,comanda):
    try:
        comanda[1] = int(comanda[1])
        carti = delete(lista_carti, comanda[1])
        print('Lista in urma stergerii este ')
        handle_showall2(carti)
    except ValueError as ve:
        print('Eroare: ', ve)

def handle_update2(lista_carti, comanda):

    try:
        comanda[1] = int(comanda[1])
        comanda[4] = int(comanda[4])
        carte_noua = create_book(comanda[1], comanda[2], comanda[3], comanda[4],comanda[5])
        carti = update(lista_carti, carte_noua)
        print('Lista updatata este: ')
        handle_showall2(carti)

    except ValueError as ve:
        print('Eroare: ', ve)

def handle_pret_minim2(lista_carti):
    lista_pret_min = determinare_pret_minim(lista_carti)
    print('Preturile minime pentru fiecare gen sunt: ')
    for pret in lista_pret_min:
        print(f'Pretul minim pentru genul {pret[0]} este {pret[1]}')
    return lista_carti


def handle_modificare_gen2(lista_carti, comanda):
    try:
        comanda[1] = int(comanda[1])
        lista_noua = modificare_gen(lista_carti, comanda[1], comanda[3], comanda[2])
        print('Lista in urma modificarii genului este ')
        for carte in lista_noua:
            print(get_str_carte(carte))
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_help():
    print('add,15,titlu,gen,15,silver;')
    print('delete,2;')
    print('showall;')
    print('update,3,titlu1,gen1,15,gold;')
    print('details,4;')
    print('pret minim;')
    print('modificare gen,4,titlu4,gen15;')
    print('discount')
    print('quit;')


def handle_discount2(lista_carti):
    lista_noua = discount(lista_carti)
    print('Lista actualizata in urma aplicarii reducerii este: ')

    for carte in lista_noua:
        print(get_str_carte(carte))


def run_ui2(lista_carti):
    ok = True
    while ok == True:
        show_menu2()
        lista_comenzi = input('Dati comenzi despartite prin ; si parametrii prin , ')
        lista_cu_comenzi = prelucrare_input(lista_comenzi)

        for comanda in lista_cu_comenzi:
            if comanda[0] == 'delete':
                handle_delete2(lista_carti,comanda)
            elif comanda[0] == 'add':
                handle_add2(lista_carti,comanda)
            elif comanda[0] == 'showall':
                print('Lista de carti este: ')
                handle_showall2(lista_carti)
            elif comanda[0] == 'update':
                handle_update2(lista_carti, comanda)
            elif comanda[0] == 'details':
                handle_details(lista_carti, comanda)
            elif comanda[0] == 'pret minim':
                handle_pret_minim2(lista_carti)
            elif comanda[0] == 'modificare gen':
                handle_modificare_gen2(lista_carti, comanda)
            elif comanda[0] == 'help':
                handle_help()
            elif comanda[0]=='discount':
                handle_discount2(lista_carti)
            elif comanda[0] == 'quit':
                ok = False
        if ok == False:
            break
