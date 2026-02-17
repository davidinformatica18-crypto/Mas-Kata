import pytest

def string_sumar(numeros):

    if numeros =="":
        return 0

lista = numeros.split(",")

total = 0

for n in lista:
    total += int(cifras)

    return total

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_string_vacio():
    assert string_sumar("") == 0

def test_uno_numero():
    assert string_sumar("1") == 1

def test_dos_numero():
    assert string_suma("1,2") == 3

def test_tres_numero():
    assert string_suma("1,2,3") == 6
