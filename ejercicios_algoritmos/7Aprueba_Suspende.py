cal1=input("ingrese primera nota: ")
cal2=input("ingrese segunda nota: ")
cal3=input("ingrese tercera nota: ")
if(cal1.isdigit() and cal2.isdigit() and cal3.isdi()):
    promedio=(int(cal1)+int(cal2)+int(cal3))//3
    if(promedio>=4):
        print("aprueba")
    else:
        print("suspende")
    print(promedio)
else:
    print("escribe numeros validos")

#si queremos comprobar entre 0-10: cal1 in range (0,11)