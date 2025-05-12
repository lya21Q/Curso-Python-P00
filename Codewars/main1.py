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

from jugador_clase import Jugador
from equipo import Equipo
from torneos import Torneo

def menu():
    jugadores = []
    equipos = []
    torneo = Torneo()

    opcion = None
    while opcion != "11":
        print("\nMenú Principal")
        print("1. Crear nuevo jugador.")
        print("2. Crear nuevo equipo.")
        print("3. Ver lista de jugadores.")
        print("4. Ver lista de equipos.")
        print("5. Agregar jugadores a un equipo.")
        print("6. Eliminar jugadores de un equipo.")
        print("7. Agregar equipos al torneo.")
        print("8. Eliminar equipos del torneo.")
        print("9. Anotar gol(es) a un jugador.")
        print("10. Mostrar goles totales por equipo.")
        print("11. Generar rol de juegos.")
        print("12. Salir.")
        opcion = input("Seleccione una opción: ")


jugadores = []
list_equipo = []


def menu():
    opcion = None
    while opcion != "0":
        print("\nMenú Principal")
        print("[1]. Crear nuevo jugador")
        print("[2]. Crear nuevo equipo")
        print("[3]. Ver lista de jugadores")
        print("[4]. Ver lista de equipos")
        print("[0]. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo...")
        elif opcion == "1":
            while True:
                nombre = input("Ingresa el nombre del jugador: ")
                znumero = input("Ingresa el número del jugador: ")
            goles = input("Ingresa la cantidad de goles: ")

            if nombre and numero and goles.isdigit():
                jugadores.append(Jugador(nombre, numero, int(goles)))
                print(f"Jugador {nombre} creado exitosamente.")
            else:
                print("Datos inválidos, por favor intenta nuevamente.")
        elif opcion == "2":
            equipo_nombre = input("Ingresa el nombre del equipo: ")
            if equipo_nombre:
                list_equipo.append(Equipo(equipo_nombre, jugadores))
                print(f"Equipo {equipo_nombre} creado exitosamente.")
            else:
                print("Datos inválidos, por favor intenta nuevamente.")
        elif opcion == "3":
            if jugadores:
                print("Lista de jugadores:")
                for jugador in jugadores:
                    print(jugador)
            else:
                print("No hay jugadores registrados.")
        elif opcion == "4":
            if list_equipo:
                print("Lista de equipos:")
                for equipo in list_equipo:
                    print(equipo)
            else:
                print("No hay equipos registrados.")


if __name__ == "__main__":
    menu()
