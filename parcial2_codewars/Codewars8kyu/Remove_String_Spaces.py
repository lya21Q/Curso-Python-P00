"""
Escriba una función que elimine los espacios de la cadena y luego devuelva la cadena resultante.
Ejemplos ( Entrada -> Salida ):
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"""
x= input("Ingresa una palabra: ")
def no_space(x):
    result = ""
    for i in x:
        if i != " ":
            result = result + i
    return result
print(no_space(x))