for n in range (10, 20 , 2): # El bucle `for` se ejecutará para cada número en la secuencia generada por `range(10, 20, 2)`, que incluye los números 10, 12, 14, 16 y 18. En cada iteración, el número actual se asigna a la variable `n`, y se imprime su valor. Al finalizar el bucle, se habrán impreso todos los números pares entre 10 y 20 (excluyendo el 20).
    print(n)
    
    
mi_lista = list(range(1,101))
print(mi_lista) # La función `list()` se utiliza para convertir el objeto `range(1, 101)` en una lista de números enteros que van desde 1 hasta 100 (excluyendo el 101). Al imprimir `mi_lista`, se mostrará la lista completa de números del 1 al 100.


suma_cuadrados = range(1,15)

for num in range(1,15):
    suma_cuadrados += num ** 2 # En cada iteración del bucle, se calcula el cuadrado del número actual (`num ** 2`) y se suma al acumulador `suma_cuadrados`. Al finalizar el bucle, `suma_cuadrados` contendrá la suma total de los cuadrados de los números del 1 al 14.
    