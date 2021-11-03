from Domain.carte import create_book
from Logic.determinare_pret_minim import determinare_pret_minim


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 17, 'silver'),
        create_book(3, 'titlu3', 'gen4', 105.50, 'silver'),
        create_book(4, 'titlu4', 'gen4', 59.99, 'none'),
        create_book(5, 'titlu5', 'gen3', 32, 'gold'),
        create_book(6, 'titlu6', 'gen2', 44.50, 'none'),
    ]

def test_determinare_pret_minim():
    lista_carti = get_data()
    lista_preturi_minime = determinare_pret_minim(lista_carti)
    assert lista_preturi_minime[0][1] == 35
    assert lista_preturi_minime[2][1] == 59.99
    assert len(lista_preturi_minime) == 4

    lista_carti_2 = []
    try:
        determinare_pret_minim(lista_carti_2)
        assert False
    except ValueError:
        assert True


