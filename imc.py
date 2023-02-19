try:
    peso = int(input("digita tu peso: "))
    estatura = float(input("digita tu estura: "))
    formulaImc = peso/estatura**2
    imc = (round(formulaImc,1))
    
    print (round(formulaImc,1))
    
    if imc < 18.5:
        print("Bajo en peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso estable")
    elif 25.0 <= imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0:
        print("Obesidad")
      
except ValueError:
    print("debes digitar un numero valido")
      