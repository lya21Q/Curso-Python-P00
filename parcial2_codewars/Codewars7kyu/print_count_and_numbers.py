def count_me(data):
    contador = {}
    resultado = ""
    contados = ""
    for i in data:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    for i in data:
        if i not in contados:
            resultado += str(contador[i]) + i
            contados += i

    return resultado

data = "112233"
print(count_me(data))


