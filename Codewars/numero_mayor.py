
st='hi!'
def replace_exclamation(st):
    a='!'
    esp=""
    for letra in st:
        if letra == 'a' or letra == 'e' or letra =="i" or letra == "o" or letra =="u":
            esp+=a
        elif letra == 'A' or letra == 'E' or letra =="I"or letra == "O" or letra =="U":
            esp+=a
        else:
            esp+= letra
    return esp