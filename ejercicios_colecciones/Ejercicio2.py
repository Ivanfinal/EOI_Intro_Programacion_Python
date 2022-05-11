from random import randint

personas = [randint(0,99) for i in range(0,100)]

#print(personas)
mas_de_diezocho = len([persona for persona in personas if persona>=18])
#clasificación
personas.sort()
Clasificacion_Edades = {edad:0 for edad in personas}
for n in personas:
    Clasificacion_Edades[n]+=1
print(Clasificacion_Edades)
edad_mayor=max(personas)
edad_menor=min(personas)

print("Número de personas con 18 o mas años:",mas_de_diezocho)
print("La edad mas alta es:",edad_mayor)
print("la edad mas baja es:",edad_menor)

for edad in Clasificacion_Edades:
    print('{:3} -> {:1.2f}%'.format(edad,Clasificacion_Edades[edad]))