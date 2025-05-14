param=input("Ingresa la profesion: ")
def get_drink_by_profession(param):
    param1 = param.lower()
    if param1 == "jabroni":
        return "Patron Tequila"
    elif param1 == "school counselor":
        return "Anything With Alcohol"
    elif param1 == "programmer":
        return 	"Hipster Craft Beer"
    elif param1 == "bike bang member":
        return "Moonshine"
    elif param1 == "politician":
        return "Your tax dollars"
    elif param1 == "rapper":
        return "Cristal"
    else:
        return "Beer"
if __name__=="__main__":
    print(get_drink_by_profession(param))