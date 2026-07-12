class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"Muuu.")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} hace beee.")
        for n in range(3):
            print(f"hace beee {n+1} .")
            
            
vaca1 = Vaca("Lola")

oveja1 = Oveja("Dolly")
   
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()  # Llamada al método hablar de cada objeto, demostrando polimorfismo
    
def animal_habla(animal):
    animal.hablar()
animal_habla(vaca1)  # Llamada al método hablar de la vaca
animal_habla(oveja1)  # Llamada al método hablar de la ove