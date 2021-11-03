from Domain.carte import create_book, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        create_book(1, 'titlu1', 'gen1', 35, 'none'),
        create_book(2, 'titlu2', 'gen2', 105.50, 'silver'),
        create_book(3, 'titlu3', 'gen3', 112, 'gold'),
        create_book(4, 'titlu4', 'gen4', 40.13, 'none'),
    ]

def test_create():
    carti = get_data()
    parametrii = (5, 'titlu5', 'gen5', 78, 'none')
    carte_noua = create_book(*parametrii)
    carti_noi = create(carti, *parametrii)
    assert len(carti_noi) == len(carti)+1
    ok = False
    for carte in carti_noi:
        if carte == carte_noua:
            ok = True

    assert ok

    parametrii2 = (1, 'titlu1', 'gen1', 35, 'none')
    try:
        create(carti_noi, *parametrii2)
        assert False
    except ValueError:
        assert True

def test_read():
    carti = get_data()
    carte = carti[1]
    assert read(carti, get_id(carte)) == carte
    assert read(carti, 100) == None


def test_update():
    carti = get_data()
    carte_updated = create_book(2, 'titlu nou', 'gen nou', 98, 'silver')
    carti_updated = update(carti, carte_updated)
    assert carte_updated in carti_updated
    assert carte_updated not in carti
    assert len(carti_updated) == len(carti)

    carte_updated_2 = create_book(100, 'titlu nou2', 'gen nou2', 100, 'none')
    try:
        update(carti, carte_updated_2)
        assert False
    except ValueError:
        assert True


def test_delete():
    carti = get_data()
    de_sters = 3
    carte_de_sters = read(carti, de_sters)
    stearsa = delete(carti, de_sters)
    assert carte_de_sters not in stearsa
    assert carte_de_sters in carti
    assert len(stearsa) == len(carti)-1

    de_sters_2 = 100
    try:
        delete(carti, de_sters_2)
        assert False
    except ValueError:
        assert True


def test_crud():
    test_delete()
    test_update()
    test_read()
    test_create()


