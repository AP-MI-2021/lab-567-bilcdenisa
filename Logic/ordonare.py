from Domain.carte import get_pret


def ordonare(lista_carti):
    '''
    Ordoneaza o lista de carti crescator dupa pret.
    :param lista_carti: lista de carti initiala
    :return: lista ordonata
    '''

    if len(lista_carti) == 0:
        raise ValueError('Lista de carti nu poate fi goala')

    return sorted(lista_carti, key=get_pret)