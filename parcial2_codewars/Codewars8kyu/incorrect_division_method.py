"""
Este método, que debería devolver el resultado de dividir su primer argumento entre el
 segundo, no siempre devuelve valores correctos. Corríjanlo.
def divide_numbers(x,y):
    return x // y
"""
def divide_numbers(x,y):
    return x / y
if __name__=="__main__":
    x=4
    y=2
    print(divide_numbers(x,y))