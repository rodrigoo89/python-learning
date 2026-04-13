mi_lista= ["manzana", "banana", "cereza"]
for i, fruta in enumerate(mi_lista):
    print(f"Índice: {i}, Fruta: {fruta}")
    
mi_lista= ["manzana", "banana", "cereza"]
for fruta in enumerate(mi_lista):
    print(f"{fruta}")
    

for fruta in enumerate(range(54, 57)):
    print(f"{fruta}")
    
    
mi_lista= ["a", "b", "c", "d", "e"]

mis_elementos = list(enumerate(mi_lista))
print(mis_elementos[0][1])  # Imprime 'a'
print(mis_elementos[1][1])  # Imprime 'b'   
print(mis_elementos[2][0])  # Imprime 2




lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):

    print(f'{nombre} se encuentra en el índice {indice}')


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre [0] == "M":
         print(indice)
