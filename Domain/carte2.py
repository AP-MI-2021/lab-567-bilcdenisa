def create_book(id_carte: int, titlu, gen, pret, tip_reducere_client):
    '''
    Creeaza o carte.
    :param id_carte: id-ul cartii, trebuie sa fie unic
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere_client: tipul de reducere client -poate fi: none, silver, gold
    :return: o carte
    '''
    tuple = (id_carte, titlu, gen, pret, tip_reducere_client)
    return tuple

def get_id(carte):
    '''
    Getter pentru id-ul cartii.
    :param carte: cartea
    :return: id-ul cartii data prin parametru
    '''
    return carte[0]

def get_titlu(carte):
    '''
    Getter pentru titlul cartii.
    :param carte: cartea
    :return: titlul cartii data ca parametru
    '''

    return carte[1]

def get_gen(carte):
    '''
    Getter pentru genul cartii.
    :param carte: cartea
    :return: genul cartii data ca parametru
    '''

    return carte[2]

def get_pret(carte):
    '''
    Getter pentru pretul cartii.
    :param carte: cartea
    :return: pretul cartii data ca parametru
    '''

    return carte[3]

def get_tip_reducere(carte):
    '''
    Getter pentru tipul de reducere al cartii.
    :param carte: cartea
    :return: tipul de reducere client in urma vanzarii cartii transmisa prin parametru
    '''

    return carte[4]

def get_str_carte(carte):
    '''
    Getter pentru reprezentarea de tip string a unei carti.
    :param carte: cartea
    :return: reprezentarea de tip string a cartii
    '''
    return f'Cartea cu id-ul {get_id(carte)}, cu titlul {get_titlu(carte)}, din genul {get_gen(carte)}, cu pretul {get_pret(carte)} si tipul de reducere client{get_tip_reducere(carte)}.'