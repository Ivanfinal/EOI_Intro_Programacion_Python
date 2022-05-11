#print("escribir el numero")
Numero=input("escribir el numero")
if(Numero.isdigit()):
    Numero=int(Numero)
    if((Numero%2)==0):
        print("Es par")
    else:
        print("Es impar")
