"""
Nombtre: Rosalinda Aquino Pérez
Fecha: 01/04/2025
Instrucciones:
Define un méodo llamado countCharOccurrenceso, count_char_occurrencesque acepta una cadena y un carácter como
entradas y devuelve la cantidad de veces que el carácter aparece en la cadena como un int.
"""

def count_char_occurrences(strng:str, char:str)->int:
#Parametros: strng(str):Cadena ingresada por el usuario.
#char(str): Caracter ingresado por el usuiario.
#Retorna : cont (int): El número que representa la cantidad de veces que el carácter aparece en la cadena.
    cont=0
    for letra in strng:
        if letra == char:
            cont+=1
    return cont

if __name__ == "__main__":
    strng = input("Ingrese una palabra:")
    char = input("Ingrese un caracter:")
    print(count_char_occurrences(strng,char))