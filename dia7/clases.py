class Pajaro:
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print(f"{self.especie} está piando y es de color {self.color}.")
        
    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros.")

mi_pajaro = Pajaro("Loro", "Verde")
mi_pajaro2 = Pajaro("Canario", "Amarillo")

mi_pajaro.piar()
mi_pajaro2.piar()
mi_pajaro.volar(10)
mi_pajaro2.volar(5)



class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
reloj= Alarma()
reloj.postergar(5)