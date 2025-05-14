def remove_every_other(my_list):
    nueva = []
    for indice, lista in enumerate(my_list):
        if indice % 2 == 0:
            nueva.append(lista)
    return nueva

if __name__ == "__main__":
    my_list = ["Keep", "Remove", "Keep", "Remove", "Keep"]
    print(remove_every_other(my_list))
