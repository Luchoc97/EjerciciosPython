import re

camelcase = "HolaMundoPython"

print ("frase en camel case: " + camelcase)

#si la primer letra de la cadena es mayuscula la convierto en minuscula y con camelcase[1:] la concateno con el resto de las letras 
if camelcase[0].isupper():
    camelcase = camelcase[0].lower() + camelcase[1:]
    
#regex para buscar letras mayusculas
pattern = r"[A-Z]"

#genera una lista con las mayusculas encontradas en la cadena
match = re.findall(pattern, camelcase)

for i in match:
    #recorro cada letra de la lista y le agrego _ y las convierto en minusculas
    m = "_" + i.lower()
    #mientras haya una letra mayuscula en la cadena se reemplazara por la variable m
    while i in camelcase:
        camelcase = camelcase.replace(i, m)

print("frase en snake: " + camelcase)