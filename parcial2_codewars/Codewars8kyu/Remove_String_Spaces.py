x= input("Ingresa una palabra: ")
def no_space(x):
    result = ""
    for i in x:
        if i != " ":
            result = result + i
    return result
print(no_space(x))