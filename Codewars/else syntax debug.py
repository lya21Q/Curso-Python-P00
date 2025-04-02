"""
Depuración de sintaxis if/else
checkAliveMientras creaba un juego, tu compañero Greg decidió crear una función llamada // para comprobar si el usuario sigue vivo CheckAlive. check_aliveDesafortunadamente, Greg cometió algunos errores al crear la función.
checkAlive// debe devolver verdadero si la salud CheckAlivedel check_alivejugador es mayor que 0 o falso si es 0 o menor.
La función recibe un parámetro healthque siempre será un número entero entre -10 y 10.
"""

from random import randint

def check_alive(health):
    if health <= 0:
        return False
    else:
        return True

if __name__ == "__main__":
    salud = randint(-10,10)
    print(salud)
    print(check_alive(salud))