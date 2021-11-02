class PuntoPublico:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class PuntoPrivado:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y


publico = PuntoPublico(4,6)
privado = PuntoPrivado(7,3)

print("valores punto publico: ", publico.X, ",", publico.Y)
print("valores punto privado: ", privado.GetX(), ",", privado.GetY())

publico.X = 2
privado.SetX(9)

print("valores punto publico: ", publico.X, ",", publico.Y)
print("valores punto privado: ", privado.GetX(), ",", privado.GetY())

print("")

class OperarValores:
    def __init__(self,v1,v2):
        self.__V1 = v1
        self.__V2 = v2
    def __Sumar(self):
        return self.__V1 + self.__V2
    def __Restar(self):
        return self.__V1 - self.__V2
    def Operar(self):
        print("El resultado de la suma es: ", self.__Sumar())
        print("El resultado de la resta es: ", self.__Restar())

operarValores = OperarValores(7,3)
operarValores.Operar()

print("")

class OperarValores:
    def __init__(self,v1,v2):
        self.__V1 = v1
        self.__V2 = v2
    def __Sumar(self):
        return self.__V1 + self.__V2
    def __Restar(self):
        return self.__V1 - self.__V2
    def Operar(self):
        print("El resultado de la suma es: ", self.__Sumar())
        print("El resultado de la resta es: ", self.__Restar())

operarValores = OperarValores(7,3)
operarValores.Operar()
print("el resultado de la suma es: ", operarValores.__Sumar())