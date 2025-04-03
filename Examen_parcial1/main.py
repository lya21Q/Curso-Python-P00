from jugador_clase import Jugador
from equipo import Equipo

def menu():
    opcion=None
    while opcion != 0:
        print("Menú Principal")
        print("[1].- Crear nuevo jugador.")
        print("[2]. Crear nuevo equipo")
        print("[3]. Ver lista de jugadores")
        print("[4]. Ver lista de equipos")
        print("[5]. Agregar jugadores a un equipo")
        print("[6]. Eliminar jugadores de un equipo")
        print("[7]. Agregar equipos al torneo")
        print("[8]. Eliminar equipos del torneo")
        print("[9]. Anotar gol(es) a un jugador")
        print("[10]. Mostrar goles totales por equipo")
        print("11. Generar rol de juegos")
        print("0.Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion==0:
            print("Saliendo")
            break
        elif opcion == 1:
            jugadores=[]
            nombre = input("Ingresa el nombre del jugador: ")
            numero = int(input("Ingresa el número del jugador: "))
            goles = int(input("Ingresa la cantidad de goles: "))
            while bool(nombre) and bool(numero) and bool(goles):
                jugadores.append(Jugador(nombre, numero,goles))
                print(f"Jugador {nombre} creado exitosamente.")
                break
            else:
                print("Datos inválidos, por favor intenta nuevamente.")

        elif opcion == 2:
            list_equipo=[]
            nombre = input("Ingresa el nombre del equipo.")
            if nombre:
                list_equipo.append(Equipo(nombre,jugadores))
        elif opcion==3:
            if jugadores:
                print("Lista de jugadores:")
                for jugador in jugadores:
                    print(jugador)
            else:
                print("No hay jugadores registrados.")
        elif opcion==4:
            if list_equipo:
                print("Lista de equipos:")
                for equipo in list_equipo:
                    print(equipo)
            else:
                print("No hay equipos registrados.")
        elif opcion==5:
            pass
        elif opcion==6:
            pass
        elif opcion==7:
            pass
        elif opcion==8:
            pass
        elif opcion==9:
            pass
        elif opcion==10:
            pass
        elif opcion==11:
            pass


if __name__ == "__main__":
   menu()

