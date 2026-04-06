mi_set = set([1, 2, 3, 4, 5]) # Crea un conjunto con los elementos 1, 2, 3, 4 y 5
print(type(mi_set)) # Imprime el tipo de la variable mi_set
print(mi_set)

mi_set.add(6) # Agrega el elemento 6 al conjunto mi_set
print(mi_set)

set = {4, 5, 6, 7, 8} # Crea un conjunto con los elementos 4, 5, 6, 7 y 8
nuevo_set = mi_set.union(set) # Crea un nuevo conjunto que es la unión de mi_set y set
print(nuevo_set)
nuevo_set.remove(1) # Elimina el elemento 1 del conjunto nuevo_set
print(nuevo_set)