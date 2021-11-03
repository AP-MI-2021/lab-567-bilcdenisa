from Domain.carte import create_book, get_pret
from Logic.reducere import discount


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 105.50, 'silver'),
        create_book(3, 'titlu3', 'gen3', 112, 'gold'),
        create_book(4, 'titlu4', 'gen4', 40.13, 'none'),
        create_book(5, 'titlu5', 'gen4', 100, 'gold'),
        create_book(6, 'titlu6', 'gen4', 60, 'silver'),
    ]

def test_reducere():
    carti = get_data()
    lista_cu_reducere = discount(carti)
    assert len(carti) == len(lista_cu_reducere)
    assert get_pret(lista_cu_reducere[4]) == 90
    assert get_pret(lista_cu_reducere[5]) == 57
    assert get_pret(lista_cu_reducere[0]) == 35

    carti2 = []
    try:
        discount(carti2)
        assert False
    except ValueError:
        assert True