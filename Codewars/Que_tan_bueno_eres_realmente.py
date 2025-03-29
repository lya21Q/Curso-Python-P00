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