
def undo(lista_versiuni, versiune_curenta):
    '''
    Sterge ultima operatiune fscuta.
    :param lista_versiuni: lista de versiuni anterioare
    :param versiune_curenta: versiunea curenta la care ma aflu
    :return: versiunea de pe pozitia versiune_curenta-1 din lista_versiuni
    '''
    if versiune_curenta == 0 and lista_versiuni[0] == []:
        return [], 0
    elif versiune_curenta == 0 and lista_versiuni[0] != []:
        return lista_versiuni[0]
    versiune_curenta = versiune_curenta - 1
    return lista_versiuni[versiune_curenta], versiune_curenta

