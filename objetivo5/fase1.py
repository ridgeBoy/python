def Saludar():
    print("Hola")
Saludar()

print("")

def esMayorQueCero(param):
    if param >0:
        print(param,"es mayor que cero")
    else:
        print(param, "no es mayor que cero")

numero = int(input("Introduce un número:"))
esMayorQueCero(numero)

print("")

def sumar(param1, param2):
    return param1+ param2

sumando1 = int(input("Interoduce el primer sumando: "))
sumando2 = int(input("Introduce el segundo sumando: "))
resultado = sumar(sumando1, sumando2)

print("El resultado de la suma es:", resultado)

print("")

def sumarRestar(param1, param2):
    return param1 + param2, param1 - param2

numero1 = int(input("Interoduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
resultadoSuma, resultadoResta = sumarRestar(numero1, numero2)

print("El resultado de la suma es:", resultadoSuma)
print("El resultado de la resta es:", resultadoResta)

print("")

def sumar(*valores):
    resultado =0
    for item in valores:
        resultado = resultado + item

    return resultado

resultado = sumar(23,56,3,89,78,455)
print("El resultado de la suma es:", resultado)