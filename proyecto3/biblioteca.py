class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def mostrarAutor(self):
        print("Autor: ", self.Nombre, " ", self.Apellidos)

class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn

    def añadirAutor(self, autor):
        self.Autor = autor

    def mostrarLibro(self):
        print("------ Libro ------")
        print("Titulo: ", self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.mostrarAutor()
        print("-----------------")

    def obtenerTitulo(self):
        return self.Titulo

class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def numeroLibros(self):
        return len(self.ListaLibros)

    def añadirLibro(self, libro):
        self.ListaLibros = self.ListaLibros + [libro]

    def mostrarBiblioteca(self):
        print("####################################")
        for item in self.ListaLibros:
            item.mostrarLibro()
        print("####################################")

    def borrarLibro(self, titulo):
        encontrado = False
        posicionaBorrar = -1
        for item in self.ListaLibros:
            posicionaBorrar += 1
            if item.obtenerTitulo() == titulo:
                encontrado = True
                break

        if encontrado:
            del self.ListaLibros[posicionaBorrar]
            print("Libro borrado correctamente")
        else:
            print("Libro no encontrado")

def mostrarMenu():
    print(""" Menu
        1) Añadir libro a la biblioteca
        2) Mostrar biblioteca
        3) Borrar libro
        4) ¿Número de libros?
        5) Salir """)

def añadirLibroABiblioteca(biblioteca):
    titulo = input("Introduzca el titulo del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    autorNombre = input("Introduzca el nombre del autor: ")
    autorApellido = input("Introduzca el apellido del autor: ")

    autor = Autor(autorNombre, autorApellido)

    libro = Libro(titulo, isbn)

    libro.añadirAutor(autor)

    biblioteca.añadirLibro(libro)
    return biblioteca

def mostrarBiblioteca(biblioteca):
    biblioteca.mostrarBiblioteca()

def borrarLibro(biblioteca):
    titulo = input("Introduzca el título del libro a borrar: ")
    biblioteca.borrarLibro(titulo)

def numeroLibros(biblioteca):
    print("El número de libros en la biblioteca es: ", biblioteca.numeroLibros())

fin = False

biblioteca = Biblioteca()

while not fin:
    mostrarMenu()
    opcion = int(input("Seleccione opcion: "))

    if(opcion == 1):
        biblioteca = añadirLibroABiblioteca(biblioteca)
    elif(opcion == 2):
        mostrarBiblioteca(biblioteca)
    elif(opcion == 3):
        borrarLibro(biblioteca)
    elif(opcion == 4):
        numeroLibros(biblioteca)
    elif(opcion == 5):
        fin = True

print("¡Adios!")
