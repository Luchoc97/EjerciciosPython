import random

numero = random.randint(1,10)
#print (numero)
mult = 0

print ("tabla de multiplicar del numero " +str(numero))

#mientras "mult" sea menor que 10 lo aumentara 1 vez hasta llegar a 10
while mult < 10:
    mult += 1
    #multiplico el numero, por cada numero recorrido por la variable "mult"
    print (str(numero) + " x " + str(mult) + " = " + str(numero*mult))   