class Scoreboard:
    marcador=1
    def __init__(self,points:int=0,text_color:tuple[int]=(0,0,0),font:str="kimono"):
        self._points=points
        self._text_color=tuple[int]
        self._font=font
    marcador += 1

    @property
    def points(self)->int:
        return self._points

    @property
    def text_color(self)->tuple[int]:
        return self.text_color

    @property
    def font(self)->str:
        return self.font
    @property
    def size(self)->float:
        return self.size

    def draw(self)->None:
        pass

    def _str_int(self):
        pass

    def __str__(self) -> str:
        return f"(Scoreboard {self.points}, color {self.text_color, }, la fuente del texto{self.font})"


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
    marcador2 = Scoreboard(10, font="Arial", text_color=(127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()