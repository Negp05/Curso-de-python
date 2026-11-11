def suma(a,b):
    return(a+b)


def resta(a,b):
    return(a-b)


def multiplicacion(a,b):
    return(a*b)


def division(a,b):
    if b == 0:
        return("Divison no valida")
    else:
        return(a/b)




def mostrar_menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")




while True:
    mostrar_menu()
    opcion = input("Elige un opcion ")
    if opcion == "1":
        a=int (input("Ingrese el primer numero "))
        b=int (input("Ingrese el segundo numero "))
        resultado = suma(a,b)
        print ("La suma de ",a," + ",b,"es = ", resultado)
        
    elif opcion == "2":
        a=int (input("Ingrese el primer numero "))
        b=int (input("Ingrese el segundo numero "))
        resultado = resta(a,b)
        print ("La resta de ",a," - ",b,"es = ", resultado)

    elif opcion == "3":
        a=int (input("Ingrese el primer numero "))
        b=int (input("Ingrese el segundo numero "))
        resultado = multiplicacion(a,b)
        print ("La multiplicacion de ",a," X ",b,"es = ", resultado)

    elif opcion == "4":
        a=int (input("Ingrese el primer numero "))
        b=int (input("Ingrese el segundo numero "))
        resultado = division(a,b)
        print ("La division de ",a," ÷ ",b,"es = ", resultado)
    

    elif opcion == "5":
        print("Adios")
        break
    else:
        print("Opcion No Valida")
    
    


