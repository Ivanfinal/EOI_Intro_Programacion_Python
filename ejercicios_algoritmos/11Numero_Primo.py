import math

num=int(input("ingrese  numero: "))
divisor=2
comprobante=True

while(divisor<=math.ceil(num)/2):
    if(num%divisor==0):
        comprobante=False
        #break
    divisor+=1

if(comprobante):
    print("el numero es primo")
else:
    print("el numero NO es primo")
