contador = 0

#bucle infinito si no se digita un numero
while True:
    try:
        numero = int(input("Introduce un número par: "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

#si se digita un numero par al primer intento no se entra al bucle y se imprime el mensaje        
if numero % 2 == 0:
        print ("El numero " + str(numero) + " es par")

#mientras el numero digitado sea impar o cero el programa sera infinito hasta digitar un numero par
while numero % 2 == 1:
    #si no el par vuelve a pedir la entrada
    print ("debes digitar un numero par \n")
    #se aumenta el contador por cada intento fallido al digitar un nro impar o cero
    contador += 1
    
    #bucle infinito si no se digita un numero
    while True:
        try:           
            numero = int(input("digita un numero par: "))
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")
        
    if numero % 2 == 0:
        print ("El numero " + str(numero) + " es par")
        
    else:
        print ("El numero " + str(numero) + " es impar \n")
    
    intentos = contador-1
    
    if contador == 2 and numero % 2 == 1:
        print ("Te quedan " + str(intentos) + " intento")
    
    if contador == 3 and numero % 2 == 1:
        print ("Ningun numero digitado era par")
        break