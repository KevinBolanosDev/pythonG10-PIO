#cadenas = 'palabra espanol'
#print(len(cadenas))
#print(f"Esta cadena {cadenas}")
#print(type(cadenas))
#caracter = 'a'
#print(len(caracter))
#print(type(caracter))
#minusculas = cadenas.lower()
#print(minusculas)
#print(cadenas.capitalize())
#print(cadenas.title())
""" print(cadenas.upper())
print(cadenas[1:3+1])
print(cadenas[:4])
print(cadenas[5:]) """
""" cadenas = 'palabra espanol'
print("en" not in cadenas)
print("bra" not in cadenas)
print("bra" in cadenas) """




#Entero o int - integer 
""" numeroEntero = 1
print(type(numeroEntero))
print(numeroEntero) """

#Numero decimales o flotantes -> float
""" numFloat = 3.14
print(type(numFloat))
print(numFloat) """

#numComplejo = 4j

#boolena valida si es verdader o falso
""" booleanoVerdader =  True
print(type(booleanoVerdader))
booleanoFalso = False
print(type(booleanoFalso)) """

#Comparacion ==, !=, >, <, >=, <=
""" num1 = 17
num2 = 20

igualdad = num1 == num2
desigual =  num1 != num2

print(igualdad)
print(desigual)
"""

#Logicos and , or, not

""" edad = 17
validarEdad = edad >= 18 and edad <= 35 
operdadorO =  "verde" or "rojo" """ 

""" 
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)    
print(not(z))
 """

""" import time


for i in range(1,6+1):
    print(i,"Mississippi")
    time.sleep(2)
print("¡Listo o no, ahí voy") """


palabraSinVocal = ""
userWord = input("Ingrese una palabra: ").upper()
vocal=("A","E","I","O","U")

for letra in userWord:
    if letra in vocal:
        continue
    else:
        print(letra+palabraSinVocal,end="\n")