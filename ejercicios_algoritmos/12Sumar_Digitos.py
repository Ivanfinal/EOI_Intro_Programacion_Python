from math import trunc


nro=int(input("ingrese  numero: "))
resul=0
while(nro!=0):
    resul+= nro % 10
    nro=nro//10
print("el resultado es ", resul)
