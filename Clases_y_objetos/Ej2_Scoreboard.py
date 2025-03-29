class Scoreboard:
    """
    Atributos:
    - points (int): Número de puntos iniciales en el marcador.
    - text_color (tuple[int, int, int]): .Formato del texto
    - font (str): Fuente utilizada para el marcador. Predeterminado es "kimono".
    - size (float): Tamaño del marcador.
    """
    """Métodos"""
    def __init__(self,points:int=0,text_color:tuple[int,int,int]=(0,0,0),font:str= "kimono",size:float=48) -> None:
        """Constructor de la clase, inicializa el marcador con los valores predeterminadas."""
        self._points=points
        self._text_color=text_color
        self._font=font
        self._size=size

    @property
    def points(self)->int:#Propiedad para obtener el valor actual de los puntos
        return self._points

    @property
    def text_color(self)->tuple[int,int,int]:#Propiedad para obtener el color actual del texto.
        return self._text_color

    @property
    def font(self)->str:#Propiedad para obtener la fuente actual del marcador.
        return self._font
    @property
    def size(self)->float:#Propiedad paara obtener el tamaño de actual del marcador.
        return self._size

    def draw(self)->None:
        print(f"score={self.points}")

    def __str__(self) -> str:
        return f"(Scoreboard (points={self._points}, text_color {self._text_color},font= {self._font}, size={self._size})"


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(points=10, font="Arial", text_color=(127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()