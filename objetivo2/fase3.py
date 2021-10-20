lista = ["ordenador", "teclado", "raton"]
print(lista)

print("")

lista = ["ordenador", "teclado", "raton"]
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])

print("")

listaoriginal = ["ordenador", "teclado", "raton"]
listanueva = ["monitor", "impresora", "altavoces"]
listafinal = listaoriginal + listanueva
print(listafinal)

print("")

lista = ["ordenador", "teclado", "raton"]
print(lista)
lista = lista + ["mesa"]
print(lista)

print("")

lista = ["ordenador", "teclado", "raton"]
print(lista)
lista[0] = "monitor"
lista[1] = "impresora"
lista[2] = "altavoces"
print(lista)

print("")

lista = ["ordenador", "teclado", "raton"]
print(lista)
del lista[1]
print(lista)

print("")

lista = ["ordenador", "teclado", "raton", ["tarjeta de crédito", "microfono", "altavoces"]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[3][2])

print("")

tupla = ("ordenador","teclado","raton")
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])

'''
# esto da error
tupla[1] = "yeah"
'''

print("")

mesestraducidos = {
    "Enero":"January",
    "Febrero":"February",
    "Marzo":"March",
    "Abril":"April",
    "Mayo":"May",
    "Junio":"June",
    "Julio":"July",
    "Agosto":"August",
    "Septiembre":"September",
    "Octubre":"October",
    "Noviembre":"November",
    "Diciembre":"December"
}

print(mesestraducidos["Noviembre"])
print(mesestraducidos["Mayo"])






