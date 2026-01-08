"""
Verificar formatos de fechas por ddmmaaaa
"""


def verificarformato(fecha): #Pasamos fecha por parametro

    verificacion = False


    fecha = fecha.strip() #.strip() tambien quita espacios

    if len(fecha) == 10:
        if fecha[2] == '/' and fecha[5] == '/': #Verificamos que los caracteres en las posiciones 2 y 5 sean '/'}

            fecha_sep = fecha.split('/') #Split funciona para separar cadenas de texto en listas segun el caracter que le indiquemos, en este caso '/'

            if len(fecha_sep[0]) == 2 and len(fecha_sep[1]) == 2 and len(fecha_sep[2]) == 4: # Verificamos que la primera parte tenga 2 digitos, la segunda 2 digitos y la tercera 4

        # Otra opcion es if len(fecha_sep[0:2]) == 2 and len(fecha_sep[3:5]) == 2 and len(fecha_sep[6:10]) == 4

                if fecha_sep[0].isdecimal() and fecha_sep[1].isdecimal() and fecha_sep[2].isdecimal(): #Comprobamos que cada parte contiene un decimal
                    verificacion = True #Cambiamos el estado de verificacion a TRUE
    return verificacion



print(verificarformato("02/05/2023")) #Llamamos a la funcion con un print
print(verificarformato("13/03/2025"))
print(verificarformato("5/2/25"))

print(int("02/05/2023"[0:2]))
def es_bisiesto(anho): # Usamos otra funcion para comprobar el año bisiesto
    return (anho % 4 == 0 and anho % 100 != 0) or (anho % 400 == 0)
def verificardiames(fecha):

    verificacion = False

    fecha = fecha.strip()

    fecha_sep = fecha.split('/')

    dia = int(fecha_sep[0])
    mes = int(fecha_sep[1])
    anho = int(fecha_sep[2])

    if mes == 2:
        if es_bisiesto(anho):

            if 1 <= dia <= 29:
                print(f"Valido por año bisiesto")
                verificacion = True
            else:
                print(f"Cuando el año es bisiesto febrero llega a 29 dias")
        else:
            if 1 <= dia <= 28:
                print(f"Valido")
                verificacion = True
    elif 1 <= mes <= 12:
        if 1 <= dia <= 31:
            print(f"Valido")
            verificacion = True
        else:
            print(f"No hay meses con mas de 31 dias")
    else:
        print(f"Mes fuera de rango")
    return verificacion

print(verificardiames("12/01/2025"))
print(verificardiames("32/13/2025"))
print(verificardiames("30/02/2026"))
print(verificardiames("29/02/2028"))

