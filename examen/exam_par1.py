class Jugador:
    #nombre,numero,goles:Métodos de acceso para obtener y modificar atributos.
    def __init__(self,nombre:str,numero,goles:int=0) -> None:
        """Constructor para inicializar los atributos."""
        self._nombre=nombre
        self._numero=numero
        self._goles=goles
    def nombre(self):
        return self._nombre

    def anotar_goles(self,no_goles: int):
        self._goles += no_goles
        return no_goles

    def __str__(self):
       return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"

_id = 0
class Equipo:
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        """Constructor de la clase equipo, que representa un equipo"""
        self._id_equipo=Equipo._id
        self._nombre=nombre
        self._jugadores=list(jugadores)


    def nombre(self):
        return self._nombre

    def agregar_jugadores(self,*jugadores: tuple[Jugador])->None:
        """Se utiliza para agregar jugadores"""
        for jugador in jugadores:
            self._jugadores.append(jugador)

    def remover_jugadores(self,*jugadores: tuple[Jugador])->None:
        """Se utilizapara remover un jugador del equipo """
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)
            else:
                print(f"El {jugador} no forma parte de {self._nombre}.")

    def mostrar_jugadores(self):
        for jugador in self._jugadores:
            print(jugador)

    def total_goles(self):
        return sum(jugador._goles for jugador in self._jugadores)

    def __str__(self):
        def __str__(self):
            return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"

class Torneos:
    def __init__(self,nombre:str,*equipos:tuple[Equipo]):
        self._nombre=nombre
        self._equipos=list(equipos)
    def agregar_equipos(self,*equipos: tuple[Equipo])->None:
        for equipo in equipos:
            self._equipos.append(equipo)

    def remover_equipos(self,*equipos: tuple[Equipo])->None:
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
            else:
                print(f"El empleado {equipo} no forma parte de {self._equipos}")

    def mostrar_equipos(self,*equipos: tuple[Equipo]):
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self):
        pass
    def __str__(self):
        return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"

if __name__=="__main__":
    print("Bienvenido al torneo: Champions ")
    op=None
    while op!=0:
        print("[1].Crea un nuevo jugador.")
        print("[2].-Crear nuevo equipo.")
        print("[3].-Ver lista de jugadores.")
        print("[4].-Ver lista de equipos.")
        print("[5].-Agregar jugadores a algún equipo.")
        print("[6].-Eliminar jugadores de un equipo.")
        print("[7].-Anotar goles a un jugador.")
        print("[8].-Anotar goles a un jugador.")
        print("[9].-Anotar goles a un jugador.")
        print("[10].-Anotar goles a un jugador.")
        print("[11].-Anotar goles a un jugador.")
        print("[0].-Salir.")
        op=int(input("Ingresa una opción"))

