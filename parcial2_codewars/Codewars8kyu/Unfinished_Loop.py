def cadena_a_flotante(cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None
num_cadena = input("Ingresa un número flotante: ")
numero = cadena_a_flotante(num_cadena)
print(f"El número convertido a float es: {numero}")
