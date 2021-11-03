from Domain.carte import create_book, get_gen, get_titlu
from Logic.modificare_gen import modificare_gen


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 17, 'silver'),
        create_book(3, 'titlu3', 'gen4', 105.50, 'silver'),
        create_book(4, 'titlu4', 'gen4', 59.99, 'none'),
        create_book(5, 'titlu5', 'gen3', 32, 'gold'),
        create_book(6, 'titlu6', 'gen2', 44.50, 'none'),
    ]

def test_modificare_gen():
    lista_carti = get_data()
    id = 3
    titlu = 'titlu3'
    gen = 'gen1'
    lista_noua = modificare_gen(lista_carti, id, gen, titlu)
    assert len(lista_carti) == len(lista_noua)
    assert get_gen(lista_carti[2]) != get_gen(lista_noua[2])
    assert get_titlu(lista_carti[2]) == get_titlu(lista_noua[2])
    assert get_gen(lista_noua[2]) == 'gen1'
    id2 = 7
    titlu2 = 'titlu1'
    gen2 = 'gen1'
    try:
        modificare_gen(lista_carti,id2,titlu2,gen2)
        assert False
    except ValueError:
        assert True