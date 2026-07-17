from collections import defaultdict

# defaultdict crea un diccionario que, cuando buscás una clave que no existe,
# en vez de tirar error, devuelve automáticamente lo que le indiques en el lambda
mi_diccionario = defaultdict(lambda: 'Valor no hallado')

# Cargamos el par clave-valor que pide la consigna:
# la CLAVE es 'edad' (no "palabra clave", eso era solo la explicación del enunciado)
# el VALOR es 44 (no "valor", ese texto tampoco va literal)
mi_diccionario.update({'edad': 44})

# Ahora, si buscamos una clave que SÍ existe, nos da el valor real:
print(mi_diccionario['edad'])        # >> 44

# Y si buscamos una clave que NO existe, no explota, nos da el default:
print(mi_diccionario['altura'])      # >> Valor no hallado
