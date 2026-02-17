from main import string_calculator


def test_string_vacio():
    assert string_calculator("") == 0


def test_uno_numero():
    assert string_calculator("1") == 1


def test_dos_numero():
    assert string_calculator("1,2") == 3


def test_tres_numero():
    assert string_calculator("1,2,3") == 6

def test_separador_salto():
    assert string_calculator("1\n2,3") == 6
