import random
integrantes=["Rebeca","Galilea","Addi","Hector","Juan",
             "Jenny","Rosalinda","Ryan","Duran","Alberto","Tania","Patricia"]
equipo_1=[]
equipo_2=[]
equipo_3=[]
equipo_4=[]
equipo_5=[]
equipo_6=[]

while len(integrantes)>=2:
    persona1=random.choice(integrantes)
    integrantes.remove(persona1)
    persona2=random.choice(integrantes)
    integrantes.remove(persona2)



print(f"Equipo 1: {equipo_1}")
print(f"Equipo 2: {equipo_2}")
print(f"Equipo 3: {equipo_3}")
print(f"Equipo 4: {equipo_4}")
print(f"Equipo 5: {equipo_5}")
print(f"Equipo 6: {equipo_6}")



