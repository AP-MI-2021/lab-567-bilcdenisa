from Domain.carte import get_tip_reducere, get_pret, create_book, get_titlu, get_id, get_gen


def discount(lista_carti):


    if len(lista_carti)== 0:
        raise ValueError('Lista de carti nu poate fi goala')

    lista_noua = []

    for carte in lista_carti:
        if get_tip_reducere(carte) == 'silver':
            pret = get_pret(carte) * (100-5)/100
            carte_noua = create_book(get_id(carte), get_titlu(carte), get_gen(carte), pret, get_tip_reducere(carte))
            lista_noua.append(carte_noua)

        elif get_tip_reducere(carte) == 'gold':
            pret = get_pret(carte) * (100 - 10) / 100
            carte_noua = create_book(get_id(carte), get_titlu(carte), get_gen(carte), pret, get_tip_reducere(carte))
            lista_noua.append(carte_noua)
        else:
            lista_noua.append(carte)


    return lista_noua

