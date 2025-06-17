def add_binary(a,b):
    suma=a+b
    resultado=bin(suma)
    res=resultado.replace("0b","")
    return res