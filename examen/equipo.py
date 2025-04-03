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
        no_goles=int(input("Ingresar la cantidad de goles:"))
        return self._goles

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
        for jugador in list(jugadores):
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
        for jugador in self._jugadores:
            sum(jugador._goles)
        return sum
    def __str__(self):
        def __str__(self):
            return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"