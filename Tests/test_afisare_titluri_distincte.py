from Domain.carte import create_book
from Logic.afisare_titluri_distincte import titluri_distincte


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 105.50, 'silver'),
        create_book(3, 'titlu3', 'gen3', 112, 'gold'),
        create_book(4, 'titlu4', 'gen4', 40.13, 'gold'),
        create_book(5, 'titlu4', 'gen4', 40.13, 'none'),
        create_book(6, 'titlu4', 'gen2', 40.13, 'silver'),
        create_book(7, 'titlu5', 'gen4', 40.13, 'none'),
        create_book(8, 'titlu6', 'gen2', 40.13, 'gold'),
        create_book(9, 'titlu6', 'gen2', 40.13, 'none'),
        create_book(10, 'titlu7', 'gen1', 40.13, 'silver'),
    ]

def test_titluri_distincte():
    lista = get_data()
    lista_nr_titluri_distincte = titluri_distincte(lista)
    assert lista_nr_titluri_distincte[0][1] == 2
    assert len(lista_nr_titluri_distincte) == 4
    assert lista_nr_titluri_distincte[2][1] == 1
    lista2 = []

    try:
        lista_2 = titluri_distincte(lista2)
        assert False
    except ValueError:
        assert True