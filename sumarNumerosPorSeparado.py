import random

#genero un numero aleatorio de 3 cifras
numero = random.randint(100,999)

#convertimos el numero a cadena para poder recorrerlo en el bucle for
cad = str(numero)
contador = 0

for i in cad:
    print (i)
    #convertimos i en entero para poder realizar la suma de cada numero
    contador += int(i)

print ("la suma de separar el numero " + cad + " es " + str(contador))