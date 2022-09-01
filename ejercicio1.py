import math
def area_triangulo(base,altura):
    return (base * altura)/2
    
def area_circulo(radio):
    
    resultado = math.pi * (radio *radio)
    return(resultado)
 
print("area del triangulo de base 2 y altura 3 = ", area_triangulo(2,3))
print("area del circulo de radio 50 =",area_circulo(50))