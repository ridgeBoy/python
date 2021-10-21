cadenaejemplo = "en un lugar de la mancha..."
print(cadenaejemplo.capitalize())

print("")

print(cadenaejemplo.upper())

print("")

print(cadenaejemplo.lower())

print("")

print(len(cadenaejemplo))

print("")

cadenaejemplo = "en un lugar de la mancha..."
print(cadenaejemplo.isalnum())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg1234567890"
print(cadenaejemplo.isalnum())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalnum())

print("")

cadenaejemplo = "enunlugardelamancha"
print(cadenaejemplo.isalpha())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isalpha())
cadenaejemplo = "abcdefg1234567890"
print(cadenaejemplo.isalpha())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isalpha())

print("")

cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.isdigit())
cadenaejemplo = "1234567890"
print(cadenaejemplo.isdigit())
cadenaejemplo = "abcdefg 1234567890"
print(cadenaejemplo.isdigit())

print("")

cadenaejemplo = "En un lugar de la mancha"
print(cadenaejemplo.islower())
cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.islower())

print("")

cadenaejemplo = "En un lugar de la mancha"
print(cadenaejemplo.isupper())
cadenaejemplo = "EN UN LUGAR DE LA MANCHA"
print(cadenaejemplo.isupper())

print("")

cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.lstrip())
cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.rstrip())
cadenaejemplo = "en un lugar de la mancha"
print(cadenaejemplo.strip())

print("")

cadenaejemplo = "abcdefghijklmnopqrstuvwxyz"
print(max(cadenaejemplo))
print(min(cadenaejemplo))

print("")

cadenaejemplo = "AEIOU"
print(cadenaejemplo.replace('A','E'))

print("")

cadenaejemplo = "En un lugar de la mancha"
print(cadenaejemplo.swapcase())

print("")

cadenaejemplo = "En un lugar de la mancha"
print(cadenaejemplo.split())

print("")

cadenaejemplo = "31/12/20217"
print(cadenaejemplo.split("/"))

