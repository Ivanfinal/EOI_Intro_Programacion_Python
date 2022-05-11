def Fivonacci(N):
    if(N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return Fivonacci (N-1) + Fivonacci (N-2)

n=input("Introduce la posicion de Fibonacci: ")
try:
    n=int(n)
    serie=[]
    for i in range (1,n+1):
        r=Fivonacci(i)
        serie.append(r)
    print(f"el numero es {r}")
    print('la serie es', *serie)
    #print("la serie es {} {} {} {} {}".format(*serie))                muestra los 5 primeros solamente
except TypeError:
    print("Numero no valido")
except ValueError:
    print("Valor no validot")
except:
    print("faio")