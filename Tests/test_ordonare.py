from Domain.carte import create_book
from Logic.ordonare import ordonare


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 105.50, 'silver'),
        create_book(3, 'titlu3', 'gen3', 112, 'gold'),
        create_book(4, 'titlu4', 'gen4', 40.13, 'none'),
    ]

def test_ordonare():
    lista = get_data()
    lista_ordonata = ordonare(lista)
    assert lista[0] == lista_ordonata[0]
    assert lista[2]== lista_ordonata[3]
    assert len(lista) == len(lista_ordonata)

    lista2 = []
    try:
        lista2 = ordonare(lista2)
        assert False
    except ValueError:
        assert True