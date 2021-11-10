
def lista_noua(lista_versiuni, versiune_curenta, lista_carti):
    '''
    Adauga la o lista de versiuni o noua lista.
    :param lista_versiuni: lista de versiuni anterioare
    :param versiune_curenta: versiunea curenta la care ma aflu
    :param lista_carti: lista de carti pe care o adaug la lista_versiuni
    :return: lista_versiuni in urma adaugarii lista_versiuni si incrementeaza valoarea parametrului versiune_curenta
    '''

    while versiune_curenta < len(lista_versiuni)-1:
        lista_versiuni.pop()

    lista_versiuni.append(lista_carti)
    versiune_curenta = versiune_curenta + 1
    return lista_versiuni, versiune_curenta