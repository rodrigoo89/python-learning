lista_numeros = [1,4,9,8,12,6,11]
def cantidad_pares(numeros):
   pares = 0
   for n in numeros:
       if n % 2 == 0:
           pares += 1
   return pares

print(cantidad_pares(lista_numeros))
