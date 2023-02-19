from collections import Counter
numeros = [7, 5, 7, 1, 5, 7, 9, 3, 4, 3, 5, 7, 8]
contador = Counter(numeros)
#contador.most_common(1) le indicamos que nos devuelva el numero mas repetido
#de la lista
numero_mas_repetido = contador.most_common(1)
#contador.most_common(2) le indicamos que nos devuelva los dos numeros mas repetidos
#de la lista
dos_numeros_mas_repetidos = contador.most_common(2)
#nos imprime el numero mas repetido y el numero de veces que se repite
print(numero_mas_repetido)
print(dos_numeros_mas_repetidos)
#imprimo solamente el numero sin las veces que se repite
print(numero_mas_repetido[0][0])
#imprimo solamente el numero sin las veces que se repite, [0] es el indice del numero,
#el segundo [0] si lo dejamos en cero no muestra las veces que repite, si lo dejamos en 1 muestra
#las repeticiones
print(dos_numeros_mas_repetidos[0][0], dos_numeros_mas_repetidos[1][1])
#imprime el numero mas repetido de los dos 
print(dos_numeros_mas_repetidos[0][0])


print("el numero mas repetido es: " + str(numero_mas_repetido[0][0]))
print("esta en la lista " + str(numero_mas_repetido[0][1]) + " veces")

print("el segundo numero mas repetido es: " + str(dos_numeros_mas_repetidos[1][0]))
print("esta en la lista " + str(dos_numeros_mas_repetidos[1][1]) + " veces")