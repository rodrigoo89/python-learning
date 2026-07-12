class Pajaro:
    alas= True
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def cantar(self):
        return f"{self.especie} está cantando."

    def volar(self, metros):
        return f"{self.especie} está volando {metros} metros."

pajaro1 = Pajaro("Loro", "Verde")
pajaro2 = Pajaro("Canario", "Amarillo")

print(pajaro1.cantar())
print(pajaro2.volar())