import random

#genero un numero random del 1 hasta el 10
numero = random.randint(1,10)

print ("tabla de multiplicar del numero " +str(numero))

#rango hasta 10
for i in range(1,11):
    #multiplico el numero, por cada numero recorrido del rango
    print (str(numero) + " x " + str(i) + " = " + str(numero*i))