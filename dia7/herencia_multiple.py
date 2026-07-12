class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja ja ja")
    def hablar(self):
        print("Hola, soy la madre")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
print(Nieto.__mro__)  # Muestra el orden de resolución de métodos (Method Resolution Order)