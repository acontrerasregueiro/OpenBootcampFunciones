def test():
    print("")
    numero = input("Introduce un numero para ver si es primo ")
    #Un numero es primo si es mayor que uno y solo es divisible por si mismo
    if (int(numero) > 1):
        for i in range(2,int(numero)):
            if(int(numero % i) == 0):
                return(numero, " no es primo")
                break
            else:                
                return("numero " ,numero, "es primo")
    else:
        print("El numero debe ser mayor que uno")

print(test())