# Elabore un programa suma los cubos de los números del 1 al 50.
suma_cubos = sum(i**3 for i in range(1, 51))
print(f"La suma de los cubos del 1 al 50 es: {suma_cubos}")

# 3.2 Elaborar una pirámide de estrellas (matriz)
altura = 5
for i in range(altura):
    for j in range(altura * 2 - 1):
        if j >= altura - i - 1 and j < altura + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 3.3 Simular un tablero de ajedrez
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()

# 3.4 Invertir una cadena ingresada por el usuario
cadena = input("Ingrese una cadena: ")
cadena_invertida = ""
for char in cadena:
    cadena_invertida = char + cadena_invertida
print(f"La cadena invertida es: {cadena_invertida}")

# 3.5 Buscar una palabra en una lista de palabras
lista_palabras = ["carro", "barco", "avión", "tren", "bicicleta", "carromoto"]
palabra_buscar = "carro"
coincidencias = []

for i, palabra in enumerate(lista_palabras):
    if palabra_buscar in palabra:
        coincidencias.append((i, palabra))

if coincidencias:
    print(f"La palabra '{palabra_buscar}' se encuentra en:")
    for posicion, palabra in coincidencias:
        print(f"  Posición {posicion}: {palabra}")
else:
    print(f"La palabra '{palabra_buscar}' no se encuentra en ninguna palabra de la lista")






