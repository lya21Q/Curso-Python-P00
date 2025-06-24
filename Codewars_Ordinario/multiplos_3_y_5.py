"""
Rosalinda Aquino Perez
Si enumeramos todos los números naturales menores de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
Termina la solución para que devuelva la suma de todos los múltiplos de 3 o 5 por debajo del número pasado.
Además, si el número es negativo, devuelve 0.
"""
def solution(number):
    suma=0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:# Se verifica que el nú,mero al dividirlo entre 3 y 5 se obtenga un residuo de 0
            suma += i#Se acumula en la variable suma y se le suman los anteriores.
    print(f"La suma de los multipos de {number}, es {suma}")
    return suma#se le suma el numero actual a la variable suma

if __name__=="__main__":
    number = 10
    solution(number)