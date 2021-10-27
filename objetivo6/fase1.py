class Punto:
    def __init__(self, x,y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y,")")

p1 = Punto(4,6)
p1.mostrarPunto()

print("")

class Punto:
    def __init__(self, x,y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y,")")

p1 = Punto(4,6)
p2 = Punto(-5,9)
p3 = Punto(3,-7)
p4 = Punto(0,4)
p1.mostrarPunto()
p2.mostrarPunto()
p3.mostrarPunto()
p4.mostrarPunto()

print("")

class Punto:
    def __init__(self, x,y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y,")")

p1 = Punto(4,6)
p1.mostrarPunto()
p1.X = 7
p1.mostrarPunto()

print("")

class Punto:
    def __init__(self, x,y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El punto es (", self.X, ",", self.Y,")")

p1 = Punto(4,6)
p1.mostrarPunto()
p2 = Punto(3,8)
p2.mostrarPunto()
p1 = p2
p1.mostrarPunto()

print("")