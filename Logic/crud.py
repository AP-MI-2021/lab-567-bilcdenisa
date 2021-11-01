from Domain.carte import create_book, get_id, get_titlu, get_gen, get_pret, get_tip_reducere


def create(lista_carti, id_carte, titlu, gen, pret, tip_reducere_client):
    '''
    Adauga la lista de carti o carte noua.
    :param lista_carti: lista de carti
    :param id_carte: id-ul cartii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere_client: tipul reducerii de client (silver, gold, none)
    :return: o lista de carti ce contine noua carte pe care vrem sa o adaugam
    '''

    carte = create_book(id_carte, titlu, gen, pret, tip_reducere_client)
    return lista_carti + [carte]

def read(lista_carti, id_carte):
    '''
    Citeste o carte din lista de carti.
    :param lista_carti: lista de carti
    :param id_carte: id-ul cartii
    :return: cartea daca aceasta exista in lista de carti sau lista de carti daca aceasta nu exista
    '''
    carte_id = None
    for carte in lista_carti:
        if get_id(carte) == id_carte:
            carte_id = carte

    if carte_id:
        return carte_id
    else:
        return None


def delete(lista_carti, id_carte):
    '''
    Sterge o carte din lista de carti.
    :param lista_carti: lista initiala de carti
    :param id_carte: id-ul cartii pe care vrem sa o stergem
    :return: o lista de carti fara cartea cu id-ul id_carte
    '''

    lista_noua = []

    for carte in lista_carti:
        if get_id(carte) != id_carte:
            lista_noua.append(carte)

    return lista_noua

def update(lista_carti, carte_noua):
    '''
    Actualizeaza o carte din lista de carti
    :param lista_carti: lista initiala de carti
    :param carte_noua: cartea pe care o actualizam
    :return: o lista cu cartea actualizata
    '''

    lista_noua = []
    for carte in lista_carti:
        if get_id(carte) == get_id(carte_noua):
            lista_noua.append(carte_noua)
        else:
            lista_noua.append(carte)

    return lista_noua



