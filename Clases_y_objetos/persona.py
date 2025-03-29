class Persona:
    def __init__(self,nombre:str,edad:int,altura:float,peso:float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
    def caminar(self) -> None:
        print("Estoy caminando")
    def comer(self) -> None:
        print("Estoy camiendo")
    def jugar(self) -> None:
        print("Estoy jugando")
    def dormir(self) -> None:
        print("Estoy durmiendo")


if __name__=='__main__':
    amiga=Persona("Jennifer Marlene Gutierrez Beteta",19,1.52,46)
print(amiga.nombre)
print(amiga.edad)
print(amiga.altura)
print(amiga.peso)

def caminar(self)->None:
    print(f"{self.nombre}está caminando para bajar de sus {self.peso}kgs")

def comer(self)->None:
    print(f"{self.nombre}está comiendo una maruchan de pollo picante.")

def jugar(self) -> None:
    print(f"{self.nombre}está jugando .")

def dormir(self)->None:
    print(f"{self.nombre}está durmiendo.")

amiga.peso=50
amiga.nombre="Rebeca"
amiga.edad=19
amiga.altura=1.65
amiga.caminar()
print(amiga.nombre)
