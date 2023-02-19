numero = 75
numDiv = "3 4 5"

#recorre cada numero que hay en la cadena y lo convierte a numero, con split
#genera una lista con cada uno de los numeros agrupados en ella eliminado
#los espacios
numDiv = [int(k) for k in numDiv.split(" ")]


for i in numDiv:   
    if int(i) == 0:
        resultado = "not divisible by all"
        break
    #guardo el resultado del resto de la division entre el numero y cada uno de los numeros de numDiv
    div = numero%int(i)
    #si el resto es cero quiere decir que es divisible y si hay un resultado que es diferente a cero rompe el bucle
    #ya que todos los numeros deben ser divisibles
    if div != 0:
        resultado = "not divisible by all"
        break
    else:
        resultado = "divisible by all"
    
print (resultado)