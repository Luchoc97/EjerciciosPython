frase = input("Ingresa una cadena: ")
#separa palabra por palabra en una lista con split
words = frase.split()
#se estable la primer palabra con words[0] para posteriormente tener un valor
#para poder comparar las demas palabras
masLarga = words[0]
contador = 0
mismasP = []
for palabra in words:
    #compara la longitud de las palabras con la funcion "len" en cada iteracion, 
    #si se cumple la condicion se reasigna el valor de la variable "masLarga"
    if len(palabra) > len(masLarga):
        masLarga = palabra

print("La palabra más larga es: " + str(masLarga))
print("La longitud de la palabra es "  + str(len(masLarga)))