def multiplication_table(size):
    lista=[]
    for i in range(size):
        i=i+1
        aux=[]
        for j in range(size):
            j=j+1
            aux.append(i*j)
        lista.append(aux)
    return lista