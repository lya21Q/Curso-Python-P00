"""
Dada una cadena que contiene una lista de números enteros separados por comas,
escriba la función que toma dicha cadena y devuelve una nueva matriz/lista que contenga
todos los números enteros presentes en la cadena, preservando el orden.
- Tenga en cuenta que puede haber una o más comas consecutivas sin números,
como se muestra a continuación:
"-1,-2,,,,,,3,4,5,,6"
Por ejemplo

"-1,-2,3,-4,-5"--> [-1,-2,3,-4,-5]
"1,2,3,,,4,,5,,," --> [1,2,3,4,5]
",,,,,,,"--> []
"""
def string_to_int_list(s):
    numeros = []
    num = ''
    for i in s:
        if i == '-' and not num:#mientras no encuentre un negativo
            num += i
        elif i >='0' or i >= '9':#Verificar si el caracter es un numero
            num += i
        else:#si encontramos un caracter no numerico,almacenamos el numero construido.
            if num:
                numeros.append(int(num))#convertimos la cadena en int y lo añadimos a la lista.
                num = ''
    if num:
        numeros.append(int(num))
    return numeros

if __name__=="__main__":
    s="-1,-2,3,-4,-5"
    print(string_to_int_list(s))

