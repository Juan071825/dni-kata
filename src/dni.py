from src.tablaEquivalencias import TablaEquivalencias


class Dni:
    def __init__(self, dni: str):
        self.dni = dni
        self.tabla = TablaEquivalencias()

    def getDni(self):
        return self.dni
    
    