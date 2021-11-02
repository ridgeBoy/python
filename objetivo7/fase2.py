class Electrodomestico:
    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0

    def Encender(self):
        self.__Encendido=True

    def Apagar(self):
        self.__Encendido=False

    def Encendido(self):
        return self.__Encendido

    def SetTension(self, tension):
        self.__Tension = tension

    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0

    def setRPM(self,rpm):
        self.__RPM = rpm

    def setKilos(self,kilos):
        self.__Kilos = kilos

    def MostrarLavadora(self):
        print("############")
        print("Lavadora:")
        print("\tRPM: ", self.__RPM)
        print("\tKilos: ", self.__Kilos)
        print("\tTension: ", self.GetTension())

        if self.Encendido():
            print("\tLavadora encendida")
        else:
            print("\tLavadora no encendida")

        print("############")

lavadora = Lavadora()
lavadora.setRPM(1200)
lavadora.setKilos(7)
lavadora.SetTension(220)

lavadora.Encender()
lavadora.MostrarLavadora()

print("")

class Microondas(Electrodomestico):
    def __init__(self):
        self.__PotenciaMaxima = 0
        self.__Grill = False

    def SetPotenciaMaxima(self, potencia):
        self.__PotenciaMaxima = potencia

    def SetGrill(self, grill):
        self.__Grill = grill

    def MostrarMicroondas(self):
        print("############")
        print("Microondas:")
        print("\tPotencia maxima: ", self.__PotenciaMaxima)

        if self.__Grill == True:
            print("\tGrill: si")
        else:
            print("\tGrill: no")

        print("\tTension: ", self.GetTension())

        if self.Encendido():
            print("\tMicroondas encendido")
        else:
            print("\tMicroondas no encendido")

        print("############")

microondas = Microondas()
microondas.SetPotenciaMaxima(800)
microondas.SetGrill(True)
microondas.SetTension(220)
microondas.Apagar()
microondas.MostrarMicroondas()
