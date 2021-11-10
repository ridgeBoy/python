print("### Fichero original ###")
flectura = open("prueba.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)
print("### Insertando linea... ###\n")
fescritura = open("prueba.txt", "a")
fescritura.write("info@timesofsoftware.com\n")
fescritura.close()
print("### Fichero modificado ###")
flectura = open("prueba.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)

print("---")

fcrear = open("pruebacreacion.txt", "x")
fcrear.write("Times of Software\n")
fcrear.write("Fichero creado 8-2-2\n")
fcrear.close()

print("### Fichero creado ###")

flectura = open("pruebacreacion.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)

print("---")

fcrear = open("pruebacreacion.txt", "w")
fcrear.write("Fichero creado desde cero\n")
fcrear.write("Times of Software\n")
fcrear.write("Fichero creado 8-2-3\n")
fcrear.close()

print("### Fichero creado ###")

flectura = open("pruebacreacion.txt", "r")
texto = flectura.read()
flectura.close()
print(texto)