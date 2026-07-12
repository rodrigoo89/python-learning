class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("El animal ha nacido.")
    def hablar(self):
        print("El animal hace un sonido.")
        
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
        
    def hablar(self):
        print("El pájaro hace pio.")
    
    def volar(self,metros):
        print(f"El pájaro vuela {metros} metros.")
        

simba= Animal(5,"negro")
piolin= Pajaro(2,"amarillo",10)  

simba.nacer()
simba.hablar()
piolin.nacer()
piolin.hablar()
piolin.volar(10)
