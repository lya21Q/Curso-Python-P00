"""
Dada una matriz de números enteros, devuelve una nueva matriz con cada valor duplicado.
Por ejemplo:
[1, 2, 3] --> [2, 4, 6]
"""

def cadena_a_flotante(cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

if __name__=="__main__":
    num_cadena = input("Ingresa un número flotante: ")
    numero = cadena_a_flotante(num_cadena)
    print(f"El número convertido a float es: {numero}")
