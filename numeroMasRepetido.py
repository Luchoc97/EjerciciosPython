numeros = [7, 7, 1, 5, 7, 9, 3, 4, 3, 5, 7, 8]
#diccionario vacio el cual hara la funcion de contador
contador = {}

#recorre la lista y si el numero esta en la lista lo acumula en el contador
for i in numeros:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1

#la función max() para encontrar el elemento con el valor máximo, en este caso el que mas repite debido al condicional de arriba
#key=contador.get imprime la clave que tiene el valor mas alto en el diccionario
repetido = max(contador, key=contador.get)
print("el numero " + str(repetido) + " es el mas repetido")
#(contador[repetido]) accede al valor de la clave 
print ("esta en la lista " + str(contador[repetido]) + " veces")

print (contador)