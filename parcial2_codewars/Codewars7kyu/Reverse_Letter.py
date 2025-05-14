"""
Tarea
Dada una cadena str, inviértala y omita todos los caracteres no alfabéticos.
Ejemplo
Para str = "krishan", la salida debe ser "nahsirk".

Para str = "ultr53o?n", la salida debe ser "nortlu".
Entrada/Salida
[input]cadenastr
Una cadena consta de letras latinas minúsculas, dígitos y símbolos.
[output]una cuerda
"""
def reverse_letter(st):
    letras = ""

    for letra in st:
        if 'a' <= letra <= 'z' or 'A' <= letra <= 'Z':  # Filtrar letras
            letras+=letra
    return "".join(reversed(st))

if __name__=="__main__":
    st="krishan"
    print(reverse_letter(st))