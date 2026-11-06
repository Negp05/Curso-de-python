


"""
def doble(numero):
    return numero * 2

resultado = doble(5)
print(resultado)       
print(doble(5) + 1)



############################
def doble_print(numero):
    print(numero * 2)

def doble_return(numero):
    return numero * 2

a = doble_print(5)
b = doble_return(5)
print(a)
print(b)
print ( b + 1)
print (a + 1)

"""



#Ejercicio 1: suma(a, b)
def suma(a,b):
    return(a+b)
resultado = suma(3, 4)
print(resultado)

#Ejercicio 2: resta(a, b) y multiplicacion(a, b)
def resta(c,d):
    return(c-d)
resultado = resta(9,2)
print(resultado)

def multiplicacion(e,f):
    return(e*f)
resultado = multiplicacion(4,5)
print(resultado)



#Ejercicio 3: es_mayor_de_edad(edad)

def es_mayor_de_edad(edad):
    return edad >=18 # <--- no sabia que esto se podia hacer
if es_mayor_de_edad(30):
    print("Puede pasar")
else:
    print("No puede pasar")


#Ejercicio 4: calificacion(nota)
def calificacion(nota):
    if nota >=60:
        return "Aprobada"
    else:
        return "Reprobada"
print(calificacion(45))
print(calificacion(60))
print(calificacion(90))


