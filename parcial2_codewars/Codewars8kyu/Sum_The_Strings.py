"""
Crea una función que tome 2 números enteros en forma de cadena como entrada y muestre la suma (también como cadena):
Ejemplo: ( Entrada1, Entrada2 -->Salida )
"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
"""
def sum_str(a, b):
    if a == "":
        a=0
    else:
        a=int(a)
    if b == "":
        b=0
    else:
        b=int(b)

    return a + b
if __name__=="__main__":
    a=input("Ingresa el valor de a:")
    b=input("Ingresa el valor de b:")
    print(sum_str(a,b))