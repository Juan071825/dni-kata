import pytest
from src.tablaEquivalencias import TablaEquivalencias

@pytest.fixture(name="tabla")
def tablaEquivalencias():
    return TablaEquivalencias()