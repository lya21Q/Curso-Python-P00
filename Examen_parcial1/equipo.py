from jugador_clase import Jugador
class Equipo:
    id=1
    def __init__(self,nombre:str,*jugadores:tuple[Jugador]):
        """Constructor de la clase equipo, que representa un equipo"""
        self._id_equipo=Equipo.id
        Equipo.id+=1
        self._nombre=nombre
        self._jugadores=list(jugadores)
    @property
    def id_equipo(self):
        return self._id_equipo
    @property
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
        if not self._jugadores:
            print(f"No hay jugadores en el equipo {self._nombre}.")
        else:
            print(f"Jugadores en el equipo {self._nombre}:")
            for jugador in self._jugadores:
                print(f"- {jugador}")

    def total_goles(self):
        if not self._jugadores:
            return 0
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        jugadores_str = "\n".join(f"- {jugador}" for jugador in self._jugadores)
        return f"Equipo(Id equipo:{self._id_equipo}, nombre:{self._nombre},jugadores{self.mostrar_jugadores()}cantidad de goles anotados {self.total_goles()})"
