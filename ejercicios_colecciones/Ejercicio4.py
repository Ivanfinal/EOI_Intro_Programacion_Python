from random import randint
import statistics

"""
def generar_temperatura(cantidad):
    ciudades=[]
    for n in range(0,cantidad):
        temperaturas = [randint(0,12) for i in range(-20,50)]
        ciudades[n]= temperaturas
    return ciudades

temperaturas_ciudades = generar_temperatura(20)
"""
#recordar odiar que esto no venga por SQL

temperatura_alta=-20
ciudad_alta=0
temperatura_baja=50
ciudad_baja=0

for x in range (0,20):
    temperaturas = [randint(-20,50) for i in range(0,12)]
    promedio=round(statistics.mean(temperaturas))
    if(promedio>temperatura_alta):
        temperatura_alta = promedio
        ciudad_alta=x
    elif(promedio<temperatura_baja):
        temperatura_baja=promedio
        ciudad_baja=x

print(f"la ciudad {ciudad_alta} tiene el promedio mas alto con {temperatura_alta}")
print(f"la ciudad {ciudad_baja} tiene el promedio mas bajo con {temperatura_baja}")
