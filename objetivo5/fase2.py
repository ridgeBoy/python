def sumarRestar(param1, param2):
    return sumar(param1, param2), restar(param1, param2)

def sumar(sumando1, sumando2):
    return sumando1+sumando2

def restar(minuendo, sustraendo):
    return minuendo - sustraendo

numero1 = int(input("Introduce el primer número:"))
numero2 = int(input("Introduce el segundo número:"))

resultadoSuma, resultadoResta  = sumarRestar(numero1, numero2)

print("El resultado de la suma es:", resultadoSuma)
print("El resultado de la resta es:", resultadoResta)

print("")


