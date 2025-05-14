"""
Dada una cadena de números enteros, cuente cuántas veces se repite ese número entero y luego devuelva una cadena que muestre el recuento y el número entero.

Ejemplo:"1123"

Aquí 1 viene dos veces así <count><integer>será"21"
entonces 2 viene una vez así <count><integer>será"12"
entonces viene 3 una vez así <count><integer>será"13"
Por lo tanto, la cadena de salida será "211213".

De manera similar "211213"regresará "1221121113" (1 vez 2, 2 veces 1, 1 vez 2, 1 vez 1, 1 vez 3)

Retorna :""para cadenas vacías, nulas o no numéricas
"""
def count_me(data):
    contador = {} # Diccionario que almacenará la cantidad de apariciones de cada carácter
    resultado = ""
    contados = ""
    # Recorremos la cadena y contamos las ocurrencias de cada carácter
    for i in data:
        if i in contador:
            contador[i] += 1
        else:#si la letra aparece por primera vez inializamos el contador e n e1.
            contador[i] = 1
    for i in data:
        if i not in contados:#caracteres que no han sido agregados
            resultado += str(contador[i]) + i
            contados += i

    return resultado

if __name__=="__main__":
    data = "112233"
    print(count_me(data))


