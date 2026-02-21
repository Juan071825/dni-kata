class TablaEquivalencias():

    def __init__(self):
        self.tabla = [
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
            "E"
        ]

    def getTabla(self):
        return self.tabla
    
    def getLetra(self, clave):
        try:
            return self.tabla[clave]
        except IndexError:
            return "La letra no es válida."
    
    def getModulo(self):
        return len(self.tabla)
    
    def isLetraValida(self, letra):
        return letra in self.tabla
    
    def calcularLetra(self, numero_dni):
        posicion = int(numero_dni) % self.getModulo()
        return self.getLetra(posicion)

    
    def __repr__(self):
        return str(self.tabla)
    

    

if __name__ == '__main__':
    tabla = TablaEquivalencias()
    print(tabla)
