class Scoreboard():
    puntuacion=1
    def __init__(self,points:int=0,text_color:tuple[int]=(0,0,0),font:str="kimono"):
        self.points=points
        self.text_color=tuple[int,int,int]
        self.font=font

    def constructor(self):
        pass
    def metodos_de_acceso(self):

    def draw(self):
        pass
    def _str_int(self):
        pass

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