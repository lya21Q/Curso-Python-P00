"""
Descripción del programa:

El curso tiene los siguientes equipos:
    Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
    Los Hackers de Café: Tania, Patricia, Rebeca.
    Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
    Los Ctrl+Z: Galilea, Jennifer, Juan.
"""
"""
Este programa debe generar 6 nuevos equipos de 2 personas cada uno, 
pero con la restricción de que no puede haber dos personas que ya estuvieron en el mismo equipo de arriba ☝️. 
"""


import random

# Lista de los integrantes
integrantes = ["Rebeca", "Galilea", "Addi", "Hector", "Juan",
               "Jenny", "Rosalinda", "Ryan", "Duran", "Alberto", "Tania", "Patricia"]

# Listas para los nuevos equipos
equipo_1 = []
equipo_2 = []
equipo_3 = []
equipo_4 = []
equipo_5 = []
equipo_6 = []

# Todos los equipos
todos_los_equipos = [equipo_1, equipo_2, equipo_3, equipo_4, equipo_5, equipo_6]

while len(integrantes) >= 2:
    # Elegir dos personas aleatorias
    persona1 = random.choice(integrantes)
    integrantes.remove(persona1)
    persona2 = random.choice(integrantes)
    integrantes.remove(persona2)


    for equipos in todos_los_equipos:
        if len(equipos)<2:
            equipos.append(persona1)
            equipos.append(persona2)
            break

# Mostrar los equipos generados
print(f"Equipo 1: {equipo_1}.")
print(f"Equipo 2: {equipo_2}.")
print(f"Equipo 3: {equipo_3}.")
print(f"Equipo 4: {equipo_4}.")
print(f"Equipo 5: {equipo_5}.")
print(f"Equipo 6: {equipo_6}.")
