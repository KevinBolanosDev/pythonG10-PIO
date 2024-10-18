# 1.1. Pida una “letra” por teclado y diga si es de las primeras letras del 
# alfabeto o si es de las ultimas

print("\n ******Ejercicio 1.1*****************")
pedir_letra = input("Ingrese una letra: ").lower()

if pedir_letra.isalpha() and len(pedir_letra) == 1:
    if pedir_letra <= 'm':
        print("La letra se encuentra entre las primeras letras del alfabeto.")
    else:
        print("La letra se enuentra entre las últimas letras del alfabeto.")
else:
    print("Por favor, ingrese una sola letra válida.")


# 1.2. Pida el valor de un ángulo en grados y diga en que cuadrante se encuentra.

print("\n ******Ejercicio 1.2*****************")

angulo = float(input("Ingresa el valor del ángulo en grados: "))

if 0 <= angulo < 90:
    print("El ángulo está en el primer cuadrante.")
elif 90 <= angulo < 180:
    print("El ángulo está en el segundo cuadrante.")
elif 180 <= angulo < 270:
    print("El ángulo está en el tercer cuadrante.")
elif 270 <= angulo < 360:
    print("El ángulo está en el cuarto cuadrante.")
else:
    print("El ángulo no está en un cuadrante válido (0-359 grados).")


# 1.3. Clasifique el rendimiento de un estudiante según sus calificaciones con los
# siguientes parámetros: mayor a 4.5 “Excelente”, entre 3.5 y 4.5 “bueno”, entre
# 3 y 3.5 “regular” e “Insuficiente” entre 0 y 3.

print("\n ******Ejercicio 1.3*****************")

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

# 1.4. Solicita y clasifica la temperatura como frio, templado y cálido.

print("\n ******Ejercicio 1.4*****************")

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 10:
    print("La temperatura es fría.")
elif 10 <= temperatura <= 20:
    print("La temperatura es templada.")
else:
    print("La temperatura es cálida.")

# 1.5. Solicite por pantalla la palabra “Jengibre” y emita un mensaje que diga:
# Si la palabra fue bien digitada:
# a. "Si, ¡El Jengibre es la mejor planta de todos los tiempos!"
# b. Si la palabra ingresada es ‘jengibre’ el mensaje debe ser "No, ¡quiero
# un gran Jengibre!”;
# c. Si ingresa otra palabra el mensaje será “! Jengibre¡ No ", la palabra
# ingresada.

print("\n ******Ejercicio 1.5*****************")
palabra_jengibre = input("Ingrese la palabra 'Jengibre': ")

if palabra_jengibre == "Jengibre":
    print("Sí, ¡El Jengibre es la mejor planta de todos los tiempos!")
elif palabra_jengibre == "jengibre":
    print("No, ¡quiero un gran Jengibre!")
else:
    print("¡Jengibre! No", palabra_jengibre)