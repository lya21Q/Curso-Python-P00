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


