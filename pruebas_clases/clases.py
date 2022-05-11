class Persona:
    Nombre=""
    Apellido=""

    def __init__(self,nombre,apellido):
        self.Nombre=nombre
        self.Apellido=apellido

    def __str__(self):
        return "{} {}".format(self.Nombre, self.Apellido)
    def caminar(a):
        print("Voy, caminando por la vida...")

a=1
profesor= Persona("Billy","Vanegas")
#profesor.Nombre="Billy"
#profesor.Apellido="Vanegas"

alumno= Persona("Tomas","Turbao")
#alumno.Nombre="Tomas"
#alumno.Apellido="Turbao"

diputado= Persona("Perro","Sanchez")
#diputado.Nombre="Perro"
#diputado.Apellido="Sanchez"

print("El profesor: {} {}". format(profesor.Nombre,profesor.Apellido))
print("El alumno: {} {}". format(alumno.Nombre,alumno.Apellido))
print("El diputado: {} {}". format(diputado.Nombre,diputado.Apellido))
print("El profesor:", profesor)
profesor.caminar()
personas=[str(profesor),str(alumno),str(diputado)]
print(*personas)
print(" , ".join(personas))