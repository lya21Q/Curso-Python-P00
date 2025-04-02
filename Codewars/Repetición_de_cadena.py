"""
Nombre: Rosalinda Aquino Pérez
Fecha: 01/04/2025
Instrucciones:
Escriba una función que acepte un entero no negativo ny una cadena scomo parámetros, y devuelva una cadena s repetida exactamente n veces.
Ejemplos (entrada -> salida)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""

def repeat_str(repeat:int, string:str)->str:
    #Parámetros:repeat(int):Representa el numero de veces que se repetira la palabra.
    #string(str):Cadena que se repetira.
    #Retorna: La cadena repetida n veces.
    # Si el número es 0, retorna una cadena vacía.
    if repeat > 0:# Mientras el numero sea mayor que cero
        return repeat * string#Multiplica la cadena con el número ingresado.
    elif repeat == 0:#Si es cero
        return ''#Retorna un cadena vacia
if __name__ == "__main__":
    repeat = int(input("ingrese un numero:"))
    string = input("ingrese una palabra:")
    print(repeat_str(repeat,string))