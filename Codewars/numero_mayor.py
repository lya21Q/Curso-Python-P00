"""
Nombre:Rosalinda Aquino Pérez
Fecha: 01/04/2025
Instrucciones:
Reemplace todas las vocales por signos de exclamación en la oración. aeiouAEIOUes vocal.
Ejemplos
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
"""
# Funcion que sustutuye las vocales en una oracion por el simbolo de exclamación
def replace_exclamation(st:str)->str:
    a='!'
    esp=""
    for letra in st:
        if letra == 'a' or letra == 'e' or letra =="i" or letra == "o" or letra =="u":# Comprueba si la letra es una vocal, ninuscula
            esp+=a
        elif letra == 'A' or letra == 'E' or letra =="I"or letra == "O" or letra =="U":# Comprueba si la letra es una vocal,mayuscula.

            esp+=a
        else:
            esp+= letra
    return esp
if __name__ == "__main__":
    st = 'hi!'
    print(replace_exclamation(st))