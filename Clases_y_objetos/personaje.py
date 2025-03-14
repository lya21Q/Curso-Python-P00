class Personaje:
    #Clase que representa a un personaje.
    #SUS ATRIBUTOS SON, X y Y.
    contador_id:int=1
    no_id = 1
    def __init__(self):
        #Atributos de instancia
        self.X=0
        self.Y=0

        #Atributo independiente
        self.id_personaje=Personaje.no_id
        Personaje.no_id+=1

    def moverse(self, ordenes:str)->None:
        for palabra in ordenes:
            if palabra == "A" or palabra== "a":
                self.Y+=1
            elif palabra == "R" or palabra== "r":
                self.Y-=1
            elif palabra == "D" or palabra== "d":
                self.X+=1
            elif palabra == "I" or palabra== "i":
                self.X-=1
            else:
                print("no valido, intentelo de nuevo")
                break

    def posicion_actual(self)->None:
        print(f"Posición actual de X:{self.X} y la posición actual de Y es: {self.Y} ")


    def __str__(self):
        return f"Personaje(id: {self.id_personaje}, (X,Y):({self.X},{self.Y}))"

    """ %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ =="__main__":
    #Personaje=()
    personaje1=Personaje()
    cont=0
    while cont < 10:
        ordenes=input("Ingresa las ordenes de movimiento: ")
        if ordenes=="S" or ordenes == "s":
            print("Fin del programa.")
            break
        personaje1.moverse(ordenes)
        personaje1.posicion_actual()
        cont+=1
