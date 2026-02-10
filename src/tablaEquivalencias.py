class TablaEquivalencias():

    def __init__(self):
        self.tabla = (
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

    def getTabla(self):
        return self.tabla
    
    def getLetra(self, index):
        try:
            return self.tabla[index]
        except IndexError:
            return "Posicion letra fuera de rango"
    
    def getModulo(self):
        return len(self.tabla)
    
    def isLetraValida(self, letra):
        return letra in self.getTabla()

    def calcularLetra(self, dni):
        numero_dni = dni[:-1]
        posicion = int(numero_dni) % self.getModulo()
        return self.getLetra(posicion)

    
    def __repr__(self):
        return str(self.tabla)
