import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejercicio_1_3():
    print("\n****** Ejercicio 1.3 *****************")
    calificacion = float(input("Ingrese la calificación del estudiante: "))

    if calificacion > 4.5:
        print("Rendimiento: Excelente")
    elif 3.5 <= calificacion <= 4.5:
        print("Rendimiento: Bueno")
    elif 3 <= calificacion < 3.5:
        print("Rendimiento: Regular")
    elif 0 <= calificacion < 3:
        print("Rendimiento: Insuficiente")
    else:
        print("La calificación ingresada no es válida.")

def ejercicio_3_3():
    print("\n****** Ejercicio 3.3 *****************")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print("□", end=" ")
            else:
                print("■", end=" ")
        print()

def ejercicio_2_3():
    print("\n****** Ejercicio 2.3 *****************")
    cadena = input("Ingrese una palabra: ").lower()
    vocales = "aeiou"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    print(f"El número de vocales en la cadena es: {contador}")

def ejercicio_4_4():
    print("\n****** Ejercicio 4.4 *****************")
    numeros = [5, 12, 3, 18, 7, 24, 9]
    mayores_a_10 = list(filter(lambda x: x > 10, numeros))
    print("Números mayores a 10:", mayores_a_10)

def mostrar_menu():
    print("\nMenú de Ejercicios")
    print("1. Ejercicio 1.3 - Calificación del estudiante")
    print("2. Ejercicio 3.3 - Tablero de ajedrez")
    print("3. Ejercicio 2.3 - Contar vocales")
    print("4. Ejercicio 4.4 - Filtrar números mayores a 10")
    print("5. Salir")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == '1':
            ejercicio_1_3()
        elif opcion == '2':
            ejercicio_3_3()
        elif opcion == '3':
            ejercicio_2_3()
        elif opcion == '4':
            ejercicio_4_4()
        elif opcion == '5':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()