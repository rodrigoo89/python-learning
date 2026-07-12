palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objeto = [palabra, lista, tupla]

def contar_elementos(objeto):
    for elemento in objeto:
        print(len(elemento))
contar_elementos(objeto)
        
        



class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
personajes=[Arquero(), Mago(), Samurai()]
for personaje in personajes:
    personaje.atacar()  # Llamada al método atacar de cada objeto, demostrando polimorfismo 
    
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
            personaje.defender()
        # Llamada al método defender de cada objeto, demostrando polimorfismo
    

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personaje_defender(mago1)     # Escudo mágico
personaje_defender(arquero1)  # Esconderse
personaje_defender(samurai1)  # Bloqueo