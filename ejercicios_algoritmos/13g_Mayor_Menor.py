nro1=int(input("ingrese  numero 1: "))
nro2=int(input("ingrese  numero 2: "))
nro3=int(input("ingrese  numero 3: "))
if(nro1>= nro2 and nro1>=nro3):
    print(f"El numero mayor es: {nro1}")
elif(nro2>=nro1 and nro2>=nro3):
    print(f"El numero mayor es: {nro2}")
else:
    print(f"El numero mayor es: {nro3}")