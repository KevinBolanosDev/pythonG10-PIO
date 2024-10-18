# 4.1 Función lambda para sumar dos números

print("\n ******Ejercicio 4.1*****************")

suma = lambda a, b: a + b

print("Suma de a + b:", suma(3, 5))


# 4.2 Función lambda para verificar si un número es par

print("\n ******Ejercicio 4.2*****************")

es_par = lambda x: x % 2 == 0

print("¿Es 4 par?:", es_par(4))


# 4.3 Ordenar una lista de tuplas por el segundo elemento

print("\n ******Ejercicio 4.3*****************")

lista_tuplas = [(1, 5), (3, 2), (2, 8), (4, 1)]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])

print("Lista ordenada:", lista_ordenada)

# 4.4 Filtrar números mayores a 10

print("\n ******Ejercicio 4.4*****************")

numeros = [5, 12, 3, 18, 7, 24, 9]
mayores_a_10 = list(filter(lambda x: x > 10, numeros))

print("Números mayores a 10:", mayores_a_10)

# 4.5 Elevar cada número al cuadrado

print("\n ******Ejercicio 4.5*****************")

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))

print("Números al cuadrado:", cuadrados)

