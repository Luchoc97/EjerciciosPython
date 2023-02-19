#importo el modulo calendario para usar la funcion month_name para obtener el nombre del mes dependiendo del numero
import calendar

ddmmaa = "31/10/1997"

#verifico si la fecha fue escrita con guiones o slash, dependiendo el caso, los elimino con split y genero una lista con dia mes y año
if "-" in ddmmaa:
    ddmmaa = ddmmaa.split("-")
elif "/" in ddmmaa:
    ddmmaa = ddmmaa.split("/")   
    
#almacena los valores en la variables dadas
dia , mes , año = ddmmaa

#funcion que toma como parametro la cadena ddmmaa
def fecha(ddmmaa):
    #aqui dentro de la funcion coloco en un try-except, ya que el fin de este ejercicio es tomar el numero del mes y pasarlo a su correspondiente version en texto, por lo cual si hay un numero menor que 1 o mayor a 12 generara una excepsion (calendar.month_name), por lo cual se hace el respectivo condicional tomando que mes este entre 1 y 12  
    try:
        if 1 <= int(mes) <= 12 and int(dia) <= 31:
            nombreMes = (calendar.month_name[int(mes)])
            print (dia + "/" + nombreMes + "/"+año)
        else:
        #si el numero del mes es mayor a 12 entonces se reemplaza la excepsion y colocamos un mensaje personalizado
            raise ValueError("fecha invalida")
    except ValueError as ve:
        print(ve)
    
fecha(ddmmaa)