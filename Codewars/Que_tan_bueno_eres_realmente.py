"""
Hubo un examen en tu clase y lo aprobaste. ¡Felicidades!
Pero eres ambicioso. Quieres saber si eres mejor que el promedio de tu clase.
Recibirás una matriz con las puntuaciones de tus compañeros. ¡Ahora calcula el promedio y compara tu puntuación!
Vuelve truesi estás mejor, de lo contrario false...
Nota:
Tus puntos no se incluyen en la matriz de puntos de tu clase. ¡No los olvides al calcular la puntuación media!
"""
class_points = [70, 80, 90, 85]
your_points = 55
def better_than_average(class_points, your_points):
    total_puntos = 0
    num_estudiantes= 0
    for points in class_points:
        total_puntos += points
        num_estudiantes += 1
    prom = total_puntos / num_estudiantes
    if prom < your_points:
        return True
    else:
        return False
print(better_than_average(class_points,your_points))