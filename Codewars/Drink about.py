def people_with_age_drink(edad):
    edad=0
    if edad <= 14:
        print("drink toddy")
    elif edad > 14 and edad <= 18:
        print("drink coke")
    elif edad > 18 and edad <= 21:
        print("drink beer")
    elif edad > 21:
        print("drink whisky")

edad= int(input())