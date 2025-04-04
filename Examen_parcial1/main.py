from jugador_clase import Jugador
from equipo import Equipo
from torneos import Torneo

def menu():
    jugadores = []
    list_equipo=[]
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
            crear_jugador(jugadores)
        elif opcion == 2:
            crear_equipo(list_equipo)
        elif opcion==3:
            mostrar_lista_jugadores(jugadores)
        elif opcion==4:
            mostrar_lista_equipos(list_equipo)
        elif opcion==5:
          agregar_jugadores(jugadores,list_equipo)
        elif opcion==6:
            eliminar_jugadores(jugadores)
        elif opcion==7:
            agregar_equipos_torneo(list_equipo)
        elif opcion==8:
           eliminar_equipos_del_torneo()
        elif opcion==9:
            anotar_goles_a_un_jugador()
        elif opcion==10:
            total_de_goles(jugadores)
        elif opcion==11:
            generarl_rol(list_equipo)


def crear_jugador(jugadores):
    nombre = input("Ingresa el nombre del jugador: ")
    numero = int(input("Ingresa el número del jugador: "))
    goles = int(input("Ingresa la cantidad de goles: "))
    if nombre.strip() and numero > 0 and goles >= 0:
        jugadores.append(Jugador(nombre, numero, goles))
        print(f"Jugador {nombre} creado exitosamente.")
    else:
        print("Datos inválidos, por favor verifica que el número y los goles sean positivos.")

def crear_equipo(list_equipo):
    while True:
        nombre_del_equipo= input("Ingresa el nombre del equipo o '1' para terminar: ")
        if nombre_del_equipo == "1":
            break
        equipo = Equipo(nombre_del_equipo,)
        list_equipo.append(equipo)

def mostrar_lista_jugadores(jugadores):
    if jugadores:
        print("Lista de jugadores:")
        for jugador in jugadores:
            print(jugador)
    else:
        print("No hay jugadores registrados.")

def mostrar_lista_equipos(lista_equipos):
    for equipo in lista_equipos:
        if lista_equipos=="":
            print("No hay equipos para mostrar.")
        else:
            print(equipo)

def agregar_jugadores(list_equipo,jugadores):
    nombre_jugador = input("Escribe el nombre del jugador: ")
    nombre_equipo = input("Escribe el nombre del equipo: ")
    equipo_seleccionado=" "
    for equipo in list_equipo:
        if equipo.nombre == nombre_equipo:
            equipo_seleccionado= equipo
            break
    if equipo_seleccionado!= list_equipo:
        print(f"No se encontro equipo.intenta de nuevo")
        return
    jugador_seleccionado=" "
    for jugador in jugadores:
        if jugador.nombre==nombre_jugador:
            jugador_seleccionado=jugador
            break
    if jugador_seleccionado!=jugadores:
        print("Nose encontro el jugador.")
    equipo_seleccionado.agregar_jugador(jugador_seleccionado)

def agregar_equipos_torneo(list_equipo,*jugadores):
        print("ingresa el nombre del equipo:")
        for equipo in list_equipo:
            if equipo != list_equipo:
                print("No hay equipos disponibles.")
            else:
                crear_equipo(list_equipo,*jugadores)
def eliminar_jugadores(jugadores):
    nombre=input("Ingresa el nombre del integrante que deceas eliminar:")
    for jugador in jugadores:
        if jugador in jugadores:
            jugadores.remove(jugador)
        else:
            print(f"El {jugador} no forma parte de {nombre}.")
def agregar_equipos_al_torneo():
    pass
def eliminar_equipos_del_torneo():
    pass
def anotar_goles_a_un_jugador():
    pass

def total_de_goles(jugadores):
    for i in jugadores:
        if i!= jugadores:
            return 0
        return sum(jugador.goles for jugador in jugadores)

def generarl_rol(list_equipo):
    if len(list_equipo) < 2:
        print("No hay suficientes equipos.")
        return " "
    jornadas = []
    for equipo1 in enumerate(list_equipo):
        for equipo2 in enumerate(list_equipo):
            if equipo1 < equipo2:
                jornadas.append((equipo1, equipo2))
    return jornadas
if __name__ == "__main__":
   menu()
