"""
Nombre: Rosalinda Aquino Pérez
Fecha: 01/04/2025
Instrucciones:
A Nathan le encanta el ciclismo.
Como Nathan sabe que es importante mantenerse hidratado, bebe 0,5 litros de agua por cada hora de ciclismo.
Te dan el tiempo en horas y debes devolver el número de litros que beberá Nathan, redondeado hacia abajo .

Por ejemplo:
time = 3 ----> litres = 1
time = 6.7---> litres = 3
time = 11.8--> litres = 5
"""
def litres(time:float)->int:
#Parametros: time(float):Un número que representa la cantidad de horas en ciclismo.
#Retorna: litres(int):Los litros de agua que bebe en el tiempo trascurrido.
    litros=0.5
    total_consumido=time*litros
    total_consumido=int(total_consumido)
    print(f"El total de litros que consumio fueron: {total_consumido}")
    return total_consumido

if __name__ == "__main__":
    time = float(input("ingresa el tiempo transcurrido"))
    print(litres(time))