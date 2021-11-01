from Domain.carte import get_gen, get_pret


def determinare_pret_minim(lista_carti):
    '''
    Determinarea pretului minim pentru fiecare gen.
    :param lista_carti: lista de carti
    :return: o lista de tupluri, in care fiecare tuplu contine un gen din lista de carti si pretul minim pentru acest gen
    '''

    if len(lista_carti)== 0:
        raise ValueError('Lista de carti nu poate fi goala')

    lista_genuri = []

    for carte in lista_carti:
        if get_gen(carte) not in lista_genuri:
            lista_genuri.append(get_gen(carte))

    lista_preturi_minime = []

    for gen in lista_genuri:
        for carte in lista_carti:
            if get_gen(carte) == gen:
                pret_minim = get_pret(carte)
                break

        for carte in lista_carti:
            if get_gen(carte) == gen and get_pret(carte)<pret_minim:
                pret_minim = get_pret(carte)

        lista_preturi_minime.append((gen,pret_minim))

    return lista_preturi_minime


