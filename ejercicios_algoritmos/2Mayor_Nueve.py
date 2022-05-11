print("escribir el numero")
Numero=input()
if(Numero.isdigit()):
    Numero=int(Numero)
    if(Numero==9):
        print("Tu numero es igual a 9")
    elif(Numero>9):
        print("Tu numero es mayor a 9")
    else:
        print("Tu numero es menor a 9")