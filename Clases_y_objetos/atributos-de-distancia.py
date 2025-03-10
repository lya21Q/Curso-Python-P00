class   Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre
        self.temas_aprendidos=[]
    def aprender_tema(self,tema:str)->None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendio {tema}")
    def __str__(self)->str:
        return f"Estudiante(nombre:{self.nombre},temas aprendidos : {self.temas_aprendidos})"



class   Profesor:
    def __init__(self,nombre):
        self.nombre=nombre
        self.temas_dominados=[]
    def dominar_temas(self,tema:str)->None:
        self.temas_dominados.append(tema)
    def ensenar_tema(self, no_tema:int)->str:
        if no_tema >len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"
    def __str__(self)->str:
        return f"Profesor(nombre:{self.nombre},temas dominados : {self.temas_dominados})"
if __name__=='__main__':
    estudiante1=Estudiante("Rosalinda Aquino Pérez")
    estudiante2=Estudiante("Jennifer Gutierrez")
    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("Internet de las cosas")
    print(estudiante1)
    print(estudiante2)

    profe=Profesor("Alberto Martínez Barbosa")
    profe.dominar_temas("Atributos de distancia")
    print(profe)





