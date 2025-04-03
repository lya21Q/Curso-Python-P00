class Jugador:
    #nombre,numero,goles:Métodos de acceso para obtener y modificar atributos.
    def __init__(self,nombre:str,numero,goles:int=0) -> None:
        """Constructor para inicializar los atributos."""
        self._nombre=nombre
        self._numero=numero
        self._goles=goles

    @property
    def nombre(self):
        return self._nombre
    @property
    def numero(self):
        return self._numero
    @property
    def goles(self):
        return self._goles

    def __str__(self):
       return f"Jugador(Nombre del jugador:{self._nombre}, numero de jugador:{self._numero},cantidad de goles anotados {self._goles})"