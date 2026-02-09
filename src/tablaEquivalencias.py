class TablaEquivalencias():

    def __init__(self):
        self.tabla = (
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
        )

    def getTabla(self):
        return self.tabla
    
    def getLetra(self, letra):
        try:
            return self.tabla[letra]
        except KeyError:
            return "La letra no es válida."
    
    def getModulo(self):
        return len(self.tabla)
    
    def isLetraValida(self, letra):
        letra in self.tabla

    def calcularLetra(self, dni):
        numero_dni = dni[:-1]
        posicion = int(numero_dni) % self.getModulo()
        return self.getLetra(posicion)

    
    def __repr__(self):
        return str(self.tabla)
