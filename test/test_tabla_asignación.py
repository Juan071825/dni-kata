import pytest

def test_getTabla(tabla):

    assert tabla.getTabla() == [
        "T",
        "R",
        "W",
        "A",
        "G",
        "M",
        "Y",
        "F",
        "P",
        "D",
        "X",
        "B",
        "N",
        "J",
        "Z",
        "S",
        "Q",
        "V",
        "H",
        "L",
        "C",
        "K",
        "E",
    ]

def test_getLetra(tabla):
    assert tabla.getLetra(4) == "G"
    assert tabla.getLetra(12) == "N"
    assert tabla.getLetra(32) == "Posicion letra fuera de rango"