def maps(a:list[int])->list[int]:
    list=[]
    for i in a:
        list.append(i*2)
    return list
if __name__=="__main__":
    a=[1,2,3]
    resultado=maps(a)
    print(f"La suma de los elementos del arreglo es: {resultado}")

