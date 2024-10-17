""" with open('dataArchivos.txt', 'w', encoding="utf-8") as archivo:
    archivo.write("Hola clase, escribiendo una linea de código\n")
    archivo.write("Colocando una segunda linea de código\n")
    archivo.write("Una linea más\n") """

""" with open('dataArchivos.txt', 'r') as archivo:
    contenido = archivo.readlines()
    print(contenido)
   
    for l in contenido:
        print(l.replace('\n', '')) """

with open('dataArchivos.txt', 'a') as archivos:
    archivos.write('\nAgregando linea al final del archivo')