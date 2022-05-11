from random import randint

def generar_sexo(cantidad):
    personasfun=[]
    for n in range(0,cantidad):
        genero=randint(0,1)
        if (genero ==1):
            personasfun.append("H")
        else:
            personasfun.append("M")
    return personasfun

personas = generar_sexo(100)
"""
personas=[]
for n in range(1,101):
    genero=randint(0,1)
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
"""

#print(personas)

nº_hombres = len([genero for genero in personas if genero == "M"])
p_mujeres = 100 - nº_hombres
print(f"Hay {nº_hombres}% hombres y {p_mujeres}% mujeres")
"""
print(f"El porcentaje de mujeres es del: {lista.count(0)}%")
print(f"El porcentaje de hombres es del: {lista.count(1)}%")
"""
if nº_hombres > 50:
    print("Hay mas hombres")
elif nº_hombres < 50:
    print("Hay mas mujeres")
else:
    print("Empate")
