import random

#generar numero aleatorio entre -20 hasta 20
numero = random.randint(-20,20)

if numero > 0:
    print ("el numero " + str(numero) + " es positivo")
elif numero == 0:
    print ("el numero " + str(numero) + " es neutro")
else: 
    print ("el numero " + str(numero) + " es negativo")