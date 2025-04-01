"""
Escriba una función que acepte un entero no negativo ny una cadena scomo parámetros, y devuelva una cadena srepetida exactamente nveces.
Ejemplos (entrada -> salida)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""
def repeat_str(repeat, string):
    if repeat > 0:
        return repeat * string
    elif repeat == 0:
        return ''
