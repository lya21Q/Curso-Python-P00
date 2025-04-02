"""
Nombre : Rosalinda Aquino Pérez
Fecha: 01/04/2025
Instrucciones:
Completa la función que devuelve el día de la semana según el número de entrada:
1 - Devoluciones"Sunday"
2 - Devoluciones"Monday"
3 - Devoluciones"Tuesday"
4 - Devoluciones"Wednesday"
5 - Devoluciones"Thursday"
6 - Devoluciones"Friday"
7 - Devoluciones"Saturday"
De lo contrario regresa: "Wrong, please enter a number between 1 and 7"
"""

"""Función que devuelve un dia correspondiendo a un número"""
def whatday(num:int) ->str:
#Parámetros:num (int), Un número entero del 1 al 7 que representa un día de la semana.
#Retorna :El nombre correspondiente al número ingresado.
# Si el número no se encuentrá en el rango imprime un mensaje de error.
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num== 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"

if __name__ == "__main__":
    num = int(input("Ingresa un número:"))
    print(whatday(num))
