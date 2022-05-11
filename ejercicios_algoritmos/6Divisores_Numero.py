from this import d


numero=input("ingrese el numero: ")
if(numero.isdigit()):
    numero=float(numero)
    div=1
    while(div<=numero):
        if(numero%div == 0):
            print(div)
        div +=1
else:
    print("introduce valores validos")