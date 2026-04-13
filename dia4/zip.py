nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
edades = [25, 30, 35, 40, 45, 50, 55, 60, 65]
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata", "San Miguel de Tucumán", "Salta", "Santa Fe"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")   
    

marcas = ["Nike", "Adidas", "Puma"]
productos = ["Zapatillas", "Ropa", "Accesorios"]


español = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "  cinco"]
ingles = ["one", "two", "three", "four","five"]

numeros = list(zip(español, portugues, ingles))