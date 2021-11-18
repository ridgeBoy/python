class Direccion:
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""

    def GetCalle(self):
        return self.__Calle

    def GetPiso(self):
        return self.__Piso

    def GetCiudad(self):
        return self.__Ciudad

    def GetCodigoPostal(self):
        return self.__CodigoPostal

    def SetCalle(self, calle):
        self.__Calle = calle

    def SetPiso(self, piso):
        self.__Piso = piso

    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad

    def SetCodigoPostal(self, codigopostal):
        self.__CodigoPostal = codigopostal

class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaNacimiento = ""

    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetFechaNacimiento(self):
        return self.__FechaNacimiento

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetFechaNacimiento(self, fechanacimiento):
        self.__FechaNacimiento = fechanacimiento

class Telefono:
    def __init__(self):
        self.__TelefonoMovil = ""
        self.__TelefonoFijo = ""
        self.__TelefonoTrabajo = ""

    def GetTelefonoMovil(self):
        return self.__TelefonoMovil

    def GetTelefonoFijo(self):
        return self.__TelefonoFijo

    def GetTelefonoTrabajo(self):
        return self.__TelefonoTrabajo

    def SetTelefonoMovil(self, telefonomovil):
        self.__TelefonoMovil = telefonomovil

    def SetTelefonoFijo(self, telefonofijo):
        self.__TelefonoFijo = telefonofijo

    def SetTelefonoTrabajo(self, telefonotrabajo):
        self.__TelefonoTrabajo = telefonotrabajo

class Contacto(Persona, Direccion, Telefono):
    def __init__(self):
        self.__Email = ""

    def GetEmail(self):
        self.__Email

    def SetEmail(self,email):
        self.__Email = email

    def MostrarContacto(self):
        print("------- Contacto -------")
        print("Nombre:", self.GetNombre())
        print("Apellidos:", self.GetApellidos())
        print("Fecha de nacimiento:", self.GetFechaNacimiento())
        print("Telefono movil:", self.GetTelefonoMovil())
        print("Telefono fijo:", self.GetTelefonoFijo())
        print("Telefono trabajo:", self.GetTelefonoTrabajo())
        print("Calle:", self.GetCalle())
        print("Piso:", self.GetPiso())
        print("Ciudad:", self.GetCiudad())
        print("Codigo postal:", self.GetCodigoPostal())
        print("Email:", self.GetEmail())
        print("--------------")


