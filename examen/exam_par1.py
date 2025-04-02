class Jugador:
    #nombre,numero,goles:Métodos de acceso para obtener y modificar atributos.
    def __init__(self,nombre:str,numero,goles:int=0) -> None:
        """Constructor para inicializar los atributos."""
        self._nombre=nombre
        self._numero=numero
        self._goles=goles

    def anotar_goles(self,no_goles: int):
        no_goles=self._goles
        return self._goles

    def __str__(self):
       return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"

class Equipo:
    contador_id:int=0
    no_id = 1
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        self._nombre=list(nombre)
        self._jugadores=tuple[jugadores]

    def agregar_jugadores(self,*jugadores: tuple[Jugador]):
        for jugador in jugadores:
            if jugador != self._jugadores:
                jugadores=jugadores.append(jugador)
            else:
                print("El jugador ya existe")
        return self._jugadores

    def remover_jugadores(self,*jugadores: tuple[Jugador]):
        pass
    def mostrar_jugadores(self):
        pass
    def total_goles(self):
        pass
    def __str__(self):
        pass
class Torneos:
    def __init__(self,nombre:str,*equipos:tuple[Equipo]):
        self._nombre=nombre
        self._equipos=equipos
    def agregar_equipos(self,*equipos: tuple[Equipo]):
        pass
    def remover_equipos(self,*equipos: tuple[Equipo]):
        pass
    def mostrar_equipos(self,*equipos: tuple[Equipo]):
        pass
    def generar_rol(self):
        pass
    def __str__(self):
        pass

if __name__=="__main__":
    print("Bienvenido al torneo: Champions ")
    op=None
    while op!=0:
        print("[1].Crea un-")
        print("[1].-")
        print("[1].-")
        print("[1].-")
        print("[1].-")
        print("[1].-")
        print("[1].-")

