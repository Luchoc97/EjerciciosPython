frase = "programando en python"
contTotal = 0
#quitamos los espacios en blanco con replace
unirlet = frase.replace(" ","")
resultado = ""

for i in unirlet:    
    #recorremos cada letra de la frase unida y con la funcion count contamos si se repiten letras en la frase sin espacios
    letra = unirlet.count(i)
    #si se repite una letra 2 o mas veces aumentamos el contador
    if letra > 1:
        contTotal += 1
        #agregamos las letras repetidas a la variable resultado
        resultado += i
               
print ("El numero total de letras repetidas son: " + str(contTotal)) 
print ("Las letras repetidas en la frase: '" + frase + "' son: " + resultado)
