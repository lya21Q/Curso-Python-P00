"""
Nombre:Rosalinda Aquino Pérez
Fecha: 01/04/2025
Hubo un Examen_parcial1 en tu clase y lo aprobaste. ¡Felicidades!
Pero eres ambicioso. Quieres saber si eres mejor que el promedio de tu clase.
Recibirás una matriz con las puntuaciones de tus compañeros. ¡Ahora calcula el promedio y compara tu puntuación!
Vuelve truesi estás mejor, de lo contrario false...
Nota:
Tus puntos no se incluyen en la matriz de puntos de tu clase. ¡No los olvides al calcular la puntuación media!
"""
def better_than_average(class_points:list[int], your_points:int)->bool:
    total_puntos = 0
    num_estudiantes= 0
    for points in class_points:#Recorre la matriz de puntos
        total_puntos += points#Suma de los puntos
        num_estudiantes += 1#conteo de los estudiantes
    prom = total_puntos / num_estudiantes#calcula el promedio
    if prom < your_points:
        return True#Devuelve true si su caificacion es mayor a los puntos.
    else:
        return False#De lo contrario devuelve False
if __name__ == "__main__":
    class_points = [70, 80, 90, 85]
    your_points = 55
    print(better_than_average(class_points,your_points))