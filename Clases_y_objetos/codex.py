rating=float(input("ingresa un numero:"))
if rating > 4.5:
    print("Extraordinary")
elif rating > 4 :
    print("Excelent")
elif rating > 3 :
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")