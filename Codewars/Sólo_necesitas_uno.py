"""
NombreÑ Rosalinda Aquino Pérez
Fecha: 04/04/2025
Instrucciones:
Recibirá una matriz a y un valor x. Solo necesita comprobar si la matriz proporcionada contiene el valor.
a Puede contener números o cadenas. x Puede ser cualquiera de los dos.
Devuelve true si la matriz contiene el valor, false si no.
"""
def check(seq:list[int], elem:int)->bool:
    #Parametros : seq: Matriz de numeros
    #elem: Numero ingresado
    for i in seq:#Recorre la lista
        if i == elem:#Si encuentra el elemento
            return True#devuelve true
    return False#caso contrario devuelve false
if __name__ == "__main__":
    seq=[1,4,5,6,2,5]
    elem=int(input("Ingresa un número:"))
    print(check(seq,elem))