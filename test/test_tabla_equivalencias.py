import pytest
from tablaEquivalencias import TablaEquivalencias

@pytest.fixture(name="tabla")
def tablaEquivalencias():
    return TablaEquivalencias()

def test_getTabla(tabla):

    assert tabla.getTabla() == {
            "T": 0,
            "R": 1,
            "W": 2,
            "A": 3,
            "G": 4,
            "M": 5,
            "Y": 6,
            "F": 7,
            "P": 8,
            "D": 9,
            "X": 10,
            "B": 11,
            "N": 12,
            "J": 13,
            "Z": 14,
            "S": 15,
            "Q": 16,
            "V": 17,
            "H": 18,
            "L": 19,
            "C": 20,
            "K": 21,
            "E": 22,
        }

def test_getLetra(tabla):
    assert tabla.getLetra(4) == "G"
    assert tabla.getLetra(12) == "N"
    assert tabla.getLetra(32) == "Posicion letra fuera de rango"

def test_getModulo(tabla):
    assert tabla.getModulo() == 23

def test_isLetraValida(tabla):
    assert tabla.isLetraValida("T")
    assert not tabla.isLetraValida("I")




