from ast import Num


Numero1=input("escribir el primer numero: ")
Numero2=input("escribir el segundo numero: ")
if(Numero1.isdigit() and Numero2.isdigit()):
    #resultado=int(Numero1)+int(Numero2)
    print("el resultado es ", int(Numero1)+int(Numero2))
else:
    print("los valores introducidos no son numeros")
