
from Ej2_Scoreboard import Scoreboard
class Window:
    #Métodos:
    #Inicializa la instancia de clase winddow don: texto, alto,ancho y marcador de la puntuación.
    def __init__(self,text:str,width:int,height:int,scoreboard:Scoreboard=Scoreboard())->None:
        #Atributos
        self._text=text#Título de la ventana(protegido).
        self._width=width#Ancho de la ventana (protegido).
        self._height=height#Alto de la ventana (protegido).
        self._scoreboard=scoreboard#Instancia de Scoreboard asociada a la ventana


    def draw_scoreboard(self)->None:#Llama al método draw para mostrarlo en pantalla.
        self._scoreboard.draw()

    def update_score(self,points:int)->None:#Actualiza la puntuación del marcador y lo dibuja nuévamente.
        self._scoreboard._points = points
        self._scoreboard.draw()

    def __str__(self)->str:
        return f"(Window(title= {self._text},width={self._width},heigth={self._height},{self._scoreboard})"
    #Representación en cadena que muestra, el título,dimdensiones y marcador.

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")