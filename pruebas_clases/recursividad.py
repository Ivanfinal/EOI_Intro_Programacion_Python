def Factorial(N):
    if (N<=0):
        raise
    if(N<=1):
        return 1
    else:
        return N * Factorial(N-1)

n=input("Introduce numero a sacar factorial: ")
try:
    n=int(n)
    r=Factorial(n)
    print(f"el factorial es {r}")
except TypeError:
    print("Numero no valido")
except:
    print("faio")