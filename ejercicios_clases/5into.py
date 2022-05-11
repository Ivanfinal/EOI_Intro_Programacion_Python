#Escriba su respuesta aquí.


class Nobel:
    category=""
    year=0
    winner=""
    def __init__(self, categoria, año , ganador):
        self.category = categoria
        self.year = año
        self.winner  = ganador

nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
print(nq2019.category, nq2019.year, nq2019.winner)