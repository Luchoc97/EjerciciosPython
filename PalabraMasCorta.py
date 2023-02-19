frase = input("Ingresa una cadena: ")
words = frase.split()
#se estable 0 como indice para posteriormente tener un valor para poder comparar las demas palabras
shortest = words[0]
for palabra in words:
    #compara la longitud de las palabras con la funcion "len" en cada iteracion, 
    #si se cumple la condicion se reasigna el valor de la variable "shortest"
    if len(palabra) < len(shortest):
        shortest = palabra
print("La palabra más corta: " + str(shortest))
print("La longitud de la palabra es "  + str(len(shortest)))