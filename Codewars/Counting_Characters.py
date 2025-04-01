"""
Define un método llamado countCharOccurrenceso
count_char_occurrencesque acepta una cadena y un carácter como
entradas y devuelve la cantidad de veces que el carácter aparece en la cadena como un int.

"""
strng=input("Ingrese una palabra:")
char=input("Ingrese un caracter:")
def count_char_occurrences(strng, char):
    cont=0
    for letra in strng:
        if letra == char:
            cont+=1
    return cont
print(count_char_occurrences(strng,char))