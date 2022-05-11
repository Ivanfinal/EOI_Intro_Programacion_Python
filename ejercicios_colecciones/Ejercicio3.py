from random import randint
#from ejercicios_colecciones.Ejercicio1 import generar_sexo

def generar_sexo(cantidad):
    personasfun=[]
    for n in range(0,cantidad):
        genero=randint(0,1)
        if (genero ==1):
            personasfun.append("H")
        else:
            personasfun.append("M")
    return personasfun

sexo = generar_sexo(120)
edad = [randint(0,99) for i in range(0,120)]

mayorhombres=0
mayormujeres=0
menorhombres=100
menormujeres=100
numerohombres=0
numeromujeres=0
edadeshombres=0
edadesmujeres=0

for x in range (0,120):
    if(sexo[x] == "H"):
        numerohombres+=1
        edadeshombres+=edad[x]
        if (sexo[x] == "H" and edad[x]>mayorhombres):
            mayorhombres=edad[x]
        if (sexo[x] == "H" and edad[x]<menorhombres):
            menorhombres=edad[x]
    else:
        numeromujeres+=1
        edadesmujeres+=edad[x]
        if (sexo[x] == "M" and edad[x]>mayormujeres):
            mayormujeres=edad[x]
        if (sexo[x] == "M" and edad[x]<menormujeres):
            menormujeres=edad[x]

print(f"El hombre mas mayor tiene {mayorhombres} años")
print(f"El hombre mas joven tiene {menorhombres} años")
print(f"La mujer mas mayor tiene {mayormujeres} años")
print(f"La mujer mas joven tiene {menormujeres} años")
print(f"La media de los hombres es {round(edadeshombres/numerohombres)} años")
print(f"La media de las mujeres es {round(edadesmujeres/numeromujeres)} años")