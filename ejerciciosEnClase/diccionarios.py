my_dictionary = {
    'Manzana': 1200,
    'Pera': 1500,
    'Mango': 1300,
    'Sandia': 2000
}

obtenerV = my_dictionary.get('Pera')
print(obtenerV)

eliminarV = my_dictionary.pop('Sandia')
print(eliminarV)

my_dictionary.update({'Guayaba': 2000, 'Banano': 500})



print(my_dictionary)