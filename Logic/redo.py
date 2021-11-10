

def redo(lista_versiuni, versiune_curenta):
    '''
    Revine la operatiunea de dinaintea stergerii.
    :param lista_versiuni: lista de versiuni anterioare
    :param versiune_curenta: versiunea curenta la care ma aflu
    :return: versiunea de pe pozitia versiune_curenta+1 din lista_versiuni
    '''

    if versiune_curenta != len(lista_versiuni) - 1:
        versiune_curenta = versiune_curenta + 1
        return lista_versiuni[versiune_curenta], versiune_curenta
    else:
        return lista_versiuni[versiune_curenta], versiune_curenta