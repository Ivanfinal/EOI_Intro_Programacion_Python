num1=input("ingrese primer numero: ")
num2=input("ingrese segundo numero: ")
num3=input("ingrese tercer numero: ")
try:
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    if(num1<0):
        resul=num1*num2*num3
    else:
        resul=num1+num2+num3
    print(resul)
except:
    print("mete numeros caraho")