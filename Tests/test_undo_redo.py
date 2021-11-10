from Domain.carte import get_pret, get_gen
from Logic.crud import create
from Logic.lista_noua import lista_noua
from Logic.modificare_gen import modificare_gen
from Logic.ordonare import ordonare
from Logic.redo import redo
from Logic.reducere import discount
from Logic.undo import undo
def test_undoRedo():
    lista = []
    lista_versiuni = [lista]
    versiune_curenta = 0
    lista = create(lista, 1, 'titlu1', 'gen1', 120, 'silver')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista = create(lista, 2, 'titlu2', 'gen2', 46, 'none')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista = create(lista, 3, 'titlu3', 'gen3', 50, 'gold')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)

    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 2
    assert lista[1] == {'id': 2, 'titlu': 'titlu2', 'gen': 'gen2', 'pret': 46, 'tip reducere': 'none'}
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 1
    assert lista[0] == {'id': 1, 'titlu': 'titlu1', 'gen': 'gen1', 'pret': 120, 'tip reducere': 'silver'}
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 0
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 0
    assert lista == []

    lista_versiuni = [[]]
    versiune_curenta = 0
    lista = create(lista, 1, 'titlu1', 'gen1', 120, 'silver')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista = create(lista, 2, 'titlu2', 'gen2', 46, 'none')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista = create(lista, 3, 'titlu3', 'gen3', 50, 'gold')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)


    lista, versiune_curenta = redo(lista_versiuni, versiune_curenta)
    assert len(lista) == 3
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 1
    lista = create(lista, 4, 'titlu4', 'gen4', 40, 'gold')
    assert len(lista) == 2
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista, versiune_curenta = redo(lista_versiuni, versiune_curenta)
    assert len(lista) == 2
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 1
    assert lista[0] == {'id': 1, 'titlu': 'titlu1', 'gen': 'gen1', 'pret': 120, 'tip reducere': 'silver'}
    lista, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert len(lista) == 0
    lista, versiune_curenta = redo(lista_versiuni, versiune_curenta)
    lista, versiune_curenta = redo(lista_versiuni, versiune_curenta)
    assert len(lista) == 2
    assert lista[0] == {'id': 1, 'titlu': 'titlu1', 'gen': 'gen1', 'pret': 120, 'tip reducere': 'silver'}
    assert lista[1] == {'id': 4, 'titlu': 'titlu4', 'gen': 'gen4', 'pret': 40, 'tip reducere': 'gold'}
    lista, versiune_curenta = redo(lista_versiuni, versiune_curenta)
    assert len(lista) == 2

    lista_carti = []
    versiune_curenta = 0
    lista_carti = create(lista_carti, 1, 'titlu1', 'gen1', 35, 'silver')
    lista_carti = create(lista_carti, 2, 'titlu2', 'gen2', 100, 'silver')
    lista_carti = create(lista_carti, 3, 'titlu3', 'gen1', 25, 'none')
    lista_versiuni = [lista_carti]

    lista_carti = discount(lista_carti)
    assert get_pret(lista_carti[1]) == 95
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista_carti)
    lista_carti, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert get_pret(lista_carti[1]) == 100

    lista_carti = modificare_gen(lista_carti, 2, 'gen1', 'titlu2')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista_carti)
    assert get_gen(lista_carti[1]) == 'gen1'
    lista_carti, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert get_gen(lista_carti[1]) == 'gen2'

    lista_carti = ordonare(lista_carti)
    assert get_pret(lista_carti[0]) == 25
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista_carti)
    lista_carti, versiune_curenta = undo(lista_versiuni, versiune_curenta)
    assert get_pret(lista_carti[0]) == 35


def test_lista_noua():
    lista = []
    lista_versiuni = [lista]
    versiune_curenta = 0
    lista = create(lista, 1, 'titlu1', 'gen1', 120, 'silver')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    lista = create(lista, 2, 'titlu2', 'gen2', 46, 'none')
    lista_versiuni, versiune_curenta = lista_noua(lista_versiuni, versiune_curenta, lista)
    assert len(lista_versiuni) == 3
    assert lista_versiuni[0] == []
    assert lista_versiuni[1] == [{'id': 1, 'titlu': 'titlu1', 'gen': 'gen1', 'pret': 120, 'tip reducere': 'silver'}]

def test_undo_redo():
    test_lista_noua()
    test_undoRedo()