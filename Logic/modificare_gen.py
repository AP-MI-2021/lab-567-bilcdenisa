from Domain.carte import create_book, get_pret, get_tip_reducere
from Logic.crud import update, read


def modificare_gen(lista_carti, id_carte, gen_carte, titlu_carte):
    '''
    Modificarea genului pentru un titlu dat.
    :param lista_carti: lista initiala de carti
    :param id_carte: id-ul cartii
    :param gen_carte: genul cartii
    :param titlu_carte: titlul cartii
    :return: o lista in care genul cartii cu id-ul id_carte si titlul titlu_carte este modificat in gen_carte
    '''

    if gen_carte == '' or titlu_carte == '':
        raise ValueError('Genul sau titlul nu pot fi texte goale')

    carte = read(lista_carti, id_carte)

    if carte is None:
        raise ValueError('Id-ul trebuie sa existe in lista de carti')

    carte_noua = create_book(id_carte, titlu_carte, gen_carte, get_pret(carte), get_tip_reducere(carte))
    lista_modificata = update(lista_carti, carte_noua)
    return lista_modificata
