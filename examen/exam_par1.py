class Jugador:
    def __init__(self,nombre:str,numero,goles:int=0) -> None:
        self._nombre=nombre
        self._numero=numero
        self._goles=goles
    def anotar_goles(self):
        pass
    def __str__(self):
        pass

class Equipo:
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        self._nombre=nombre
        self._jugadores=jugadores
    def agregar_jugadores(self):
        pass
    def mostrar_jugadores(self):
        pass
    def remover_jugadores(self):
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