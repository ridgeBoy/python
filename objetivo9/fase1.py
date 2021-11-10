# print(3/0)

print("---")

try:
    print(3/0)
except:
    print("ERROR: Division por cero")

print("---")

print("Iniciando programa")
try:
    print(3/0)
except:
    print("ERROR: Division errónea")
finally:
    print("Programa acabado")

print("---")

print("Iniciando programa")
try:
    print(3/1)
except:
    print("ERROR: Division errónea")
finally:
    print("Programa acabado")

print("---")

print("Iniciando programa")
try:
    print(3/1)
except:
    print("ERROR: Division errónea")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado")

print("---")

print("Iniciando programa")
try:
    print(3/0)
except:
    print("ERROR: Division errónea")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado")

print("---")

print("Iniciando programa")
try:
    print(3/0)
except ZeroDivisionError:
    print("ERROR: Division errónea")
except:
    print("ERROR: general")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado")









