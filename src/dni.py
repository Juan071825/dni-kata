from src.tablaEquivalencias import TablaEquivalencias

class Dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        self.tabla = TablaEquivalencias()

    ### INTERFAZ PÚBLICA ###

    def setDni(self, cadena):
        self.dni = cadena

    def checkDni(self):
        self.__actualizarNumeroSano(self.__longitudCorrecta() and self.checkNumero())
        return self.getNumeroSano()

    def getDni(self):
        return self.dni

    def getNumeroSano(self):
        return self.numeroSano

    def getLetraSana(self):
        return self.letraSana

    def validarCompleto(self):
        return self.checkNumero() and self.checkLetra()

    def checkNumero(self):
        self.__actualizarNumeroSano(self.__longitudCorrecta() and self.__soloNumeros())
        return self.getNumeroSano()

    def checkLetra(self):
        if not self.getNumeroSano(): 
            self.__actualizarLetraSana(False) 
            return False 
        letra_real = self.tabla.calcularLetra(self.getParteNumericaDni()) 
        letra_dni = self.getParteAlfabeticaDni() 
        es_valida = letra_real == letra_dni 
        self.__actualizarLetraSana(es_valida) 
        return es_valida
        
    
        
    def obtenerLetra(self):
        if self.getNumeroSano():
            return self.tabla.calcularLetra(self.getParteNumericaDni())
        else:
            return None

    def __calcularLetra(self):
        if self.getNumeroSano():
            numero = self.getParteNumericaDni()
            return self.tabla.calcularLetra(numero)
        return None

    ### MÉTODOS PRIVADOS ###

    def __actualizarNumeroSano(self, valor):
        self.numeroSano = valor

    def __actualizarLetraSana(self, valor):
        self.letraSana = valor

    def __longitudCorrecta(self):
        return len(self.dni) == 9

    def __soloNumeros(self):
        return self.dni[:-1].isdigit()

    def getParteAlfabeticaDni(self):
        return self.dni[-1]

    def getParteNumericaDni(self):
        if self.getNumeroSano():
            return self.dni[:-1]
        else:
            return False
