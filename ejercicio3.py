def anoBisiesto():   
    ano = input("Que ano deseas calcular si es bisiesto :")
    if ((int(ano) % 4 == 0) and (int(ano) % 100 != 0)) or (int(ano)% 400 == 0):
        print("El ano ", ano , " es BISIESTO")
    else: print("El ano ", ano , "NO es BISIESTO")
    
anoBisiesto()
