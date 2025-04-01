"""
Los niños beben ponche.
Los adolescentes beben Coca-Cola.
Los adultos jóvenes beben cerveza.
Los adultos beben whisky.
Crear una función que reciba la edad y devuelva lo que beben.

Normas:
Niños menores de 14 años.
Adolescentes menores de 18 años.
Joven menor de 21 años.
Los adultos tienen 21 o más.

Ejemplos: (Entrada --> Salida)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
"""
age= int(input("Ingrese tu edad: "))
def people_with_age_drink(age):
    if age <= 13:
        return 'drink toddy'
    if age > 13 and age <= 17:
        return 'drink coke'
    if age > 17 and age <= 20:
        return 'drink beer'
    if age > 20:
        return 'drink whisky'
print(f"{people_with_age_drink(age)}")


