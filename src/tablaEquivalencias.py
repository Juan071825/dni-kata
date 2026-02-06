class TablaEquivalencias():

    def __init__(self):
        self.tabla = {
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

    def getTabla(self):
        return self.tabla
    
    def __repr__(self):
        return str(self.tabla)
    
    
    

if __name__ == '__main__':
    tabla = TablaEquivalencias()
    print(tabla)
