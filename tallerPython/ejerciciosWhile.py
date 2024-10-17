# 2.1 Elabore usando ciclo while, una secuencia de números del 1 al 20 
# impreso de manera inversa

print("\n ******Ejercicio 2.1*****************")
numero = 20
while numero >= 1:
    print(numero, end=" ")
    numero -= 1

# 2.2 Elabore un algoritmo que imprima los números de 2 en 2 hasta el 50

print("\n ******Ejercicio 2.2*****************")
numero50 = 2
while numero50 <= 50:
    print(numero50, end=" ")
    numero50 += 2

# 2.3 Elabore un programa cuenta el número de vocales en una cadena ingresada
# por el usuario.

print("\n ******Ejercicio 2.3*****************")

cadena = input("Ingrese una palabra: ").lower()
vocales = "aeiou"
contador = 0
indice = 0

while indice < len(cadena):
    if cadena[indice] in vocales:
        contador += 1
    indice += 1

print(f"El número de vocales en la cadena es: {contador}")

# 2.4 Elabore un programa para simular el tirar un dado hasta que se obtenga un 6.
# (import random -> randint()

print("\n ******Ejercicio 2.4*****************")

import random

tirar_dado = 0
resultado = 0

while resultado != 6:
    resultado = random.randint(1, 6)
    tirar_dado += 1
    print(f"Tirada {tirar_dado}: {resultado}")

print(f"¡Se obtuvo un 6 después de {tirar_dado} tiradas!")

# 2.5 programa que suma los dígitos de un número ingresado por el usuario.

print("\n ******Ejercicio 2.5*****************")

numero_s = int(input("Ingrese un número de dos digitos: "))
suma = 0

while numero_s > 0:
    digito = numero_s % 10
    suma += digito
    numero_s //= 10

print(f"La suma de los dígitos es: {suma}")