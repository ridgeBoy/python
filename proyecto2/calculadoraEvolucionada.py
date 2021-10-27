def sumar():
    sum1 = int(input("sumando 1:"))
    sum2 = int(input("sumando 2:"))
    print("La suma es: ", sum1+sum2)

def restar():
    minuendo = int(input("minuendo: "))
    sustraendo = int(input("sustraendo:"))
    print("La resta es: ", minuendo - sustraendo)

def multiplicar():
    multiplicando = int(input("multiplicando: "))
    multiplicador = int(input("multiplicador:"))
    print("El producto es: ", multiplicando * multiplicador)

def dividir():
    dividendo = int(input("dividendo: "))
    divisor = int(input("divisor:"))
    print("La división es: ", dividendo / divisor)

def calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if(opc == 1):
            sumar()
        elif(opc == 2):
            restar()
        elif(opc == 3):
            multiplicar()
        elif(opc == 4):
            dividir()
        elif(opc == 5):
            fin = 1

print("""**********
Calculadora
**********
Menu
1) Suma
2) Resta
3) Producto
4) Division
5) Salir""")
calculadora()