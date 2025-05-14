"""
Tu colega escribió un bucle sencillo para enumerar sus animales favoritos. Pero parece que hay un pequeño error gramatical que impide que el programa funcione. ¡Corrígelo! :)
Si pasa la lista de sus animales favoritos a la función, debería obtener la lista de los animales con ordenamientos y nuevas líneas agregados.
Por ejemplo, pasar:
[ "dog", "cat", "elephant" ]
dará como resultado:
"1. dog\n2. cat\n3. elephant\n"
"""
animals=["dog", "cat", "elephant"]
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + str(animals[i]) + '\n'
    return lst
print(list_animals(animals))