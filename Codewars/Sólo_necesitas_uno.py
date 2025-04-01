"""
Recibirá una matriz ay un valor x. Solo necesita comprobar si la matriz proporcionada contiene el valor.
a Puede contener números o cadenas. xPuede ser cualquiera de los dos.
Devuelve truesi la matriz contiene el valor, falsesi no.
"""
def check(seq, elem):
    for i in range(len(seq)):
        if seq == elem:
            return True
    return False