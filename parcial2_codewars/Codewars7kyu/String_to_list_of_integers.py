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
        if i == '-' and not num:
            num += i
        elif i >='0' or i >= '9':
            num += i
        else:
            if num:
                numeros.append(int(num))
                num = ''
    if num:
        numeros.append(int(num))
    return numeros

s="-1,-2,3,-4,-5"
print(string_to_int_list(s))

