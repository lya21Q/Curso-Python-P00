"""
Tome un array y elimine cada segundo elemento. Conserve siempre el primer elemento y comience a eliminar con el siguiente.

Ejemplo:
["Keep", "Remove", "Keep", "Remove", "Keep", ...]-->["Keep", "Keep", "Keep", ...]

¡Ninguna de las matrices estará vacía, por lo que no tienes que preocuparte por eso!
"""
def remove_every_other(my_list):
    nueva = []
    for indice, lista in enumerate(my_list):
        if indice % 2 == 0:
            nueva.append(lista)
    return nueva

if __name__ == "__main__":
    my_list = ["Keep", "Remove", "Keep", "Remove", "Keep"]
    print(remove_every_other(my_list))
