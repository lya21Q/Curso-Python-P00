from equipo import Equipo
class Torneo:
    def __init__(self,nombre:str,*equipos:tuple[Equipo]):
        self._nombre=nombre
        self._equipos=list(equipos)

    def agregar_equipos(self,*equipos: tuple[Equipo])->None:
        for equipo in equipos:
            if equipo not in self._equipos:
                self._equipos.append(equipo)
            else:
                print(f"El equipo {equipo.nombre} ya está en el torneo.")

    def remover_equipos(self,*equipos: tuple[Equipo])->None:
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)
            else:
                print(f"El nombre {equipo} no forma parte de {self._equipos}")

    def mostrar_equipos(self,*equipos: tuple[Equipo]):
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self):
        if len(self._equipos) <2:
            print("No hay suficientes equipos.")
            return " "
        jornadas = []
        for equipo1 in enumerate(self._equipos):
            for equipo2 in enumerate(self._equipos):
                if equipo1 < equipo2:
                    jornadas.append((equipo1, equipo2))
        return jornadas

    def __str__(self):
        return f"Jugador(torneo:{self._nombre},equipos:{self._equipos})"
