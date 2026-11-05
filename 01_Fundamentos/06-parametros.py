"""def saludar(nombre):
    print("Hola,", nombre)

saludar("Sain")
saludar("Ana")
"""
#Ejercicio 1
#Escribe mostrar_mensaje(texto) que imprima el texto que reciba. Llámala con tres textos distintos.
def mostrar_mensaje(texto):
    print(texto)
mostrar_mensaje("Que")
mostrar_mensaje("Xopa")
mostrar_mensaje("Pmá")

#Ejercicio 2 
#Escribe doble(numero) que imprima el doble del número. Llámala con 5, 10 y 7.
def doble(numero):
    print(numero*2)
doble(5)
doble(10)
doble(7)

#Ejercicio 3: es_par(numero)
def es_par(numero):
    if numero %2 == 0:
        print("el numero",numero,"es par")
    else:
        print("el numero",numero,"impar")
es_par(4)
es_par(7)
es_par(10)


#Ejercicio 4: presentarse(nombre, edad)
def presentarse(nombre,edad):
    print("Me llamo",nombre,"y tengo",edad,"años")
presentarse("Juanito",20)


def revisar_edad(edad):
    if edad >=18:
        print(edad,"es mayor de edad")
    else:
        print(edad,"es menor de edad")
revisar_edad(15)
revisar_edad(18)
revisar_edad(30)
