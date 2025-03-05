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
    alberto=Persona("Alberto Martínez",31,50,1.65)
print(alberto.nombre)
print(alberto.edad)
print(alberto.caminar)
print(alberto.jugar)