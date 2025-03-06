class   Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre
        self.temas_aprendidos=[]
    def aprender_tema(self,tema:str)->None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre}aprendio{tema}")




class   Profesor:
    def __init__(self,nombre):
        self.nombre=nombre
        self.temas_dominados=[]

    def temas_dominados(self,tema:str,no_tema:int):
        self.temas_dominados.append(tema)
        print(f"")





