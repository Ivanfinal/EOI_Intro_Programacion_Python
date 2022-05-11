contador=0
for numero in range (1,10,2):
    contador+=1
    if contador < 2:
        continue
    elif contador > 3:
        break
    print (numero)

