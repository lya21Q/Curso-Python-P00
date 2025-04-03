from equipo import Equipo

class Torneos:
    def __init__(self,nombre:str,*equipos:tuple[Equipo]):
        self._nombre=nombre
        self._equipos=list(equipos)
    def agregar_equipos(self,*equipos: tuple[Equipo])->None:
        for equipo in list(equipos):
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
        def __str__(self):
            return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"