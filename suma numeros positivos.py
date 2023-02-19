numero = int(input("digita un numero: "))
sumaNum = 0

#se debe digitar un numero negativo o 0 para salir del bucle
while numero > 0:
    #si se digita numeros postivos, se van sumando entre si
    sumaNum += numero
    numero = int(input("digita un numero: "))
    
print ("la suma es: " + str(sumaNum))