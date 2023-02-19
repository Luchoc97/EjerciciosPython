grupo = "Luis Luisa Lucho juan"
nombre = "Leonardo"

#print (grupo)

#separo los nombres de la variable grupo en una lista con split
listaN = grupo.split()

#print (listaN)

#primer letra del nombre
nombrePrL = nombre[0]
resultado = ""

for i in listaN:
    #print (i[0])
    #recorro nombre por nombre y con i[0] acceso a la primer letra de cada nombre y lo comparo con la variable nombrePrL que tiene la primer letra del nombre, si se encuentra una coincidencia rompo el bucle, ya que si no rompo el bucle solo tomara la comparacion con la letra del ultimo nombre de la lista
    if i[0] == nombrePrL:
        resultado = "Compare notes"
        break
    else:
        resultado = "No such luck"

print (resultado)