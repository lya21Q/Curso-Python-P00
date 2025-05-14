data = "112233"


def count_me(data):
    contador = {}
    resultado = ""
    contados = ""

    # Contar ocurrencias
    for i in data:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1

    # Construir el resultado en orden de aparición
    for i in data:
        if i not in contados:
            resultado += str(contador[i]) + i
            contados += i

    return resultado


print(count_me(data))


