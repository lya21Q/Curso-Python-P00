n=int(input("Ingrese un número positivo:"))
def odd_count(n):
    impar=[]
    for i in range(n):
        if i%2!=0:
            impar.append(i)
    return impar
print(odd_count(n))