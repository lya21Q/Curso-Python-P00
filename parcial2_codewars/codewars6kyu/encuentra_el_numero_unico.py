def find_uniq(arr):
    if arr[0] == arr[1]:    # Comprobamos los primeros tres elementos de arr[i] para determinar cuál es el repetido
        base = arr[0]
    else:
        base = arr[2] if arr[0] == arr[2] else arr[0]
    for n in arr:    # Recorremos la lista para encontrar el número diferente
        if n != base:
            return n
