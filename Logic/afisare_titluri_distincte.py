from Domain.carte import get_titlu, get_gen


def titluri_distincte(lista_carti):
    '''
    Creeaza o lista cu titlurile de carti distincte dintr-o lista de carti.
    :param lista_carti: lista de carti initiala
    :return: o lista noua cu titlurile de carti distincte din lista_carti
    '''

    if len(lista_carti) == 0:
        raise ValueError('Lista nu poate fi goala')

    lista_genuri = []
    lista_nr_titluri_distincte = []

    for carte in lista_carti:
        if get_gen(carte) not in lista_genuri:
            lista_genuri.append(get_gen(carte))

    for gen in lista_genuri:
        lista_titluri = []
        for carte in lista_carti:
            if get_gen(carte) == gen:
                titlu_carte = get_titlu(carte)
                ok = True
                contor = 0
                while ok == True and contor <= len(lista_titluri) - 1:
                    if titlu_carte == lista_titluri[contor]:
                        ok = False
                    else:
                        contor += 1

                if ok == True:
                    lista_titluri.append(titlu_carte)
        lista_nr_titluri_distincte.append((gen, len(lista_titluri)))

    return lista_nr_titluri_distincte