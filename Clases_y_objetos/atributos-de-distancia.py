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
    def __init__(self,nombre,temas_dominados:list[str]):
        self.nombre=nombre
        self.temas_dominados=temas_dominados.copy()
        self.temas_dominados=temas_dominados
    def dominar_temas(self,tema:str)->None:
        self.temas_dominados.append(tema)
    def ensenar_tema(self, no_tema:int)->str:
        if no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "Fuera de rango"
    def __str__(self)->str:
        return f"Profesor(nombre:{self.nombre},temas dominados : {self.temas_dominados})"

class Empleado:
   # __no_id__: int  # Es como un contador
    no_id=1
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
        self.id_Empleado=Empleado.no_id
        Empleado.no_id += 1
    def aumentar_sueldo(self,porcentaje:float)->None:
        
        pass
    def __str__(self)-> str:
        Empleado(id={self.id},nombre={self.nombre})

if __name__=='__main__':
    estudiante1=Estudiante("Rosalinda Aquino Pérez")
    estudiante2=Estudiante("Jennifer Gutierrez")
    estudiante1.aprender_tema("Evolución sitios web")
    estudiante2.aprender_tema("Internet de las cosas")
    print(estudiante1)
    print(estudiante2)

    profe=Profesor("Alberto Martínez Barbosa", ["Atributos de distancia, instructor de musica, recursividad"])
    #tema1=Profesor.ensenar_tema(1)
    #tema2=Profesor.ensenar_tema(2)
    #estudiante1.aprender_tema(tema1)
    #estudiante2.aprender_tema(tema1)
    #estudiante2.aprender_tema(Profesor.ensenar_tema(tema2))
    #profe.dominar_temas("Atributos de distancia")
    #profe.dominar_temas("Instructor de basquetbol")
    print(profe)

    empleado1=Empleado("Jose Ramirez", 250)
    empleado2=Empleado("Maria Ramirez", 250)
    print(Empleado.no_id)





