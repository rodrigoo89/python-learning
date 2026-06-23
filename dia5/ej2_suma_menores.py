lista_numeros = [0, 10, 20, -20, 70]  # lista con valores positivos y negativos

def suma_menores(numeros):             # la función recibe la lista como parámetro
    suma = 0                           # iniciamos el acumulador en 0
    for n in numeros:                  # recorremos cada número de la lista
        if 0 < n < 1000:               # solo sumamos si es mayor a 0 y menor a 1000
            suma += n                  # acumulamos el número a suma
    return suma                        # devolvemos el resultado final

print(suma_menores(lista_numeros))     # llamamos la función y mostramos el resultado
