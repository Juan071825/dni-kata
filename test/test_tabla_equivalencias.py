import pytest
from src.tablaEquivalencias import TablaEquivalencias
from test.test_dni_correctos import TEST_DNI_VALIDOS
from test.test_dni_incorrectos import TEST_DNI_LETRA_ERRONEA

@pytest.fixture(name="tabla")
def tablaEquivalencias():
    return TablaEquivalencias()

def test_getTabla(tabla):

    assert tabla.getTabla() == (
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
        )

def test_getLetra(tabla):
    assert tabla.getLetra(4) == "G"
    assert tabla.getLetra(12) == "N"
    assert tabla.getLetra(32) == "Posicion letra fuera de rango"

def test_getModulo(tabla):
    assert tabla.getModulo() == 23

def test_isLetraValida(tabla):
    assert tabla.isLetraValida("T")
    assert not tabla.isLetraValida("I")

@pytest.mark.parametrize("dni", TEST_DNI_VALIDOS)
def test_calcularLetra_correcta(tabla, dni):
    numero_dni = dni[:-1]
    letra_dni = dni[-1]
    assert tabla.calcularLetra(numero_dni) == letra_dni

@pytest.mark.parametrize("dni", TEST_DNI_LETRA_ERRONEA)
def test_calcularLetra_correcta(tabla, dni):
    numero_dni = dni[:-1]
    letra_dni = dni[-1]
    assert tabla.calcularLetra(numero_dni) != letra_dni