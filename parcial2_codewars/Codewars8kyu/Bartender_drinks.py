"""
Completa la función que recibe como entrada una cadena y produce salidas de acuerdo a la siguiente tabla:

Aporte	-> Producción
"Jabroni" ->"Tequila Patrón"
"Consejero escolar" -> "Cualquier cosa con alcohol"
"Programador" -> Cerveza artesanal hipster
"Miembro de una pandilla de motociclistas"	-> "Luz de la luna"
"Político" ->	"Sus dólares de impuestos"
"Rapero" ->	"Cristal"
algo más -> "Cerveza"
Nota: cualquier otra cosa es el caso predeterminado: si la entrada a la función no es ninguno de los valores de la tabla, entonces el valor de retorno debe ser "Beer".

Asegúrese de cubrir los casos en los que ciertas palabras no se escriben correctamente en mayúsculas. Por ejemplo, la entrada "pOLitiCIaN"debería devolver "<sub>" (<sub>" "Your tax dollars");
"""

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