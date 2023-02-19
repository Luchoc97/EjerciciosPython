import string, random

frase = "programando en python"
#quitamos los espacios en blanco con replace
unirlet = frase.replace(" ","")
#generar un letra cualquiera
letraRandom= random.choice(string.ascii_letters)
#letra minuscula
minuscula = letraRandom.lower()
todasLetras = 0

for i in unirlet:
    #recorre letra por letra y si la letra es igual a la letra random generada aumenta el contador
    if i == minuscula:
        todasLetras += 1
               
if todasLetras > 1:
    print ("la letra '" + minuscula + "' aparece " + str(todasLetras) + " veces en la frase: '" + frase + "'")
    
elif todasLetras == 1:
    print ("la letra '" + minuscula + "' existe solamente una vez en la frase: '" + frase + "'")  
        
elif todasLetras == 0:
    print ("la letra '" + minuscula + "' no existe en la frase: '" + frase + "'")
