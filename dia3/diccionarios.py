cliente = {
    "nombre": "Juan",
    "apellido": "Fernández",
    "edad": 30,
    "peso": 75.5,
    "altura": 1.80,
    "ciudad": "Madrid"
}

resultado = cliente["nombre"] # Devuelve el valor asociado a la clave "nombre", que es "Juan"
print(resultado) # Imprime el valor obtenido, que es "Juan"

dic = {"c1": 1, 
       "c2": [1, 2, 3],
       "c3": {"s1": 1, "s2": 2}} #  Crea un diccionario con las claves "c1", "c2" y "c3" y los valores 1, 2 y 3 respectivamente
print(dic["c2"]) # Imprime el valor asociado a la clave "c2", que es la lista [1, 2, 3]
print(dic["c3"]["s2"]) # Imprime el valor asociado a la clave "
dic["color"] = "rojo" # Agrega una nueva clave "color" al diccionario con el valor "rojo"
print(dic.keys()) # Imprime las claves del diccionario, que son "c1", "c2", "c3" y "color"
print(dic.values()) # Imprime los valores del diccionario, que son 1, [ 