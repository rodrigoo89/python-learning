class Pajaro:
    alas= True # Atributo de clase
    def __init__(self, especie, color): 
        self.especie = especie
        self.color = color

    def cantar(self):
        print (f"{self.especie} está cantando.")

    def volar(self, metros):
        print(f"{self.especie} está volando {metros} metros.")
        self.cantar()
    
    def pintar_negro(self):
        self.color = "negro"
        print(f"el pajaro ahora es {self.color}")
    
    @classmethod #es un metodo de clase 
    def poner_huevos(cls, cantidad):
        print(f"Ponemos {cantidad} huevos.")
        
        
    @staticmethod
    def mirar():
        print("El pájaro está mirando.")
        
Pajaro.poner_huevos(3)




#EJEMPLOS DE EJERCICIOS

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

class Personaje:
        def __init__(self,cantidad_flechas):
            self.cantidad_flechas= cantidad_flechas
        def lanzar_flecha(self):
            self.cantidad_flechas -= 1
# Creamos una instancia de Personaje con 5 flechas
arquero = Personaje(5)

print(arquero.cantidad_flechas)  # 5

arquero.lanzar_flecha()  # dispara una flecha, resta 1
print(arquero.cantidad_flechas)  # 4
