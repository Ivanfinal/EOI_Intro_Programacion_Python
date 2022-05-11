#Escriba su respuesta aquí.
class Nobel:
    category=""
    year=0
    winner=""
    def __init__(self, categoria, año , ganador):
        self.category = categoria
        self.year = año
        self.winner  = ganador

    def __str__(self):
        return "{} {} {}".format(self.category, self.year, self.winner)


nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019)