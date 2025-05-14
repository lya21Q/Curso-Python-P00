"""
Crea una función que tome un número entero como argumento y
retorne "Even"para números pares o
"Odd"para números impares.
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__=="__main__":
    number=1
    print(even_or_odd(number))