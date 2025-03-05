import random
from hashlib import algorithms_available

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

def genera_equipos(nuevos_equipos):
    nuevos_equipos=input("Ingrese los nombres de los nuevos equipos:")

integrantes=["Hector","Addi","Jesus Alberto","Tania","Patricia","Rebeca",
             "Jamileth","Bryan","Rosalinda","Galilea","Jenny","Juan"]
print("Seleccione a los nuevos integrantes:")
