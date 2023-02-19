numero = int(input())
acCinco = 0
acTres = 0
tres = 0
cinco = 0
listaTres = []
listaCinco = []

print ("el numero es: " + str(numero) + "\n")

#rango va hasta el numero digitado
for i in range(1,numero):
    tres = (i*3)
    #agrega el resultado multiplicado a la lista vacia
    listaTres.append(tres)
    cinco = (i*5)
    listaCinco.append(cinco)  

for k in listaTres:
    #recorro y sumo a la variable acTres los resultados de la multiplicacion de 3
    #hasta dicho resultado de la multiplicacion sea menor al numero digitado
    if k < numero:
        print (k)
        Mult3Men = k
        acTres += k 

print ("el ultimo resultado de la multiplicacion de 3 menor a: " + str(numero) + " es: " + str(Mult3Men)) 

print ("---------") 

for j in listaCinco:
    if j < numero:
        print (j)
        Mult5Men = j
        acCinco += j

print ("el ultimo resultado de la multiplicacion de 5 menor a: " + str(numero) + " es: " + str(Mult5Men)) 
print ("---------") 

print ("la suma de los resultados la multiplicacion de 3 son que son menores a " + str(numero) + " es: " + str(acTres))
print ("la suma de los resultados la multiplicacion de 5 son que son menores a " + str(numero) + " es: " + str(acCinco))
#print (acTres + acCinco)