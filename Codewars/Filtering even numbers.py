"""
Nombre:Rosalinda Aquino Pérez
Fecha:01/04/2025
Instrucciones:
supone que el méodo elimina los números pares de la lista y devuelve una lista que contiene los números impares.
Sin embargo, hay un error en el méodo que necesita ser resuelto.
"""

def kata_13_december(lst:list[int]):
    i=0
    while i < len(lst): #recorre la lista
        if lst[i]%2==0: #si el numero dividido en dos es cero, es numero par.
            lst.pop(i)#entonces, elimina los elementos pares.
        else:
            i+=1
    return lst#retorna la nueva lista que solo tiene los numeros impares
if __name__ == "__main__":
    lst=[2,4,8,5,4,7,6,2,3,1]
    print(kata_13_december(lst))