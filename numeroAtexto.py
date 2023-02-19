textoNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


frase = "tengo 2 balones, 1 cancha de futbol y 10 jugadores"

#rango hasta 10 y con [::-1] empiezo por el ultimo elemento de la lista
#esto lo hago ya que cuando vaya a reemplazar el numero 10 por el textoNum
#correspondiente si empieza por el inicio y no por el final, en vez de
#cambiarlo por "ten", lo que pondra es "onezero"
for i in range(0,11)[::-1]:
    while str(i) in frase:
        #mientras i esté en la frase reemplazara el numero con su correspondiente
        #forma en texto
        frase = frase.replace(str(i), textoNum[i])

print (frase)  

#------------------------------------------
#segunda solucion

dic = {
    "10": "ten",
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

#recorre la clave y el valor del diccionario
for key, value in dic.items():
    #reemplaza los numeros que hay en la frase (key) y con su correspondiente
    #forma en texto (value)
    frase = frase.replace(key, value)

print(frase)  