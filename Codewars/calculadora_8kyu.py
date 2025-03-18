"""
Usted está obligado a crear una calculadora simple que devuelva el resultado de la adición, resta, multiplicación o división de dos números.

Su función aceptará tres argumentos:
El primer y segundo argumento deberían ser los números.
El tercer argumento debería representar un signo que indique la operación para realizar en estos dos números.

si las variables no son números o el signo no pertenece a la lista anterior, se debe devolver un mensaje de "valor desconocido".
"""
"""
Ejemplo:

calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"

"""
primer_argumento=int(input("Ingrese el primer argumento: "))
segundo_argumento=int(input("Ingrese eñ segundo argumento: "))
tercer_argumento=input("Ingrese el simbolo de la operación que se realizara: ")
simbolo=["+","-","*","/"]

def carculator(primer_argumento,segundo_argumento):
    while tercer_argumento != simbolo:
        if tercer_argumento == "+":
            calcular= primer_argumento + segundo_argumento
        elif tercer_argumento == "*":
            calcular= primer_argumento * segundo_argumento
        elif tercer_argumento == "/":
            calcular=primer_argumento / segundo_argumento
        else:
            print("Valor desconocido.")
            break
        return calcular

calcular=carculator(primer_argumento,segundo_argumento)
print(f"El resultado es {calcular}")