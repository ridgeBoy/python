f = open("prueba.txt", "r")
texto = f.read()
print(texto)
f.close()

print("---")

for linea in open("prueba.txt", "r"):
    print(linea)

print("---")

f = open("prueba.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print("---")

f = open("prueba.txt", "r")
lineas = f.readlines()
f.close()
print(lineas[0])
print(lineas[1])
print(lineas[2])
print(lineas[3])

print("---")

f = open("prueba.txt", "r")
lineas = f.readlines()
f.close()
for item in lineas:
    print(item)