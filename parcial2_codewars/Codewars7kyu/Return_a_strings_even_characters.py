"""
st=["b", "d", "f", "h", "j", "l"]

def even_chars(st):
    pares=[]
    for i in range(len(st)):
        if i % 2 == 0:
            pares.append(st[i])
    return pares
print(even_chars(st))"""

def even_chars(st):
    pares=[]
    i=1
    for i in range(1,len(st),2):#recore desde la segunda posiciób.
        pares.append(st[i])
        return pares
    if len(st)<2 or len(st) > 100:#verificar si la longitud de la cadena es válida.
        return "invalid string"

if __name__=="__main__":
    st = ["abcdefghijklm"]
    print(even_chars(st))