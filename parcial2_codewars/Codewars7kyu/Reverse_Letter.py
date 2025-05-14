def reverse_letter(st):
    letras = ""

    for letra in st:
        if 'a' <= letra <= 'z' or 'A' <= letra <= 'Z':  # Filtrar letras
            letras+=letra
    return "".join(reversed(st))

st="krishan"
print(reverse_letter(st))