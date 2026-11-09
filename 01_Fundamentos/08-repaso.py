
"""
Escribe un programa que:

-Le pide al usuario su nombre
-Solicita al usuario su año de nacimiento.
-Calcula y muestra su edad.

"""

def calcular_edad(anio):
    return 2026-int(anio)
name=input("Porfavor ingrese su nombre ")

anio=input("Porfavor ingrese su año de nacimiento ")


edad=calcular_edad(anio)

print("Hola ",name,"tienes ",edad,"años")



# es_mayor_de_edad(edad)

def es_mayor_de_edad(edad):
    return edad >=18 # <--- no sabia que esto se podia hacer
if es_mayor_de_edad(edad):
    print("Puede pasar")
else:
    print("No puede pasar")