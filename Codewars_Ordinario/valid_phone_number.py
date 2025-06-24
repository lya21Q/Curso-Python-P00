"""
Rosalinda Aquino Perez
Escriba una función que acepte una cadena y devuelva verdadero si está en formato de número de teléfono.
Suponga que cualquier entero del 0 al 9 en cualquiera de los espacios generará un número de teléfono válido.
Solo preocúpese por el siguiente formato:
(123) 456-7890 (no olvide el espacio después del paréntesis de cierre)
"""
"""
Función is.digit()
Verifica si una cadena de texto esta compuesta de por números.
"""
def valid_phone_number(phone_number):
    if len(phone_number) != 14:# si la cadena no tiene un rango de 14 caracteres
        return False #retorna falso
    if phone_number[0] != '(' or phone_number[4] != ')' or phone_number[5] != ' ' or phone_number[9] != '-':#se verifica que esten los caracteres del formato en las posiciones correspondientes
        return False
    if not (phone_number[1].isdigit() and phone_number[2].isdigit() and phone_number[3].isdigit()):#Se verifica que los caracteres de las posiciones 1,2,3 sean números
        return False
    if not (phone_number[6].isdigit() and phone_number[7].isdigit() and phone_number[8].isdigit()):#Se verifica que los caracteres de las posiciones 6,7,8 sean números
        return False
    if not (phone_number[10].isdigit() and phone_number[11].isdigit() and phone_number[12].isdigit() and phone_number[13].isdigit()):#Se verifica que los caracteres de las posiciones 10,11,12,13 sean números
        return False
    return True #Si cumple con lo anterior retorna verdadero

if __name__=="__main__":
    phone_number="(123) 456-7890"
    print(valid_phone_number(phone_number))