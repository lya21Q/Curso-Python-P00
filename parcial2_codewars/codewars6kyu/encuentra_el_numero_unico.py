"""
Hay una matriz con algunos números.
Todos son iguales excepto uno. ¡Intenta encontrarlo!
"""
def find_uniq(arr):
    if arr[0] == arr[1]:
        base = arr[0]
    elif arr[0] == arr[2]:
        base = arr[0]
    else:
        base = arr[2]

    for n in arr:
        if n != base:
            return n
if __name__=="__main__":
    arr=[ 1, 1, 1, 2, 1, 1 ]
    print(find_uniq(arr))